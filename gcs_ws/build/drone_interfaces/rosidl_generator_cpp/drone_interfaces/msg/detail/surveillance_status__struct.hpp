// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from drone_interfaces:msg/SurveillanceStatus.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__SURVEILLANCE_STATUS__STRUCT_HPP_
#define DRONE_INTERFACES__MSG__DETAIL__SURVEILLANCE_STATUS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__drone_interfaces__msg__SurveillanceStatus __attribute__((deprecated))
#else
# define DEPRECATED__drone_interfaces__msg__SurveillanceStatus __declspec(deprecated)
#endif

namespace drone_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct SurveillanceStatus_
{
  using Type = SurveillanceStatus_<ContainerAllocator>;

  explicit SurveillanceStatus_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->surveillance_completed = false;
      this->waypoints_remaining = 0l;
    }
  }

  explicit SurveillanceStatus_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->surveillance_completed = false;
      this->waypoints_remaining = 0l;
    }
  }

  // field types and members
  using _surveillance_completed_type =
    bool;
  _surveillance_completed_type surveillance_completed;
  using _waypoints_remaining_type =
    int32_t;
  _waypoints_remaining_type waypoints_remaining;

  // setters for named parameter idiom
  Type & set__surveillance_completed(
    const bool & _arg)
  {
    this->surveillance_completed = _arg;
    return *this;
  }
  Type & set__waypoints_remaining(
    const int32_t & _arg)
  {
    this->waypoints_remaining = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    drone_interfaces::msg::SurveillanceStatus_<ContainerAllocator> *;
  using ConstRawPtr =
    const drone_interfaces::msg::SurveillanceStatus_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<drone_interfaces::msg::SurveillanceStatus_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<drone_interfaces::msg::SurveillanceStatus_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      drone_interfaces::msg::SurveillanceStatus_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<drone_interfaces::msg::SurveillanceStatus_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      drone_interfaces::msg::SurveillanceStatus_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<drone_interfaces::msg::SurveillanceStatus_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<drone_interfaces::msg::SurveillanceStatus_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<drone_interfaces::msg::SurveillanceStatus_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__drone_interfaces__msg__SurveillanceStatus
    std::shared_ptr<drone_interfaces::msg::SurveillanceStatus_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__drone_interfaces__msg__SurveillanceStatus
    std::shared_ptr<drone_interfaces::msg::SurveillanceStatus_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SurveillanceStatus_ & other) const
  {
    if (this->surveillance_completed != other.surveillance_completed) {
      return false;
    }
    if (this->waypoints_remaining != other.waypoints_remaining) {
      return false;
    }
    return true;
  }
  bool operator!=(const SurveillanceStatus_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SurveillanceStatus_

// alias to use template instance with default allocator
using SurveillanceStatus =
  drone_interfaces::msg::SurveillanceStatus_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace drone_interfaces

#endif  // DRONE_INTERFACES__MSG__DETAIL__SURVEILLANCE_STATUS__STRUCT_HPP_
