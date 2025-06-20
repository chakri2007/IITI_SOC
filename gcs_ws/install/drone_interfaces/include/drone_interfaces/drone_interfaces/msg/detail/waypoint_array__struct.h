// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from drone_interfaces:msg/WaypointArray.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_ARRAY__STRUCT_H_
#define DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_ARRAY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'waypoints'
#include "drone_interfaces/msg/detail/waypoint__struct.h"

/// Struct defined in msg/WaypointArray in the package drone_interfaces.
typedef struct drone_interfaces__msg__WaypointArray
{
  drone_interfaces__msg__Waypoint__Sequence waypoints;
} drone_interfaces__msg__WaypointArray;

// Struct for a sequence of drone_interfaces__msg__WaypointArray.
typedef struct drone_interfaces__msg__WaypointArray__Sequence
{
  drone_interfaces__msg__WaypointArray * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} drone_interfaces__msg__WaypointArray__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_ARRAY__STRUCT_H_
