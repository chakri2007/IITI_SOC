#include <functional> 
#include <gazebo/gazebo.hh> 
#include <gazebo/physics/physics.hh> 
#include <gazebo/common/common.hh> 
#include <fstream>   // For file I/O operations (ifstream)
#include <string>    // For string manipulation
#include <map>       // For storing drone names and their water levels
#include <algorithm> // For std::max and std::min
#include <iostream>
using namespace std;

// Global variables (as per original code, their state is shared across plugin instances if multiple exist)


namespace gazebo
{
  class joint_c : public ModelPlugin
  {
  public: 
    void Load(physics::ModelPtr _parent, sdf::ElementPtr /*_sdf*/)
    {   
        // Store a pointer to the parent model (the model this plugin is attached to)
        this->model = _parent;
        // Get a pointer to the world
        this->world = this->model->GetWorld();

        // Get pointers to the specific drone models "iris_1" and "iris_2" as described
        this->iris_1_model = this->world->ModelByName("iris_1");
        this->iris_2_model = this->world->ModelByName("iris_2");

        // Error checking to ensure models are found
        if (!this->iris_1_model) {
            gzerr << "joint_c plugin: Model 'iris_1' not found. Make sure your world includes a model named 'iris_1'.\n";
        }
        if (!this->iris_2_model) {
            gzerr << "joint_c plugin: Model 'iris_2' not found. Make sure your world includes a model named 'iris_2'.\n";
        }

        // Get pointers to the base_link of each drone (assuming they both have a link named "base_link")
        if (this->iris_1_model) {
            this->iris_1_base_link = this->iris_1_model->GetLink("base_link");
            if (!this->iris_1_base_link) {
                gzerr << "joint_c plugin: Link 'base_link' not found for model 'iris_1'.\n";
            }
        }
        if (this->iris_2_model) {
            this->iris_2_base_link = this->iris_2_model->GetLink("base_link");
            if (!this->iris_2_base_link) {
                gzerr << "joint_c plugin: Link 'base_link' not found for model 'iris_2'.\n";
            }
        }

        // Listen to the WorldUpdateBegin event. This event is broadcast every simulation iteration.
        this->updateConnection = event::Events::ConnectWorldUpdateBegin(
            boost::bind(&joint_c::OnUpdate, this, _1));
    }

  public: 
    void OnUpdate(const common::UpdateInfo &_info)
    {
        // --- File Reading and Mass Calculation for Drones ---
        const std::string file_path = "/home/bhav/IITISoC-25-IVR09/gcs_ws/mission_files/water_levels.txt";
        std::ifstream file(file_path);
        
        // Check if the file was opened successfully
        if (!file.is_open()) {
            gzerr << "joint_c plugin: Failed to open water_level.txt at " << file_path << "\n";
        }

        std::string line;
        std::map<std::string, float> waterLevels; // Map to store drone name -> water level
        // Read the file line by line
        while (std::getline(file, line)) {
            size_t eqPos = line.find('='); // Find the position of '='
            if (eqPos != std::string::npos) {
                // Extract drone name (before '=')
                std::string droneName = line.substr(0, eqPos);
                // Trim leading/trailing whitespace from the drone name
                droneName.erase(0, droneName.find_first_not_of(" \t\n\r\f\v"));
                droneName.erase(droneName.find_last_not_of(" \t\n\r\f\v") + 1);

                // Extract value string (after '=')
                std::string valueStr = line.substr(eqPos + 1);
                try {
                    // Convert value string to float
                    float level = std::stof(valueStr);
                    waterLevels[droneName] = level;
                } catch (const std::invalid_argument& e) {
                    gzerr << "joint_c plugin: Invalid number format in water_levels.txt: '" << valueStr << "'. Error: " << e.what() << "\n";
                } catch (const std::out_of_range& e) {
                    gzerr << "joint_c plugin: Out of range value in water_levels.txt: '" << valueStr << "'. Error: " << e.what() << "\n";
                }
            }
        }
        file.close(); // Close the file after reading

        float water_level_1 = 0.0f; // Default water level for drone_1
        float water_level_2 = 0.0f; // Default water level for drone_2

        // Retrieve water levels for drone_1 and drone_2 from the map
        if (waterLevels.count("drone_1")) {
            water_level_1 = waterLevels["drone_1"];
        } else {
            gzwarn << "joint_c plugin: Water level for 'drone_1' not found in " << file_path << ". Defaulting to 0.\n";
        }
        if (waterLevels.count("drone_2")) {
            water_level_2 = waterLevels["drone_2"];
        } else {
            gzwarn << "joint_c plugin: Water level for 'drone_2' not found in " << file_path << ". Defaulting to 0.\n";
        }

        // Clamp water levels to ensure they are within the [0, 100] range
        water_level_1 = std::max(0.0f, std::min(100.0f, water_level_1));
        water_level_2 = std::max(0.0f, std::min(100.0f, water_level_2));

        const float FIXED_DRONE_MASS = 1.0f; // Fixed base mass of the drone
        // Calculate water mass: proportional to water_level (1.0f at 100%, 0.0f at 0%)
        float water_mass_1 = water_level_1 / 200.0f;
        float water_mass_2 = water_level_2 / 200.0f;

        // Calculate total mass for each drone
        // total_mass = fixed_drone_mass + water_mass_from_file + x_variable_mass
        float total_mass_1 = FIXED_DRONE_MASS + water_mass_1;
        float total_mass_2 = FIXED_DRONE_MASS + water_mass_2;
        
        cout<<"\n mass for drone2 : "<<total_mass_2;
        cout<<"\n mass for drone1 : "<<total_mass_1;
        
        // Ensure mass does not become non-positive
        total_mass_1 = std::max(0.1f, total_mass_1); 
        total_mass_2 = std::max(0.1f, total_mass_2);

        // Update mass for iris_1 (drone_1) if its model and link were found
        if (this->iris_1_model && this->iris_1_base_link) {
            this->iris_1_base_link->GetInertial()->SetMass(total_mass_1);
            this->iris_1_base_link->UpdateMass(); // Important: Call UpdateMass() after SetMass()
        }

        // Update mass for iris_2 (drone_2) if its model and link were found
        if (this->iris_2_model && this->iris_2_base_link) {
            this->iris_2_base_link->GetInertial()->SetMass(total_mass_2);
            this->iris_2_base_link->UpdateMass(); // Important: Call UpdateMass() after SetMass()
        }
    }

  private: 
      physics::ModelPtr model; // Pointer to the parent model this plugin is attached to
      physics::WorldPtr world; // Pointer to the Gazebo world

      // Pointers for iris_1 model and its base_link
      physics::ModelPtr iris_1_model;
      physics::LinkPtr  iris_1_base_link;

      // Pointers for iris_2 model and its base_link
      physics::ModelPtr iris_2_model;
      physics::LinkPtr  iris_2_base_link;

      event::ConnectionPtr updateConnection;   // Pointer to the update event connection
  };

  // Register this plugin with the simulator
  GZ_REGISTER_MODEL_PLUGIN(joint_c)
}
