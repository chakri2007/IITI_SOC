// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from drone_interfaces:srv/GetSeverityScore.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__SRV__DETAIL__GET_SEVERITY_SCORE__STRUCT_H_
#define DRONE_INTERFACES__SRV__DETAIL__GET_SEVERITY_SCORE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/GetSeverityScore in the package drone_interfaces.
typedef struct drone_interfaces__srv__GetSeverityScore_Request
{
  uint32_t id;
} drone_interfaces__srv__GetSeverityScore_Request;

// Struct for a sequence of drone_interfaces__srv__GetSeverityScore_Request.
typedef struct drone_interfaces__srv__GetSeverityScore_Request__Sequence
{
  drone_interfaces__srv__GetSeverityScore_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} drone_interfaces__srv__GetSeverityScore_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/GetSeverityScore in the package drone_interfaces.
typedef struct drone_interfaces__srv__GetSeverityScore_Response
{
  uint8_t severity_score;
} drone_interfaces__srv__GetSeverityScore_Response;

// Struct for a sequence of drone_interfaces__srv__GetSeverityScore_Response.
typedef struct drone_interfaces__srv__GetSeverityScore_Response__Sequence
{
  drone_interfaces__srv__GetSeverityScore_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} drone_interfaces__srv__GetSeverityScore_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DRONE_INTERFACES__SRV__DETAIL__GET_SEVERITY_SCORE__STRUCT_H_
