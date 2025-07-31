// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from drone_interfaces:msg/GeotagVisited.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__GEOTAG_VISITED__BUILDER_HPP_
#define DRONE_INTERFACES__MSG__DETAIL__GEOTAG_VISITED__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "drone_interfaces/msg/detail/geotag_visited__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace drone_interfaces
{

namespace msg
{

namespace builder
{

class Init_GeotagVisited_geotag_id
{
public:
  explicit Init_GeotagVisited_geotag_id(::drone_interfaces::msg::GeotagVisited & msg)
  : msg_(msg)
  {}
  ::drone_interfaces::msg::GeotagVisited geotag_id(::drone_interfaces::msg::GeotagVisited::_geotag_id_type arg)
  {
    msg_.geotag_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::drone_interfaces::msg::GeotagVisited msg_;
};

class Init_GeotagVisited_drone_id
{
public:
  Init_GeotagVisited_drone_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GeotagVisited_geotag_id drone_id(::drone_interfaces::msg::GeotagVisited::_drone_id_type arg)
  {
    msg_.drone_id = std::move(arg);
    return Init_GeotagVisited_geotag_id(msg_);
  }

private:
  ::drone_interfaces::msg::GeotagVisited msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::drone_interfaces::msg::GeotagVisited>()
{
  return drone_interfaces::msg::builder::Init_GeotagVisited_drone_id();
}

}  // namespace drone_interfaces

#endif  // DRONE_INTERFACES__MSG__DETAIL__GEOTAG_VISITED__BUILDER_HPP_
