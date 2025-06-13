// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from drone_interfaces:msg/DroneStatus.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "drone_interfaces/msg/detail/drone_status__rosidl_typesupport_introspection_c.h"
#include "drone_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "drone_interfaces/msg/detail/drone_status__functions.h"
#include "drone_interfaces/msg/detail/drone_status__struct.h"


// Include directives for member types
// Member `drone_id`
// Member `type`
// Member `status`
// Member `direction`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void drone_interfaces__msg__DroneStatus__rosidl_typesupport_introspection_c__DroneStatus_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  drone_interfaces__msg__DroneStatus__init(message_memory);
}

void drone_interfaces__msg__DroneStatus__rosidl_typesupport_introspection_c__DroneStatus_fini_function(void * message_memory)
{
  drone_interfaces__msg__DroneStatus__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember drone_interfaces__msg__DroneStatus__rosidl_typesupport_introspection_c__DroneStatus_message_member_array[4] = {
  {
    "drone_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_interfaces__msg__DroneStatus, drone_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "type",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_interfaces__msg__DroneStatus, type),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "status",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_interfaces__msg__DroneStatus, status),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "direction",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_interfaces__msg__DroneStatus, direction),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers drone_interfaces__msg__DroneStatus__rosidl_typesupport_introspection_c__DroneStatus_message_members = {
  "drone_interfaces__msg",  // message namespace
  "DroneStatus",  // message name
  4,  // number of fields
  sizeof(drone_interfaces__msg__DroneStatus),
  drone_interfaces__msg__DroneStatus__rosidl_typesupport_introspection_c__DroneStatus_message_member_array,  // message members
  drone_interfaces__msg__DroneStatus__rosidl_typesupport_introspection_c__DroneStatus_init_function,  // function to initialize message memory (memory has to be allocated)
  drone_interfaces__msg__DroneStatus__rosidl_typesupport_introspection_c__DroneStatus_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t drone_interfaces__msg__DroneStatus__rosidl_typesupport_introspection_c__DroneStatus_message_type_support_handle = {
  0,
  &drone_interfaces__msg__DroneStatus__rosidl_typesupport_introspection_c__DroneStatus_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_drone_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, drone_interfaces, msg, DroneStatus)() {
  if (!drone_interfaces__msg__DroneStatus__rosidl_typesupport_introspection_c__DroneStatus_message_type_support_handle.typesupport_identifier) {
    drone_interfaces__msg__DroneStatus__rosidl_typesupport_introspection_c__DroneStatus_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &drone_interfaces__msg__DroneStatus__rosidl_typesupport_introspection_c__DroneStatus_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
