// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from drone_interfaces:msg/GeotagArray.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__GEOTAG_ARRAY__TRAITS_HPP_
#define DRONE_INTERFACES__MSG__DETAIL__GEOTAG_ARRAY__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "drone_interfaces/msg/detail/geotag_array__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'geotags'
#include "drone_interfaces/msg/detail/geotag__traits.hpp"

namespace drone_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const GeotagArray & msg,
  std::ostream & out)
{
  out << "{";
  // member: geotags
  {
    if (msg.geotags.size() == 0) {
      out << "geotags: []";
    } else {
      out << "geotags: [";
      size_t pending_items = msg.geotags.size();
      for (auto item : msg.geotags) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GeotagArray & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: geotags
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.geotags.size() == 0) {
      out << "geotags: []\n";
    } else {
      out << "geotags:\n";
      for (auto item : msg.geotags) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GeotagArray & msg, bool use_flow_style = false)
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
  const drone_interfaces::msg::GeotagArray & msg,
  std::ostream & out, size_t indentation = 0)
{
  drone_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use drone_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const drone_interfaces::msg::GeotagArray & msg)
{
  return drone_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<drone_interfaces::msg::GeotagArray>()
{
  return "drone_interfaces::msg::GeotagArray";
}

template<>
inline const char * name<drone_interfaces::msg::GeotagArray>()
{
  return "drone_interfaces/msg/GeotagArray";
}

template<>
struct has_fixed_size<drone_interfaces::msg::GeotagArray>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<drone_interfaces::msg::GeotagArray>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<drone_interfaces::msg::GeotagArray>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // DRONE_INTERFACES__MSG__DETAIL__GEOTAG_ARRAY__TRAITS_HPP_
