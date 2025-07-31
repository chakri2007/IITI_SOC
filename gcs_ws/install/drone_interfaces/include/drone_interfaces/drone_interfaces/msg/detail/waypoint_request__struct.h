// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from drone_interfaces:msg/WaypointRequest.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_REQUEST__STRUCT_H_
#define DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_REQUEST__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'drone_id'
// Member 'direction'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/WaypointRequest in the package drone_interfaces.
typedef struct drone_interfaces__msg__WaypointRequest
{
  rosidl_runtime_c__String drone_id;
  rosidl_runtime_c__String direction;
} drone_interfaces__msg__WaypointRequest;

// Struct for a sequence of drone_interfaces__msg__WaypointRequest.
typedef struct drone_interfaces__msg__WaypointRequest__Sequence
{
  drone_interfaces__msg__WaypointRequest * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} drone_interfaces__msg__WaypointRequest__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_REQUEST__STRUCT_H_
