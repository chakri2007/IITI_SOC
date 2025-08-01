// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from drone_interfaces:msg/SurveillanceStatus.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__SURVEILLANCE_STATUS__BUILDER_HPP_
#define DRONE_INTERFACES__MSG__DETAIL__SURVEILLANCE_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "drone_interfaces/msg/detail/surveillance_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace drone_interfaces
{

namespace msg
{

namespace builder
{

class Init_SurveillanceStatus_waypoints_remaining
{
public:
  explicit Init_SurveillanceStatus_waypoints_remaining(::drone_interfaces::msg::SurveillanceStatus & msg)
  : msg_(msg)
  {}
  ::drone_interfaces::msg::SurveillanceStatus waypoints_remaining(::drone_interfaces::msg::SurveillanceStatus::_waypoints_remaining_type arg)
  {
    msg_.waypoints_remaining = std::move(arg);
    return std::move(msg_);
  }

private:
  ::drone_interfaces::msg::SurveillanceStatus msg_;
};

class Init_SurveillanceStatus_surveillance_completed
{
public:
  Init_SurveillanceStatus_surveillance_completed()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SurveillanceStatus_waypoints_remaining surveillance_completed(::drone_interfaces::msg::SurveillanceStatus::_surveillance_completed_type arg)
  {
    msg_.surveillance_completed = std::move(arg);
    return Init_SurveillanceStatus_waypoints_remaining(msg_);
  }

private:
  ::drone_interfaces::msg::SurveillanceStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::drone_interfaces::msg::SurveillanceStatus>()
{
  return drone_interfaces::msg::builder::Init_SurveillanceStatus_surveillance_completed();
}

}  // namespace drone_interfaces

#endif  // DRONE_INTERFACES__MSG__DETAIL__SURVEILLANCE_STATUS__BUILDER_HPP_
