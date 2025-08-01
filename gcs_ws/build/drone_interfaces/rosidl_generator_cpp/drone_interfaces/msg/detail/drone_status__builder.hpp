// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from drone_interfaces:msg/DroneStatus.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__DRONE_STATUS__BUILDER_HPP_
#define DRONE_INTERFACES__MSG__DETAIL__DRONE_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "drone_interfaces/msg/detail/drone_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace drone_interfaces
{

namespace msg
{

namespace builder
{

class Init_DroneStatus_direction
{
public:
  explicit Init_DroneStatus_direction(::drone_interfaces::msg::DroneStatus & msg)
  : msg_(msg)
  {}
  ::drone_interfaces::msg::DroneStatus direction(::drone_interfaces::msg::DroneStatus::_direction_type arg)
  {
    msg_.direction = std::move(arg);
    return std::move(msg_);
  }

private:
  ::drone_interfaces::msg::DroneStatus msg_;
};

class Init_DroneStatus_status
{
public:
  explicit Init_DroneStatus_status(::drone_interfaces::msg::DroneStatus & msg)
  : msg_(msg)
  {}
  Init_DroneStatus_direction status(::drone_interfaces::msg::DroneStatus::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_DroneStatus_direction(msg_);
  }

private:
  ::drone_interfaces::msg::DroneStatus msg_;
};

class Init_DroneStatus_type
{
public:
  explicit Init_DroneStatus_type(::drone_interfaces::msg::DroneStatus & msg)
  : msg_(msg)
  {}
  Init_DroneStatus_status type(::drone_interfaces::msg::DroneStatus::_type_type arg)
  {
    msg_.type = std::move(arg);
    return Init_DroneStatus_status(msg_);
  }

private:
  ::drone_interfaces::msg::DroneStatus msg_;
};

class Init_DroneStatus_drone_id
{
public:
  Init_DroneStatus_drone_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DroneStatus_type drone_id(::drone_interfaces::msg::DroneStatus::_drone_id_type arg)
  {
    msg_.drone_id = std::move(arg);
    return Init_DroneStatus_type(msg_);
  }

private:
  ::drone_interfaces::msg::DroneStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::drone_interfaces::msg::DroneStatus>()
{
  return drone_interfaces::msg::builder::Init_DroneStatus_drone_id();
}

}  // namespace drone_interfaces

#endif  // DRONE_INTERFACES__MSG__DETAIL__DRONE_STATUS__BUILDER_HPP_
