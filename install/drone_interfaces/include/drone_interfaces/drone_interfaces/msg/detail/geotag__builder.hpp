// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from drone_interfaces:msg/Geotag.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__GEOTAG__BUILDER_HPP_
#define DRONE_INTERFACES__MSG__DETAIL__GEOTAG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "drone_interfaces/msg/detail/geotag__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace drone_interfaces
{

namespace msg
{

namespace builder
{

class Init_Geotag_severity_score
{
public:
  explicit Init_Geotag_severity_score(::drone_interfaces::msg::Geotag & msg)
  : msg_(msg)
  {}
  ::drone_interfaces::msg::Geotag severity_score(::drone_interfaces::msg::Geotag::_severity_score_type arg)
  {
    msg_.severity_score = std::move(arg);
    return std::move(msg_);
  }

private:
  ::drone_interfaces::msg::Geotag msg_;
};

class Init_Geotag_alt
{
public:
  explicit Init_Geotag_alt(::drone_interfaces::msg::Geotag & msg)
  : msg_(msg)
  {}
  Init_Geotag_severity_score alt(::drone_interfaces::msg::Geotag::_alt_type arg)
  {
    msg_.alt = std::move(arg);
    return Init_Geotag_severity_score(msg_);
  }

private:
  ::drone_interfaces::msg::Geotag msg_;
};

class Init_Geotag_lon
{
public:
  explicit Init_Geotag_lon(::drone_interfaces::msg::Geotag & msg)
  : msg_(msg)
  {}
  Init_Geotag_alt lon(::drone_interfaces::msg::Geotag::_lon_type arg)
  {
    msg_.lon = std::move(arg);
    return Init_Geotag_alt(msg_);
  }

private:
  ::drone_interfaces::msg::Geotag msg_;
};

class Init_Geotag_lat
{
public:
  explicit Init_Geotag_lat(::drone_interfaces::msg::Geotag & msg)
  : msg_(msg)
  {}
  Init_Geotag_lon lat(::drone_interfaces::msg::Geotag::_lat_type arg)
  {
    msg_.lat = std::move(arg);
    return Init_Geotag_lon(msg_);
  }

private:
  ::drone_interfaces::msg::Geotag msg_;
};

class Init_Geotag_id
{
public:
  Init_Geotag_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Geotag_lat id(::drone_interfaces::msg::Geotag::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_Geotag_lat(msg_);
  }

private:
  ::drone_interfaces::msg::Geotag msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::drone_interfaces::msg::Geotag>()
{
  return drone_interfaces::msg::builder::Init_Geotag_id();
}

}  // namespace drone_interfaces

#endif  // DRONE_INTERFACES__MSG__DETAIL__GEOTAG__BUILDER_HPP_
