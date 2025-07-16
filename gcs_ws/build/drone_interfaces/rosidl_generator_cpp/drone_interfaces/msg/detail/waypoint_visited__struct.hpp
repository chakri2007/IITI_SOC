// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from drone_interfaces:msg/WaypointVisited.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_VISITED__STRUCT_HPP_
#define DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_VISITED__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__drone_interfaces__msg__WaypointVisited __attribute__((deprecated))
#else
# define DEPRECATED__drone_interfaces__msg__WaypointVisited __declspec(deprecated)
#endif

namespace drone_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct WaypointVisited_
{
  using Type = WaypointVisited_<ContainerAllocator>;

  explicit WaypointVisited_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->waypoint_id = 0l;
      this->drone_id = "";
    }
  }

  explicit WaypointVisited_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : drone_id(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->waypoint_id = 0l;
      this->drone_id = "";
    }
  }

  // field types and members
  using _waypoint_id_type =
    int32_t;
  _waypoint_id_type waypoint_id;
  using _drone_id_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _drone_id_type drone_id;

  // setters for named parameter idiom
  Type & set__waypoint_id(
    const int32_t & _arg)
  {
    this->waypoint_id = _arg;
    return *this;
  }
  Type & set__drone_id(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->drone_id = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    drone_interfaces::msg::WaypointVisited_<ContainerAllocator> *;
  using ConstRawPtr =
    const drone_interfaces::msg::WaypointVisited_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<drone_interfaces::msg::WaypointVisited_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<drone_interfaces::msg::WaypointVisited_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      drone_interfaces::msg::WaypointVisited_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<drone_interfaces::msg::WaypointVisited_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      drone_interfaces::msg::WaypointVisited_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<drone_interfaces::msg::WaypointVisited_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<drone_interfaces::msg::WaypointVisited_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<drone_interfaces::msg::WaypointVisited_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__drone_interfaces__msg__WaypointVisited
    std::shared_ptr<drone_interfaces::msg::WaypointVisited_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__drone_interfaces__msg__WaypointVisited
    std::shared_ptr<drone_interfaces::msg::WaypointVisited_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const WaypointVisited_ & other) const
  {
    if (this->waypoint_id != other.waypoint_id) {
      return false;
    }
    if (this->drone_id != other.drone_id) {
      return false;
    }
    return true;
  }
  bool operator!=(const WaypointVisited_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct WaypointVisited_

// alias to use template instance with default allocator
using WaypointVisited =
  drone_interfaces::msg::WaypointVisited_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace drone_interfaces

#endif  // DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_VISITED__STRUCT_HPP_
