// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from drone_interfaces:msg/GeotagRequest.idl
// generated code does not contain a copyright notice
#include "drone_interfaces/msg/detail/geotag_request__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `drone_id`
// Member `direction`
#include "rosidl_runtime_c/string_functions.h"

bool
drone_interfaces__msg__GeotagRequest__init(drone_interfaces__msg__GeotagRequest * msg)
{
  if (!msg) {
    return false;
  }
  // drone_id
  if (!rosidl_runtime_c__String__init(&msg->drone_id)) {
    drone_interfaces__msg__GeotagRequest__fini(msg);
    return false;
  }
  // direction
  if (!rosidl_runtime_c__String__init(&msg->direction)) {
    drone_interfaces__msg__GeotagRequest__fini(msg);
    return false;
  }
  return true;
}

void
drone_interfaces__msg__GeotagRequest__fini(drone_interfaces__msg__GeotagRequest * msg)
{
  if (!msg) {
    return;
  }
  // drone_id
  rosidl_runtime_c__String__fini(&msg->drone_id);
  // direction
  rosidl_runtime_c__String__fini(&msg->direction);
}

bool
drone_interfaces__msg__GeotagRequest__are_equal(const drone_interfaces__msg__GeotagRequest * lhs, const drone_interfaces__msg__GeotagRequest * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // drone_id
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->drone_id), &(rhs->drone_id)))
  {
    return false;
  }
  // direction
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->direction), &(rhs->direction)))
  {
    return false;
  }
  return true;
}

bool
drone_interfaces__msg__GeotagRequest__copy(
  const drone_interfaces__msg__GeotagRequest * input,
  drone_interfaces__msg__GeotagRequest * output)
{
  if (!input || !output) {
    return false;
  }
  // drone_id
  if (!rosidl_runtime_c__String__copy(
      &(input->drone_id), &(output->drone_id)))
  {
    return false;
  }
  // direction
  if (!rosidl_runtime_c__String__copy(
      &(input->direction), &(output->direction)))
  {
    return false;
  }
  return true;
}

drone_interfaces__msg__GeotagRequest *
drone_interfaces__msg__GeotagRequest__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drone_interfaces__msg__GeotagRequest * msg = (drone_interfaces__msg__GeotagRequest *)allocator.allocate(sizeof(drone_interfaces__msg__GeotagRequest), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(drone_interfaces__msg__GeotagRequest));
  bool success = drone_interfaces__msg__GeotagRequest__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
drone_interfaces__msg__GeotagRequest__destroy(drone_interfaces__msg__GeotagRequest * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    drone_interfaces__msg__GeotagRequest__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
drone_interfaces__msg__GeotagRequest__Sequence__init(drone_interfaces__msg__GeotagRequest__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drone_interfaces__msg__GeotagRequest * data = NULL;

  if (size) {
    data = (drone_interfaces__msg__GeotagRequest *)allocator.zero_allocate(size, sizeof(drone_interfaces__msg__GeotagRequest), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = drone_interfaces__msg__GeotagRequest__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        drone_interfaces__msg__GeotagRequest__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
drone_interfaces__msg__GeotagRequest__Sequence__fini(drone_interfaces__msg__GeotagRequest__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      drone_interfaces__msg__GeotagRequest__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

drone_interfaces__msg__GeotagRequest__Sequence *
drone_interfaces__msg__GeotagRequest__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drone_interfaces__msg__GeotagRequest__Sequence * array = (drone_interfaces__msg__GeotagRequest__Sequence *)allocator.allocate(sizeof(drone_interfaces__msg__GeotagRequest__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = drone_interfaces__msg__GeotagRequest__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
drone_interfaces__msg__GeotagRequest__Sequence__destroy(drone_interfaces__msg__GeotagRequest__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    drone_interfaces__msg__GeotagRequest__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
drone_interfaces__msg__GeotagRequest__Sequence__are_equal(const drone_interfaces__msg__GeotagRequest__Sequence * lhs, const drone_interfaces__msg__GeotagRequest__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!drone_interfaces__msg__GeotagRequest__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
drone_interfaces__msg__GeotagRequest__Sequence__copy(
  const drone_interfaces__msg__GeotagRequest__Sequence * input,
  drone_interfaces__msg__GeotagRequest__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(drone_interfaces__msg__GeotagRequest);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    drone_interfaces__msg__GeotagRequest * data =
      (drone_interfaces__msg__GeotagRequest *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!drone_interfaces__msg__GeotagRequest__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          drone_interfaces__msg__GeotagRequest__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!drone_interfaces__msg__GeotagRequest__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
