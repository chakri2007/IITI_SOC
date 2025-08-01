#ifndef GAZEBO_VARIABLE_MASS_PLUGIN_HPP_
#define GAZEBO_VARIABLE_MASS_PLUGIN_HPP_

#include <string>
#include <thread>
#include <memory> // For std::shared_ptr

#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo/common/common.hh>
// #include <rclcpp/rclcpp.hpp>
// #include <std_msgs/msg/float32.hpp>

namespace gazebo {

/// \brief A Gazebo plugin that allows changing the mass of a specified link
///        dynamically based on ROS2 topic messages.
class GazeboVariableMass : public ModelPlugin {
public:
    /// \brief Constructor
    GazeboVariableMass();

    /// \brief Destructor
    virtual ~GazeboVariableMass();

protected:
    /// \brief Gazebo's Load function, called when the plugin is loaded.
    /// \param[in] _model Pointer to the Gazebo model this plugin is attached to.
    /// \param[in] _sdf Pointer to the SDF element for this plugin.
    virtual void Load(physics::ModelPtr _model, sdf::ElementPtr _sdf);

    /// \brief Gazebo's OnUpdate function, called on every world update.
    /// \param[in] _info Current update information.
    virtual void OnUpdate(const common::UpdateInfo & /*_info*/);

private:
    /// \brief Callback function for the ROS2 /water_level topic.
    /// \param[in] msg The received Float32 message containing the new mass value.
    void WaterLevelCallback(const std_msgs::msg::Float32::SharedPtr msg);

    physics::ModelPtr model_;       ///< Pointer to the Gazebo model this plugin is attached to.
    physics::ModelPtr iris_model_;  ///< Pointer to the "iris" model (or specified model).
    physics::LinkPtr base_link_;    ///< Pointer to the "base_link" (or specified link) whose mass will be updated.

    event::ConnectionPtr updateConnection_; ///< Connection to the world update event.

    // ROS2 related members
    rclcpp::Node::SharedPtr ros_node_;                 ///< ROS2 node for communication.
    rclcpp::Subscription<std_msgs::msg::Float32>::SharedPtr water_level_sub_; ///< Subscriber to the water level topic.
    std::thread ros_spinner_thread_;                   ///< Thread to run the ROS2 event loop.

    float current_variable_mass_; ///< Stores the current mass value received from ROS2.

    std::string iris; ///< Name of the model to find (e.g., "iris").
    std::string base_link;  ///< Name of the link within the model to modify (e.g., "base_link").
    std::string water_level; ///< ROS topic to subscribe to (e.g., "/water_level").
};

} // namespace gazebo

#endif // GAZEBO_VARIABLE_MASS_PLUGIN_HPP_