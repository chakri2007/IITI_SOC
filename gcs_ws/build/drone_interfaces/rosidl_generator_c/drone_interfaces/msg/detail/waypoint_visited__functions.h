// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from drone_interfaces:msg/WaypointVisited.idl
// generated code does not contain a copyright notice

#ifndef DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_VISITED__FUNCTIONS_H_
#define DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_VISITED__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "drone_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "drone_interfaces/msg/detail/waypoint_visited__struct.h"

/// Initialize msg/WaypointVisited message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * drone_interfaces__msg__WaypointVisited
 * )) before or use
 * drone_interfaces__msg__WaypointVisited__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_interfaces
bool
drone_interfaces__msg__WaypointVisited__init(drone_interfaces__msg__WaypointVisited * msg);

/// Finalize msg/WaypointVisited message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_interfaces
void
drone_interfaces__msg__WaypointVisited__fini(drone_interfaces__msg__WaypointVisited * msg);

/// Create msg/WaypointVisited message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * drone_interfaces__msg__WaypointVisited__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_interfaces
drone_interfaces__msg__WaypointVisited *
drone_interfaces__msg__WaypointVisited__create();

/// Destroy msg/WaypointVisited message.
/**
 * It calls
 * drone_interfaces__msg__WaypointVisited__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_interfaces
void
drone_interfaces__msg__WaypointVisited__destroy(drone_interfaces__msg__WaypointVisited * msg);

/// Check for msg/WaypointVisited message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_interfaces
bool
drone_interfaces__msg__WaypointVisited__are_equal(const drone_interfaces__msg__WaypointVisited * lhs, const drone_interfaces__msg__WaypointVisited * rhs);

/// Copy a msg/WaypointVisited message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_interfaces
bool
drone_interfaces__msg__WaypointVisited__copy(
  const drone_interfaces__msg__WaypointVisited * input,
  drone_interfaces__msg__WaypointVisited * output);

/// Initialize array of msg/WaypointVisited messages.
/**
 * It allocates the memory for the number of elements and calls
 * drone_interfaces__msg__WaypointVisited__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_interfaces
bool
drone_interfaces__msg__WaypointVisited__Sequence__init(drone_interfaces__msg__WaypointVisited__Sequence * array, size_t size);

/// Finalize array of msg/WaypointVisited messages.
/**
 * It calls
 * drone_interfaces__msg__WaypointVisited__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_interfaces
void
drone_interfaces__msg__WaypointVisited__Sequence__fini(drone_interfaces__msg__WaypointVisited__Sequence * array);

/// Create array of msg/WaypointVisited messages.
/**
 * It allocates the memory for the array and calls
 * drone_interfaces__msg__WaypointVisited__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_interfaces
drone_interfaces__msg__WaypointVisited__Sequence *
drone_interfaces__msg__WaypointVisited__Sequence__create(size_t size);

/// Destroy array of msg/WaypointVisited messages.
/**
 * It calls
 * drone_interfaces__msg__WaypointVisited__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_interfaces
void
drone_interfaces__msg__WaypointVisited__Sequence__destroy(drone_interfaces__msg__WaypointVisited__Sequence * array);

/// Check for msg/WaypointVisited message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_interfaces
bool
drone_interfaces__msg__WaypointVisited__Sequence__are_equal(const drone_interfaces__msg__WaypointVisited__Sequence * lhs, const drone_interfaces__msg__WaypointVisited__Sequence * rhs);

/// Copy an array of msg/WaypointVisited messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_drone_interfaces
bool
drone_interfaces__msg__WaypointVisited__Sequence__copy(
  const drone_interfaces__msg__WaypointVisited__Sequence * input,
  drone_interfaces__msg__WaypointVisited__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // DRONE_INTERFACES__MSG__DETAIL__WAYPOINT_VISITED__FUNCTIONS_H_
