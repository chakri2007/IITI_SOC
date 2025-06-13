// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from drone_interfaces:msg/WaypointArray.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_ARRAY__BUILDER_HPP_
#define DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_ARRAY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "drone_interfaces/msg/detail/waypoint_array__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace drone_interfaces
{

namespace msg
{

namespace builder
{

class Init_WaypointArray_waypoints
{
public:
  Init_WaypointArray_waypoints()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::drone_interfaces::msg::WaypointArray waypoints(::drone_interfaces::msg::WaypointArray::_waypoints_type arg)
  {
    msg_.waypoints = std::move(arg);
    return std::move(msg_);
  }

private:
  ::drone_interfaces::msg::WaypointArray msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::drone_interfaces::msg::WaypointArray>()
{
  return drone_interfaces::msg::builder::Init_WaypointArray_waypoints();
}

}  // namespace drone_interfaces

#endif  // DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_ARRAY__BUILDER_HPP_
