// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from drone_interfaces:msg/DroneTypeChange.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__DRONE_TYPE_CHANGE__STRUCT_H_
#define DRONE_INTERFACES__MSG__DETAIL__DRONE_TYPE_CHANGE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'new_drone_type'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/DroneTypeChange in the package drone_interfaces.
typedef struct drone_interfaces__msg__DroneTypeChange
{
  rosidl_runtime_c__String new_drone_type;
} drone_interfaces__msg__DroneTypeChange;

// Struct for a sequence of drone_interfaces__msg__DroneTypeChange.
typedef struct drone_interfaces__msg__DroneTypeChange__Sequence
{
  drone_interfaces__msg__DroneTypeChange * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} drone_interfaces__msg__DroneTypeChange__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DRONE_INTERFACES__MSG__DETAIL__DRONE_TYPE_CHANGE__STRUCT_H_
