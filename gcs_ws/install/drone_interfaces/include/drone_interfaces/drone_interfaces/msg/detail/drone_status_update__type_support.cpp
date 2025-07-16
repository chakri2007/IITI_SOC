// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from drone_interfaces:msg/DroneStatusUpdate.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "drone_interfaces/msg/detail/drone_status_update__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace drone_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void DroneStatusUpdate_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) drone_interfaces::msg::DroneStatusUpdate(_init);
}

void DroneStatusUpdate_fini_function(void * message_memory)
{
  auto typed_message = static_cast<drone_interfaces::msg::DroneStatusUpdate *>(message_memory);
  typed_message->~DroneStatusUpdate();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember DroneStatusUpdate_message_member_array[2] = {
  {
    "drone_id",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_interfaces::msg::DroneStatusUpdate, drone_id),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "status",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_interfaces::msg::DroneStatusUpdate, status),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers DroneStatusUpdate_message_members = {
  "drone_interfaces::msg",  // message namespace
  "DroneStatusUpdate",  // message name
  2,  // number of fields
  sizeof(drone_interfaces::msg::DroneStatusUpdate),
  DroneStatusUpdate_message_member_array,  // message members
  DroneStatusUpdate_init_function,  // function to initialize message memory (memory has to be allocated)
  DroneStatusUpdate_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t DroneStatusUpdate_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &DroneStatusUpdate_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace drone_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<drone_interfaces::msg::DroneStatusUpdate>()
{
  return &::drone_interfaces::msg::rosidl_typesupport_introspection_cpp::DroneStatusUpdate_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, drone_interfaces, msg, DroneStatusUpdate)() {
  return &::drone_interfaces::msg::rosidl_typesupport_introspection_cpp::DroneStatusUpdate_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
