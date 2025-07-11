// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from drone_interfaces:msg/DroneStatusUpdate.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__DRONE_STATUS_UPDATE__BUILDER_HPP_
#define DRONE_INTERFACES__MSG__DETAIL__DRONE_STATUS_UPDATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "drone_interfaces/msg/detail/drone_status_update__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace drone_interfaces
{

namespace msg
{

namespace builder
{

class Init_DroneStatusUpdate_status
{
public:
  explicit Init_DroneStatusUpdate_status(::drone_interfaces::msg::DroneStatusUpdate & msg)
  : msg_(msg)
  {}
  ::drone_interfaces::msg::DroneStatusUpdate status(::drone_interfaces::msg::DroneStatusUpdate::_status_type arg)
  {
    msg_.status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::drone_interfaces::msg::DroneStatusUpdate msg_;
};

class Init_DroneStatusUpdate_drone_id
{
public:
  Init_DroneStatusUpdate_drone_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DroneStatusUpdate_status drone_id(::drone_interfaces::msg::DroneStatusUpdate::_drone_id_type arg)
  {
    msg_.drone_id = std::move(arg);
    return Init_DroneStatusUpdate_status(msg_);
  }

private:
  ::drone_interfaces::msg::DroneStatusUpdate msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::drone_interfaces::msg::DroneStatusUpdate>()
{
  return drone_interfaces::msg::builder::Init_DroneStatusUpdate_drone_id();
}

}  // namespace drone_interfaces

#endif  // DRONE_INTERFACES__MSG__DETAIL__DRONE_STATUS_UPDATE__BUILDER_HPP_
