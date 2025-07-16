// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from drone_interfaces:msg/WaypointArray.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "drone_interfaces/msg/detail/waypoint_array__rosidl_typesupport_introspection_c.h"
#include "drone_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "drone_interfaces/msg/detail/waypoint_array__functions.h"
#include "drone_interfaces/msg/detail/waypoint_array__struct.h"


// Include directives for member types
// Member `waypoints`
#include "drone_interfaces/msg/waypoint.h"
// Member `waypoints`
#include "drone_interfaces/msg/detail/waypoint__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__WaypointArray_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  drone_interfaces__msg__WaypointArray__init(message_memory);
}

void drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__WaypointArray_fini_function(void * message_memory)
{
  drone_interfaces__msg__WaypointArray__fini(message_memory);
}

size_t drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__size_function__WaypointArray__waypoints(
  const void * untyped_member)
{
  const drone_interfaces__msg__Waypoint__Sequence * member =
    (const drone_interfaces__msg__Waypoint__Sequence *)(untyped_member);
  return member->size;
}

const void * drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__get_const_function__WaypointArray__waypoints(
  const void * untyped_member, size_t index)
{
  const drone_interfaces__msg__Waypoint__Sequence * member =
    (const drone_interfaces__msg__Waypoint__Sequence *)(untyped_member);
  return &member->data[index];
}

void * drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__get_function__WaypointArray__waypoints(
  void * untyped_member, size_t index)
{
  drone_interfaces__msg__Waypoint__Sequence * member =
    (drone_interfaces__msg__Waypoint__Sequence *)(untyped_member);
  return &member->data[index];
}

void drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__fetch_function__WaypointArray__waypoints(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const drone_interfaces__msg__Waypoint * item =
    ((const drone_interfaces__msg__Waypoint *)
    drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__get_const_function__WaypointArray__waypoints(untyped_member, index));
  drone_interfaces__msg__Waypoint * value =
    (drone_interfaces__msg__Waypoint *)(untyped_value);
  *value = *item;
}

void drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__assign_function__WaypointArray__waypoints(
  void * untyped_member, size_t index, const void * untyped_value)
{
  drone_interfaces__msg__Waypoint * item =
    ((drone_interfaces__msg__Waypoint *)
    drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__get_function__WaypointArray__waypoints(untyped_member, index));
  const drone_interfaces__msg__Waypoint * value =
    (const drone_interfaces__msg__Waypoint *)(untyped_value);
  *item = *value;
}

bool drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__resize_function__WaypointArray__waypoints(
  void * untyped_member, size_t size)
{
  drone_interfaces__msg__Waypoint__Sequence * member =
    (drone_interfaces__msg__Waypoint__Sequence *)(untyped_member);
  drone_interfaces__msg__Waypoint__Sequence__fini(member);
  return drone_interfaces__msg__Waypoint__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__WaypointArray_message_member_array[1] = {
  {
    "waypoints",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_interfaces__msg__WaypointArray, waypoints),  // bytes offset in struct
    NULL,  // default value
    drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__size_function__WaypointArray__waypoints,  // size() function pointer
    drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__get_const_function__WaypointArray__waypoints,  // get_const(index) function pointer
    drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__get_function__WaypointArray__waypoints,  // get(index) function pointer
    drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__fetch_function__WaypointArray__waypoints,  // fetch(index, &value) function pointer
    drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__assign_function__WaypointArray__waypoints,  // assign(index, value) function pointer
    drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__resize_function__WaypointArray__waypoints  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__WaypointArray_message_members = {
  "drone_interfaces__msg",  // message namespace
  "WaypointArray",  // message name
  1,  // number of fields
  sizeof(drone_interfaces__msg__WaypointArray),
  drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__WaypointArray_message_member_array,  // message members
  drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__WaypointArray_init_function,  // function to initialize message memory (memory has to be allocated)
  drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__WaypointArray_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__WaypointArray_message_type_support_handle = {
  0,
  &drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__WaypointArray_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_drone_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, drone_interfaces, msg, WaypointArray)() {
  drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__WaypointArray_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, drone_interfaces, msg, Waypoint)();
  if (!drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__WaypointArray_message_type_support_handle.typesupport_identifier) {
    drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__WaypointArray_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &drone_interfaces__msg__WaypointArray__rosidl_typesupport_introspection_c__WaypointArray_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
