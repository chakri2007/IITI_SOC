// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from drone_interfaces:msg/Waypoint.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__WAYPOINT__STRUCT_HPP_
#define DRONE_INTERFACES__MSG__DETAIL__WAYPOINT__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__drone_interfaces__msg__Waypoint __attribute__((deprecated))
#else
# define DEPRECATED__drone_interfaces__msg__Waypoint __declspec(deprecated)
#endif

namespace drone_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Waypoint_
{
  using Type = Waypoint_<ContainerAllocator>;

  explicit Waypoint_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0l;
      this->lat = 0.0;
      this->lon = 0.0;
      this->alt = 0.0;
      this->visited = false;
    }
  }

  explicit Waypoint_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0l;
      this->lat = 0.0;
      this->lon = 0.0;
      this->alt = 0.0;
      this->visited = false;
    }
  }

  // field types and members
  using _id_type =
    int32_t;
  _id_type id;
  using _lat_type =
    double;
  _lat_type lat;
  using _lon_type =
    double;
  _lon_type lon;
  using _alt_type =
    double;
  _alt_type alt;
  using _visited_type =
    bool;
  _visited_type visited;

  // setters for named parameter idiom
  Type & set__id(
    const int32_t & _arg)
  {
    this->id = _arg;
    return *this;
  }
  Type & set__lat(
    const double & _arg)
  {
    this->lat = _arg;
    return *this;
  }
  Type & set__lon(
    const double & _arg)
  {
    this->lon = _arg;
    return *this;
  }
  Type & set__alt(
    const double & _arg)
  {
    this->alt = _arg;
    return *this;
  }
  Type & set__visited(
    const bool & _arg)
  {
    this->visited = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    drone_interfaces::msg::Waypoint_<ContainerAllocator> *;
  using ConstRawPtr =
    const drone_interfaces::msg::Waypoint_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<drone_interfaces::msg::Waypoint_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<drone_interfaces::msg::Waypoint_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      drone_interfaces::msg::Waypoint_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<drone_interfaces::msg::Waypoint_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      drone_interfaces::msg::Waypoint_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<drone_interfaces::msg::Waypoint_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<drone_interfaces::msg::Waypoint_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<drone_interfaces::msg::Waypoint_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__drone_interfaces__msg__Waypoint
    std::shared_ptr<drone_interfaces::msg::Waypoint_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__drone_interfaces__msg__Waypoint
    std::shared_ptr<drone_interfaces::msg::Waypoint_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Waypoint_ & other) const
  {
    if (this->id != other.id) {
      return false;
    }
    if (this->lat != other.lat) {
      return false;
    }
    if (this->lon != other.lon) {
      return false;
    }
    if (this->alt != other.alt) {
      return false;
    }
    if (this->visited != other.visited) {
      return false;
    }
    return true;
  }
  bool operator!=(const Waypoint_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Waypoint_

// alias to use template instance with default allocator
using Waypoint =
  drone_interfaces::msg::Waypoint_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace drone_interfaces

#endif  // DRONE_INTERFACES__MSG__DETAIL__WAYPOINT__STRUCT_HPP_
