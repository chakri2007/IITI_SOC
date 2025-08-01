// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from drone_interfaces:msg/WaypointRequest.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_REQUEST__BUILDER_HPP_
#define DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_REQUEST__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "drone_interfaces/msg/detail/waypoint_request__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace drone_interfaces
{

namespace msg
{

namespace builder
{

class Init_WaypointRequest_direction
{
public:
  explicit Init_WaypointRequest_direction(::drone_interfaces::msg::WaypointRequest & msg)
  : msg_(msg)
  {}
  ::drone_interfaces::msg::WaypointRequest direction(::drone_interfaces::msg::WaypointRequest::_direction_type arg)
  {
    msg_.direction = std::move(arg);
    return std::move(msg_);
  }

private:
  ::drone_interfaces::msg::WaypointRequest msg_;
};

class Init_WaypointRequest_drone_id
{
public:
  Init_WaypointRequest_drone_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_WaypointRequest_direction drone_id(::drone_interfaces::msg::WaypointRequest::_drone_id_type arg)
  {
    msg_.drone_id = std::move(arg);
    return Init_WaypointRequest_direction(msg_);
  }

private:
  ::drone_interfaces::msg::WaypointRequest msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::drone_interfaces::msg::WaypointRequest>()
{
  return drone_interfaces::msg::builder::Init_WaypointRequest_drone_id();
}

}  // namespace drone_interfaces

#endif  // DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_REQUEST__BUILDER_HPP_
