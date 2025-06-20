// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from drone_interfaces:msg/DroneTypeChange.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__DRONE_TYPE_CHANGE__STRUCT_HPP_
#define DRONE_INTERFACES__MSG__DETAIL__DRONE_TYPE_CHANGE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__drone_interfaces__msg__DroneTypeChange __attribute__((deprecated))
#else
# define DEPRECATED__drone_interfaces__msg__DroneTypeChange __declspec(deprecated)
#endif

namespace drone_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct DroneTypeChange_
{
  using Type = DroneTypeChange_<ContainerAllocator>;

  explicit DroneTypeChange_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->new_drone_type = "";
    }
  }

  explicit DroneTypeChange_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : new_drone_type(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->new_drone_type = "";
    }
  }

  // field types and members
  using _new_drone_type_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _new_drone_type_type new_drone_type;

  // setters for named parameter idiom
  Type & set__new_drone_type(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->new_drone_type = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    drone_interfaces::msg::DroneTypeChange_<ContainerAllocator> *;
  using ConstRawPtr =
    const drone_interfaces::msg::DroneTypeChange_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<drone_interfaces::msg::DroneTypeChange_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<drone_interfaces::msg::DroneTypeChange_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      drone_interfaces::msg::DroneTypeChange_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<drone_interfaces::msg::DroneTypeChange_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      drone_interfaces::msg::DroneTypeChange_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<drone_interfaces::msg::DroneTypeChange_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<drone_interfaces::msg::DroneTypeChange_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<drone_interfaces::msg::DroneTypeChange_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__drone_interfaces__msg__DroneTypeChange
    std::shared_ptr<drone_interfaces::msg::DroneTypeChange_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__drone_interfaces__msg__DroneTypeChange
    std::shared_ptr<drone_interfaces::msg::DroneTypeChange_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DroneTypeChange_ & other) const
  {
    if (this->new_drone_type != other.new_drone_type) {
      return false;
    }
    return true;
  }
  bool operator!=(const DroneTypeChange_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DroneTypeChange_

// alias to use template instance with default allocator
using DroneTypeChange =
  drone_interfaces::msg::DroneTypeChange_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace drone_interfaces

#endif  // DRONE_INTERFACES__MSG__DETAIL__DRONE_TYPE_CHANGE__STRUCT_HPP_
