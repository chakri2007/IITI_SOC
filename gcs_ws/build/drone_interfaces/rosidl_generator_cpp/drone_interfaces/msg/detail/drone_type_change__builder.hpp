// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from drone_interfaces:msg/DroneTypeChange.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__DRONE_TYPE_CHANGE__BUILDER_HPP_
#define DRONE_INTERFACES__MSG__DETAIL__DRONE_TYPE_CHANGE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "drone_interfaces/msg/detail/drone_type_change__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace drone_interfaces
{

namespace msg
{

namespace builder
{

class Init_DroneTypeChange_new_drone_type
{
public:
  Init_DroneTypeChange_new_drone_type()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::drone_interfaces::msg::DroneTypeChange new_drone_type(::drone_interfaces::msg::DroneTypeChange::_new_drone_type_type arg)
  {
    msg_.new_drone_type = std::move(arg);
    return std::move(msg_);
  }

private:
  ::drone_interfaces::msg::DroneTypeChange msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::drone_interfaces::msg::DroneTypeChange>()
{
  return drone_interfaces::msg::builder::Init_DroneTypeChange_new_drone_type();
}

}  // namespace drone_interfaces

#endif  // DRONE_INTERFACES__MSG__DETAIL__DRONE_TYPE_CHANGE__BUILDER_HPP_
