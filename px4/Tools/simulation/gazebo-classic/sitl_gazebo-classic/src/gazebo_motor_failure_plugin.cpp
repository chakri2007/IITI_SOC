/*
 * Copyright 2017 Nuno Marques, PX4 Pro Dev Team, Lisbon
 * Copyright 2017 Siddharth Patel, NTU Singapore
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0

 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include <gazebo_motor_failure_plugin.h>

#include <functional>
#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo/common/common.hh>
#include <thread>

float water_level_mass = 25.0;

namespace gazebo
{
  class joint_c : public ModelPlugin
  {
  public:
    void Load(physics::ModelPtr _parent, sdf::ElementPtr /*_sdf*/)
    {
      this->model = _parent;
      this->world = this->model->GetWorld();
      this->iris = this->world->ModelByName("iris");
      this->base_link = this->iris->GetLink("base_link");

      rclcpp::init(0, nullptr);
      node = rclcpp::Node::make_shared("water_mass_node");

      sub = node->create_subscription<std_msgs::msg::Float32>(
          "/water_level", 10,
          [](std_msgs::msg::Float32::SharedPtr msg)
          {
            water_level_mass = msg->data;
          });

      spinner = std::thread([]() { rclcpp::spin(node); });

      this->updateConnection = event::Events::ConnectWorldUpdateBegin(
          boost::bind(&joint_c::OnUpdate, this, _1));
    }

    void OnUpdate(const common::UpdateInfo &/*_info*/)
    {
      base_link->GetInertial()->SetMass(water_level_mass);
      base_link->UpdateMass();
      std::cout << "the mass is " << water_level_mass << std::endl;
    }

  private:
    physics::ModelPtr model;
    physics::ModelPtr iris;
    physics::WorldPtr world;
    physics::LinkPtr base_link;
    event::ConnectionPtr updateConnection;

    rclcpp::Node::SharedPtr node;
    rclcpp::Subscription<std_msgs::msg::Float32>::SharedPtr sub;
    std::thread spinner;
  };

  GZ_REGISTER_MODEL_PLUGIN(joint_c)
}




