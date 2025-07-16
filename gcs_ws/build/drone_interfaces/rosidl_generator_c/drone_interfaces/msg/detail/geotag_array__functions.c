// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from drone_interfaces:msg/GeotagArray.idl
// generated code does not contain a copyright notice
#include "drone_interfaces/msg/detail/geotag_array__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `geotags`
#include "drone_interfaces/msg/detail/geotag__functions.h"

bool
drone_interfaces__msg__GeotagArray__init(drone_interfaces__msg__GeotagArray * msg)
{
  if (!msg) {
    return false;
  }
  // geotags
  if (!drone_interfaces__msg__Geotag__Sequence__init(&msg->geotags, 0)) {
    drone_interfaces__msg__GeotagArray__fini(msg);
    return false;
  }
  return true;
}

void
drone_interfaces__msg__GeotagArray__fini(drone_interfaces__msg__GeotagArray * msg)
{
  if (!msg) {
    return;
  }
  // geotags
  drone_interfaces__msg__Geotag__Sequence__fini(&msg->geotags);
}

bool
drone_interfaces__msg__GeotagArray__are_equal(const drone_interfaces__msg__GeotagArray * lhs, const drone_interfaces__msg__GeotagArray * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // geotags
  if (!drone_interfaces__msg__Geotag__Sequence__are_equal(
      &(lhs->geotags), &(rhs->geotags)))
  {
    return false;
  }
  return true;
}

bool
drone_interfaces__msg__GeotagArray__copy(
  const drone_interfaces__msg__GeotagArray * input,
  drone_interfaces__msg__GeotagArray * output)
{
  if (!input || !output) {
    return false;
  }
  // geotags
  if (!drone_interfaces__msg__Geotag__Sequence__copy(
      &(input->geotags), &(output->geotags)))
  {
    return false;
  }
  return true;
}

drone_interfaces__msg__GeotagArray *
drone_interfaces__msg__GeotagArray__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drone_interfaces__msg__GeotagArray * msg = (drone_interfaces__msg__GeotagArray *)allocator.allocate(sizeof(drone_interfaces__msg__GeotagArray), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(drone_interfaces__msg__GeotagArray));
  bool success = drone_interfaces__msg__GeotagArray__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
drone_interfaces__msg__GeotagArray__destroy(drone_interfaces__msg__GeotagArray * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    drone_interfaces__msg__GeotagArray__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
drone_interfaces__msg__GeotagArray__Sequence__init(drone_interfaces__msg__GeotagArray__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drone_interfaces__msg__GeotagArray * data = NULL;

  if (size) {
    data = (drone_interfaces__msg__GeotagArray *)allocator.zero_allocate(size, sizeof(drone_interfaces__msg__GeotagArray), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = drone_interfaces__msg__GeotagArray__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        drone_interfaces__msg__GeotagArray__fini(&data[i - 1]);
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
drone_interfaces__msg__GeotagArray__Sequence__fini(drone_interfaces__msg__GeotagArray__Sequence * array)
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
      drone_interfaces__msg__GeotagArray__fini(&array->data[i]);
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

drone_interfaces__msg__GeotagArray__Sequence *
drone_interfaces__msg__GeotagArray__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  drone_interfaces__msg__GeotagArray__Sequence * array = (drone_interfaces__msg__GeotagArray__Sequence *)allocator.allocate(sizeof(drone_interfaces__msg__GeotagArray__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = drone_interfaces__msg__GeotagArray__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
drone_interfaces__msg__GeotagArray__Sequence__destroy(drone_interfaces__msg__GeotagArray__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    drone_interfaces__msg__GeotagArray__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
drone_interfaces__msg__GeotagArray__Sequence__are_equal(const drone_interfaces__msg__GeotagArray__Sequence * lhs, const drone_interfaces__msg__GeotagArray__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!drone_interfaces__msg__GeotagArray__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
drone_interfaces__msg__GeotagArray__Sequence__copy(
  const drone_interfaces__msg__GeotagArray__Sequence * input,
  drone_interfaces__msg__GeotagArray__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(drone_interfaces__msg__GeotagArray);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    drone_interfaces__msg__GeotagArray * data =
      (drone_interfaces__msg__GeotagArray *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!drone_interfaces__msg__GeotagArray__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          drone_interfaces__msg__GeotagArray__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!drone_interfaces__msg__GeotagArray__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
