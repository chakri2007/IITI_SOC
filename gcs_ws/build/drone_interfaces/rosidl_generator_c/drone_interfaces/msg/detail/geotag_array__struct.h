// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from drone_interfaces:msg/GeotagArray.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__GEOTAG_ARRAY__STRUCT_H_
#define DRONE_INTERFACES__MSG__DETAIL__GEOTAG_ARRAY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'geotags'
#include "drone_interfaces/msg/detail/geotag__struct.h"

/// Struct defined in msg/GeotagArray in the package drone_interfaces.
typedef struct drone_interfaces__msg__GeotagArray
{
  drone_interfaces__msg__Geotag__Sequence geotags;
} drone_interfaces__msg__GeotagArray;

// Struct for a sequence of drone_interfaces__msg__GeotagArray.
typedef struct drone_interfaces__msg__GeotagArray__Sequence
{
  drone_interfaces__msg__GeotagArray * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} drone_interfaces__msg__GeotagArray__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DRONE_INTERFACES__MSG__DETAIL__GEOTAG_ARRAY__STRUCT_H_
