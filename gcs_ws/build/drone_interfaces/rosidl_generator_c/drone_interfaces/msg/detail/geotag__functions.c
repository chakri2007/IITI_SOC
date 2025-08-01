// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from drone_interfaces:msg/Geotag.idl
// generated code does not contain a copyright notice
#include "drone_interfaces/msg/detail/geotag__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
drone_interfaces__msg__Geotag__init(drone_interfaces__msg__Geotag * msg)
{
  if (!msg) {
    return false;
  }
  // id
  // lat
  // lon
  // alt
  // severity_score
  return true;
}

void
drone_interfaces__msg__Geotag__fini(drone_interfaces__msg__Geotag * msg)
{
  if (!msg) {
    return;
  }
  // id
  // lat
  // lon
  // alt
  // severity_score
}

bool
drone_interfaces__msg__Geotag__are_equal(const drone_interfaces__msg__Geotag * lhs, const drone_interfaces__msg__Geotag * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // id
  if (lhs->id != rhs->id) {
    return false;
  }
  // lat
  if (lhs->lat != rhs->lat) {
    return false;
  }
  // lon
  if (lhs->lon != rhs->lon) {
    return false;
  }
  // alt
  if (lhs->alt != rhs->alt) {
    return false;
  }
  // severity_score
  if (lhs->severity_score != rhs->severity_score) {
    return false;
  }
  return true;
}

bool
drone_interfaces__msg__Geotag__copy(
  const drone_interfaces__msg__Geotag * input,
  drone_interfaces__msg__Geotag * output)
{
  if (!input || !output) {
    return false;
  }
  // id
  output->id = input->id;
  // lat
  output->lat = input->lat;
  // lon
  output->lon = input->lon;
  // alt
  output->alt = input->alt;
  // severity_score
  output->severity_score = input->severity_score;
  return true;
}

drone_interfaces__msg__Geotag *
drone_interfaces__msg__Geotag__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drone_interfaces__msg__Geotag * msg = (drone_interfaces__msg__Geotag *)allocator.allocate(sizeof(drone_interfaces__msg__Geotag), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(drone_interfaces__msg__Geotag));
  bool success = drone_interfaces__msg__Geotag__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
drone_interfaces__msg__Geotag__destroy(drone_interfaces__msg__Geotag * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    drone_interfaces__msg__Geotag__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
drone_interfaces__msg__Geotag__Sequence__init(drone_interfaces__msg__Geotag__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drone_interfaces__msg__Geotag * data = NULL;

  if (size) {
    data = (drone_interfaces__msg__Geotag *)allocator.zero_allocate(size, sizeof(drone_interfaces__msg__Geotag), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = drone_interfaces__msg__Geotag__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        drone_interfaces__msg__Geotag__fini(&data[i - 1]);
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
drone_interfaces__msg__Geotag__Sequence__fini(drone_interfaces__msg__Geotag__Sequence * array)
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
      drone_interfaces__msg__Geotag__fini(&array->data[i]);
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

drone_interfaces__msg__Geotag__Sequence *
drone_interfaces__msg__Geotag__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drone_interfaces__msg__Geotag__Sequence * array = (drone_interfaces__msg__Geotag__Sequence *)allocator.allocate(sizeof(drone_interfaces__msg__Geotag__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = drone_interfaces__msg__Geotag__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
drone_interfaces__msg__Geotag__Sequence__destroy(drone_interfaces__msg__Geotag__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    drone_interfaces__msg__Geotag__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
drone_interfaces__msg__Geotag__Sequence__are_equal(const drone_interfaces__msg__Geotag__Sequence * lhs, const drone_interfaces__msg__Geotag__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!drone_interfaces__msg__Geotag__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
drone_interfaces__msg__Geotag__Sequence__copy(
  const drone_interfaces__msg__Geotag__Sequence * input,
  drone_interfaces__msg__Geotag__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(drone_interfaces__msg__Geotag);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    drone_interfaces__msg__Geotag * data =
      (drone_interfaces__msg__Geotag *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!drone_interfaces__msg__Geotag__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          drone_interfaces__msg__Geotag__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!drone_interfaces__msg__Geotag__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
