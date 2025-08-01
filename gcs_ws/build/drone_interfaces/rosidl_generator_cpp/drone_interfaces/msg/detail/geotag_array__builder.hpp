// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from drone_interfaces:msg/GeotagArray.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__GEOTAG_ARRAY__BUILDER_HPP_
#define DRONE_INTERFACES__MSG__DETAIL__GEOTAG_ARRAY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "drone_interfaces/msg/detail/geotag_array__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace drone_interfaces
{

namespace msg
{

namespace builder
{

class Init_GeotagArray_geotags
{
public:
  Init_GeotagArray_geotags()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::drone_interfaces::msg::GeotagArray geotags(::drone_interfaces::msg::GeotagArray::_geotags_type arg)
  {
    msg_.geotags = std::move(arg);
    return std::move(msg_);
  }

private:
  ::drone_interfaces::msg::GeotagArray msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::drone_interfaces::msg::GeotagArray>()
{
  return drone_interfaces::msg::builder::Init_GeotagArray_geotags();
}

}  // namespace drone_interfaces

#endif  // DRONE_INTERFACES__MSG__DETAIL__GEOTAG_ARRAY__BUILDER_HPP_
