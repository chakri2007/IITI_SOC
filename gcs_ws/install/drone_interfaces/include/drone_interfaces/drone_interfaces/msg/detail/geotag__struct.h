// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from drone_interfaces:msg/Geotag.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__GEOTAG__STRUCT_H_
#define DRONE_INTERFACES__MSG__DETAIL__GEOTAG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/Geotag in the package drone_interfaces.
typedef struct drone_interfaces__msg__Geotag
{
  uint32_t id;
  double lat;
  double lon;
  double alt;
  uint8_t severity_score;
} drone_interfaces__msg__Geotag;

// Struct for a sequence of drone_interfaces__msg__Geotag.
typedef struct drone_interfaces__msg__Geotag__Sequence
{
  drone_interfaces__msg__Geotag * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} drone_interfaces__msg__Geotag__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DRONE_INTERFACES__MSG__DETAIL__GEOTAG__STRUCT_H_
