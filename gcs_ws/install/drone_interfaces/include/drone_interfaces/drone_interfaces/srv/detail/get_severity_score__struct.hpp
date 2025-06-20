// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from drone_interfaces:srv/GetSeverityScore.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__SRV__DETAIL__GET_SEVERITY_SCORE__STRUCT_HPP_
#define DRONE_INTERFACES__SRV__DETAIL__GET_SEVERITY_SCORE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__drone_interfaces__srv__GetSeverityScore_Request __attribute__((deprecated))
#else
# define DEPRECATED__drone_interfaces__srv__GetSeverityScore_Request __declspec(deprecated)
#endif

namespace drone_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GetSeverityScore_Request_
{
  using Type = GetSeverityScore_Request_<ContainerAllocator>;

  explicit GetSeverityScore_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0ul;
    }
  }

  explicit GetSeverityScore_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0ul;
    }
  }

  // field types and members
  using _id_type =
    uint32_t;
  _id_type id;

  // setters for named parameter idiom
  Type & set__id(
    const uint32_t & _arg)
  {
    this->id = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    drone_interfaces::srv::GetSeverityScore_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const drone_interfaces::srv::GetSeverityScore_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<drone_interfaces::srv::GetSeverityScore_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<drone_interfaces::srv::GetSeverityScore_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      drone_interfaces::srv::GetSeverityScore_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<drone_interfaces::srv::GetSeverityScore_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      drone_interfaces::srv::GetSeverityScore_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<drone_interfaces::srv::GetSeverityScore_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<drone_interfaces::srv::GetSeverityScore_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<drone_interfaces::srv::GetSeverityScore_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__drone_interfaces__srv__GetSeverityScore_Request
    std::shared_ptr<drone_interfaces::srv::GetSeverityScore_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__drone_interfaces__srv__GetSeverityScore_Request
    std::shared_ptr<drone_interfaces::srv::GetSeverityScore_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GetSeverityScore_Request_ & other) const
  {
    if (this->id != other.id) {
      return false;
    }
    return true;
  }
  bool operator!=(const GetSeverityScore_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GetSeverityScore_Request_

// alias to use template instance with default allocator
using GetSeverityScore_Request =
  drone_interfaces::srv::GetSeverityScore_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace drone_interfaces


#ifndef _WIN32
# define DEPRECATED__drone_interfaces__srv__GetSeverityScore_Response __attribute__((deprecated))
#else
# define DEPRECATED__drone_interfaces__srv__GetSeverityScore_Response __declspec(deprecated)
#endif

namespace drone_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GetSeverityScore_Response_
{
  using Type = GetSeverityScore_Response_<ContainerAllocator>;

  explicit GetSeverityScore_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->severity_score = 0;
    }
  }

  explicit GetSeverityScore_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->severity_score = 0;
    }
  }

  // field types and members
  using _severity_score_type =
    uint8_t;
  _severity_score_type severity_score;

  // setters for named parameter idiom
  Type & set__severity_score(
    const uint8_t & _arg)
  {
    this->severity_score = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    drone_interfaces::srv::GetSeverityScore_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const drone_interfaces::srv::GetSeverityScore_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<drone_interfaces::srv::GetSeverityScore_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<drone_interfaces::srv::GetSeverityScore_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      drone_interfaces::srv::GetSeverityScore_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<drone_interfaces::srv::GetSeverityScore_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      drone_interfaces::srv::GetSeverityScore_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<drone_interfaces::srv::GetSeverityScore_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<drone_interfaces::srv::GetSeverityScore_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<drone_interfaces::srv::GetSeverityScore_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__drone_interfaces__srv__GetSeverityScore_Response
    std::shared_ptr<drone_interfaces::srv::GetSeverityScore_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__drone_interfaces__srv__GetSeverityScore_Response
    std::shared_ptr<drone_interfaces::srv::GetSeverityScore_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GetSeverityScore_Response_ & other) const
  {
    if (this->severity_score != other.severity_score) {
      return false;
    }
    return true;
  }
  bool operator!=(const GetSeverityScore_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GetSeverityScore_Response_

// alias to use template instance with default allocator
using GetSeverityScore_Response =
  drone_interfaces::srv::GetSeverityScore_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace drone_interfaces

namespace drone_interfaces
{

namespace srv
{

struct GetSeverityScore
{
  using Request = drone_interfaces::srv::GetSeverityScore_Request;
  using Response = drone_interfaces::srv::GetSeverityScore_Response;
};

}  // namespace srv

}  // namespace drone_interfaces

#endif  // DRONE_INTERFACES__SRV__DETAIL__GET_SEVERITY_SCORE__STRUCT_HPP_
