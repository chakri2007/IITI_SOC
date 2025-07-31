// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from drone_interfaces:msg/GeotagVisited.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__GEOTAG_VISITED__STRUCT_H_
#define DRONE_INTERFACES__MSG__DETAIL__GEOTAG_VISITED__STRUCT_H_

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
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/GeotagVisited in the package drone_interfaces.
typedef struct drone_interfaces__msg__GeotagVisited
{
  rosidl_runtime_c__String drone_id;
  int32_t geotag_id;
} drone_interfaces__msg__GeotagVisited;

// Struct for a sequence of drone_interfaces__msg__GeotagVisited.
typedef struct drone_interfaces__msg__GeotagVisited__Sequence
{
  drone_interfaces__msg__GeotagVisited * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} drone_interfaces__msg__GeotagVisited__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DRONE_INTERFACES__MSG__DETAIL__GEOTAG_VISITED__STRUCT_H_
