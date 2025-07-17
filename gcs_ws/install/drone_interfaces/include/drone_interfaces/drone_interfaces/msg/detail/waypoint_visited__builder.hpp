// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from drone_interfaces:msg/WaypointVisited.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_VISITED__BUILDER_HPP_
#define DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_VISITED__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "drone_interfaces/msg/detail/waypoint_visited__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace drone_interfaces
{

namespace msg
{

namespace builder
{

class Init_WaypointVisited_drone_id
{
public:
  explicit Init_WaypointVisited_drone_id(::drone_interfaces::msg::WaypointVisited & msg)
  : msg_(msg)
  {}
  ::drone_interfaces::msg::WaypointVisited drone_id(::drone_interfaces::msg::WaypointVisited::_drone_id_type arg)
  {
    msg_.drone_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::drone_interfaces::msg::WaypointVisited msg_;
};

class Init_WaypointVisited_waypoint_id
{
public:
  Init_WaypointVisited_waypoint_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_WaypointVisited_drone_id waypoint_id(::drone_interfaces::msg::WaypointVisited::_waypoint_id_type arg)
  {
    msg_.waypoint_id = std::move(arg);
    return Init_WaypointVisited_drone_id(msg_);
  }

private:
  ::drone_interfaces::msg::WaypointVisited msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::drone_interfaces::msg::WaypointVisited>()
{
  return drone_interfaces::msg::builder::Init_WaypointVisited_waypoint_id();
}

}  // namespace drone_interfaces

#endif  // DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_VISITED__BUILDER_HPP_
