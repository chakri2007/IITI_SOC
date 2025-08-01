// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from drone_interfaces:msg/SurveillanceStatus.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__SURVEILLANCE_STATUS__STRUCT_H_
#define DRONE_INTERFACES__MSG__DETAIL__SURVEILLANCE_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/SurveillanceStatus in the package drone_interfaces.
typedef struct drone_interfaces__msg__SurveillanceStatus
{
  bool surveillance_completed;
  int32_t waypoints_remaining;
} drone_interfaces__msg__SurveillanceStatus;

// Struct for a sequence of drone_interfaces__msg__SurveillanceStatus.
typedef struct drone_interfaces__msg__SurveillanceStatus__Sequence
{
  drone_interfaces__msg__SurveillanceStatus * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} drone_interfaces__msg__SurveillanceStatus__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DRONE_INTERFACES__MSG__DETAIL__SURVEILLANCE_STATUS__STRUCT_H_
