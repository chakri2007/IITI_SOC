// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from drone_interfaces:msg/GeotagArray.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "drone_interfaces/msg/detail/geotag_array__rosidl_typesupport_introspection_c.h"
#include "drone_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "drone_interfaces/msg/detail/geotag_array__functions.h"
#include "drone_interfaces/msg/detail/geotag_array__struct.h"


// Include directives for member types
// Member `geotags`
#include "drone_interfaces/msg/geotag.h"
// Member `geotags`
#include "drone_interfaces/msg/detail/geotag__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__GeotagArray_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  drone_interfaces__msg__GeotagArray__init(message_memory);
}

void drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__GeotagArray_fini_function(void * message_memory)
{
  drone_interfaces__msg__GeotagArray__fini(message_memory);
}

size_t drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__size_function__GeotagArray__geotags(
  const void * untyped_member)
{
  const drone_interfaces__msg__Geotag__Sequence * member =
    (const drone_interfaces__msg__Geotag__Sequence *)(untyped_member);
  return member->size;
}

const void * drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__get_const_function__GeotagArray__geotags(
  const void * untyped_member, size_t index)
{
  const drone_interfaces__msg__Geotag__Sequence * member =
    (const drone_interfaces__msg__Geotag__Sequence *)(untyped_member);
  return &member->data[index];
}

void * drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__get_function__GeotagArray__geotags(
  void * untyped_member, size_t index)
{
  drone_interfaces__msg__Geotag__Sequence * member =
    (drone_interfaces__msg__Geotag__Sequence *)(untyped_member);
  return &member->data[index];
}

void drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__fetch_function__GeotagArray__geotags(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const drone_interfaces__msg__Geotag * item =
    ((const drone_interfaces__msg__Geotag *)
    drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__get_const_function__GeotagArray__geotags(untyped_member, index));
  drone_interfaces__msg__Geotag * value =
    (drone_interfaces__msg__Geotag *)(untyped_value);
  *value = *item;
}

void drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__assign_function__GeotagArray__geotags(
  void * untyped_member, size_t index, const void * untyped_value)
{
  drone_interfaces__msg__Geotag * item =
    ((drone_interfaces__msg__Geotag *)
    drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__get_function__GeotagArray__geotags(untyped_member, index));
  const drone_interfaces__msg__Geotag * value =
    (const drone_interfaces__msg__Geotag *)(untyped_value);
  *item = *value;
}

bool drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__resize_function__GeotagArray__geotags(
  void * untyped_member, size_t size)
{
  drone_interfaces__msg__Geotag__Sequence * member =
    (drone_interfaces__msg__Geotag__Sequence *)(untyped_member);
  drone_interfaces__msg__Geotag__Sequence__fini(member);
  return drone_interfaces__msg__Geotag__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__GeotagArray_message_member_array[1] = {
  {
    "geotags",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(drone_interfaces__msg__GeotagArray, geotags),  // bytes offset in struct
    NULL,  // default value
    drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__size_function__GeotagArray__geotags,  // size() function pointer
    drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__get_const_function__GeotagArray__geotags,  // get_const(index) function pointer
    drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__get_function__GeotagArray__geotags,  // get(index) function pointer
    drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__fetch_function__GeotagArray__geotags,  // fetch(index, &value) function pointer
    drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__assign_function__GeotagArray__geotags,  // assign(index, value) function pointer
    drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__resize_function__GeotagArray__geotags  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__GeotagArray_message_members = {
  "drone_interfaces__msg",  // message namespace
  "GeotagArray",  // message name
  1,  // number of fields
  sizeof(drone_interfaces__msg__GeotagArray),
  drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__GeotagArray_message_member_array,  // message members
  drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__GeotagArray_init_function,  // function to initialize message memory (memory has to be allocated)
  drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__GeotagArray_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__GeotagArray_message_type_support_handle = {
  0,
  &drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__GeotagArray_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_drone_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, drone_interfaces, msg, GeotagArray)() {
  drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__GeotagArray_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, drone_interfaces, msg, Geotag)();
  if (!drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__GeotagArray_message_type_support_handle.typesupport_identifier) {
    drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__GeotagArray_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &drone_interfaces__msg__GeotagArray__rosidl_typesupport_introspection_c__GeotagArray_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
