// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from drone_interfaces:msg/GeotagRequest.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__GEOTAG_REQUEST__BUILDER_HPP_
#define DRONE_INTERFACES__MSG__DETAIL__GEOTAG_REQUEST__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "drone_interfaces/msg/detail/geotag_request__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace drone_interfaces
{

namespace msg
{

namespace builder
{

class Init_GeotagRequest_direction
{
public:
  explicit Init_GeotagRequest_direction(::drone_interfaces::msg::GeotagRequest & msg)
  : msg_(msg)
  {}
  ::drone_interfaces::msg::GeotagRequest direction(::drone_interfaces::msg::GeotagRequest::_direction_type arg)
  {
    msg_.direction = std::move(arg);
    return std::move(msg_);
  }

private:
  ::drone_interfaces::msg::GeotagRequest msg_;
};

class Init_GeotagRequest_drone_id
{
public:
  Init_GeotagRequest_drone_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GeotagRequest_direction drone_id(::drone_interfaces::msg::GeotagRequest::_drone_id_type arg)
  {
    msg_.drone_id = std::move(arg);
    return Init_GeotagRequest_direction(msg_);
  }

private:
  ::drone_interfaces::msg::GeotagRequest msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::drone_interfaces::msg::GeotagRequest>()
{
  return drone_interfaces::msg::builder::Init_GeotagRequest_drone_id();
}

}  // namespace drone_interfaces

#endif  // DRONE_INTERFACES__MSG__DETAIL__GEOTAG_REQUEST__BUILDER_HPP_
