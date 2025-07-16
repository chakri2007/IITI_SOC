// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from drone_interfaces:msg/Waypoint.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__WAYPOINT__BUILDER_HPP_
#define DRONE_INTERFACES__MSG__DETAIL__WAYPOINT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "drone_interfaces/msg/detail/waypoint__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace drone_interfaces
{

namespace msg
{

namespace builder
{

class Init_Waypoint_visited
{
public:
  explicit Init_Waypoint_visited(::drone_interfaces::msg::Waypoint & msg)
  : msg_(msg)
  {}
  ::drone_interfaces::msg::Waypoint visited(::drone_interfaces::msg::Waypoint::_visited_type arg)
  {
    msg_.visited = std::move(arg);
    return std::move(msg_);
  }

private:
  ::drone_interfaces::msg::Waypoint msg_;
};

class Init_Waypoint_alt
{
public:
  explicit Init_Waypoint_alt(::drone_interfaces::msg::Waypoint & msg)
  : msg_(msg)
  {}
  Init_Waypoint_visited alt(::drone_interfaces::msg::Waypoint::_alt_type arg)
  {
    msg_.alt = std::move(arg);
    return Init_Waypoint_visited(msg_);
  }

private:
  ::drone_interfaces::msg::Waypoint msg_;
};

class Init_Waypoint_lon
{
public:
  explicit Init_Waypoint_lon(::drone_interfaces::msg::Waypoint & msg)
  : msg_(msg)
  {}
  Init_Waypoint_alt lon(::drone_interfaces::msg::Waypoint::_lon_type arg)
  {
    msg_.lon = std::move(arg);
    return Init_Waypoint_alt(msg_);
  }

private:
  ::drone_interfaces::msg::Waypoint msg_;
};

class Init_Waypoint_lat
{
public:
  explicit Init_Waypoint_lat(::drone_interfaces::msg::Waypoint & msg)
  : msg_(msg)
  {}
  Init_Waypoint_lon lat(::drone_interfaces::msg::Waypoint::_lat_type arg)
  {
    msg_.lat = std::move(arg);
    return Init_Waypoint_lon(msg_);
  }

private:
  ::drone_interfaces::msg::Waypoint msg_;
};

class Init_Waypoint_id
{
public:
  Init_Waypoint_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Waypoint_lat id(::drone_interfaces::msg::Waypoint::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_Waypoint_lat(msg_);
  }

private:
  ::drone_interfaces::msg::Waypoint msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::drone_interfaces::msg::Waypoint>()
{
  return drone_interfaces::msg::builder::Init_Waypoint_id();
}

}  // namespace drone_interfaces

#endif  // DRONE_INTERFACES__MSG__DETAIL__WAYPOINT__BUILDER_HPP_
