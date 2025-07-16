// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from drone_interfaces:msg/SurveillanceStatus.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__SURVEILLANCE_STATUS__TRAITS_HPP_
#define DRONE_INTERFACES__MSG__DETAIL__SURVEILLANCE_STATUS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "drone_interfaces/msg/detail/surveillance_status__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace drone_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const SurveillanceStatus & msg,
  std::ostream & out)
{
  out << "{";
  // member: surveillance_completed
  {
    out << "surveillance_completed: ";
    rosidl_generator_traits::value_to_yaml(msg.surveillance_completed, out);
    out << ", ";
  }

  // member: waypoints_remaining
  {
    out << "waypoints_remaining: ";
    rosidl_generator_traits::value_to_yaml(msg.waypoints_remaining, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SurveillanceStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: surveillance_completed
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "surveillance_completed: ";
    rosidl_generator_traits::value_to_yaml(msg.surveillance_completed, out);
    out << "\n";
  }

  // member: waypoints_remaining
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "waypoints_remaining: ";
    rosidl_generator_traits::value_to_yaml(msg.waypoints_remaining, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SurveillanceStatus & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace drone_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use drone_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const drone_interfaces::msg::SurveillanceStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  drone_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use drone_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const drone_interfaces::msg::SurveillanceStatus & msg)
{
  return drone_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<drone_interfaces::msg::SurveillanceStatus>()
{
  return "drone_interfaces::msg::SurveillanceStatus";
}

template<>
inline const char * name<drone_interfaces::msg::SurveillanceStatus>()
{
  return "drone_interfaces/msg/SurveillanceStatus";
}

template<>
struct has_fixed_size<drone_interfaces::msg::SurveillanceStatus>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<drone_interfaces::msg::SurveillanceStatus>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<drone_interfaces::msg::SurveillanceStatus>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // DRONE_INTERFACES__MSG__DETAIL__SURVEILLANCE_STATUS__TRAITS_HPP_
