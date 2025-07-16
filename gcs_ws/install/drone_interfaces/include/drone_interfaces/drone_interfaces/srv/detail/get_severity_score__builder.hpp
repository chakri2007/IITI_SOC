// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from drone_interfaces:srv/GetSeverityScore.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__SRV__DETAIL__GET_SEVERITY_SCORE__BUILDER_HPP_
#define DRONE_INTERFACES__SRV__DETAIL__GET_SEVERITY_SCORE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "drone_interfaces/srv/detail/get_severity_score__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace drone_interfaces
{

namespace srv
{

namespace builder
{

class Init_GetSeverityScore_Request_id
{
public:
  Init_GetSeverityScore_Request_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::drone_interfaces::srv::GetSeverityScore_Request id(::drone_interfaces::srv::GetSeverityScore_Request::_id_type arg)
  {
    msg_.id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::drone_interfaces::srv::GetSeverityScore_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::drone_interfaces::srv::GetSeverityScore_Request>()
{
  return drone_interfaces::srv::builder::Init_GetSeverityScore_Request_id();
}

}  // namespace drone_interfaces


namespace drone_interfaces
{

namespace srv
{

namespace builder
{

class Init_GetSeverityScore_Response_severity_score
{
public:
  Init_GetSeverityScore_Response_severity_score()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::drone_interfaces::srv::GetSeverityScore_Response severity_score(::drone_interfaces::srv::GetSeverityScore_Response::_severity_score_type arg)
  {
    msg_.severity_score = std::move(arg);
    return std::move(msg_);
  }

private:
  ::drone_interfaces::srv::GetSeverityScore_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::drone_interfaces::srv::GetSeverityScore_Response>()
{
  return drone_interfaces::srv::builder::Init_GetSeverityScore_Response_severity_score();
}

}  // namespace drone_interfaces

#endif  // DRONE_INTERFACES__SRV__DETAIL__GET_SEVERITY_SCORE__BUILDER_HPP_
