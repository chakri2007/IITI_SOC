// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from drone_interfaces:msg/WaypointArray.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_ARRAY__STRUCT_HPP_
#define DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_ARRAY__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'waypoints'
#include "drone_interfaces/msg/detail/waypoint__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__drone_interfaces__msg__WaypointArray __attribute__((deprecated))
#else
# define DEPRECATED__drone_interfaces__msg__WaypointArray __declspec(deprecated)
#endif

namespace drone_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct WaypointArray_
{
  using Type = WaypointArray_<ContainerAllocator>;

  explicit WaypointArray_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit WaypointArray_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _waypoints_type =
    std::vector<drone_interfaces::msg::Waypoint_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<drone_interfaces::msg::Waypoint_<ContainerAllocator>>>;
  _waypoints_type waypoints;

  // setters for named parameter idiom
  Type & set__waypoints(
    const std::vector<drone_interfaces::msg::Waypoint_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<drone_interfaces::msg::Waypoint_<ContainerAllocator>>> & _arg)
  {
    this->waypoints = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    drone_interfaces::msg::WaypointArray_<ContainerAllocator> *;
  using ConstRawPtr =
    const drone_interfaces::msg::WaypointArray_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<drone_interfaces::msg::WaypointArray_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<drone_interfaces::msg::WaypointArray_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      drone_interfaces::msg::WaypointArray_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<drone_interfaces::msg::WaypointArray_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      drone_interfaces::msg::WaypointArray_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<drone_interfaces::msg::WaypointArray_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<drone_interfaces::msg::WaypointArray_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<drone_interfaces::msg::WaypointArray_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__drone_interfaces__msg__WaypointArray
    std::shared_ptr<drone_interfaces::msg::WaypointArray_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__drone_interfaces__msg__WaypointArray
    std::shared_ptr<drone_interfaces::msg::WaypointArray_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const WaypointArray_ & other) const
  {
    if (this->waypoints != other.waypoints) {
      return false;
    }
    return true;
  }
  bool operator!=(const WaypointArray_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct WaypointArray_

// alias to use template instance with default allocator
using WaypointArray =
  drone_interfaces::msg::WaypointArray_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace drone_interfaces

#endif  // DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_ARRAY__STRUCT_HPP_
