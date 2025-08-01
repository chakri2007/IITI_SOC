// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from drone_interfaces:srv/GetSeverityScore.idl
// generated code does not contain a copyright notice
#include "drone_interfaces/srv/detail/get_severity_score__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "drone_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "drone_interfaces/srv/detail/get_severity_score__struct.h"
#include "drone_interfaces/srv/detail/get_severity_score__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _GetSeverityScore_Request__ros_msg_type = drone_interfaces__srv__GetSeverityScore_Request;

static bool _GetSeverityScore_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _GetSeverityScore_Request__ros_msg_type * ros_message = static_cast<const _GetSeverityScore_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: id
  {
    cdr << ros_message->id;
  }

  return true;
}

static bool _GetSeverityScore_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _GetSeverityScore_Request__ros_msg_type * ros_message = static_cast<_GetSeverityScore_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: id
  {
    cdr >> ros_message->id;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_drone_interfaces
size_t get_serialized_size_drone_interfaces__srv__GetSeverityScore_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _GetSeverityScore_Request__ros_msg_type * ros_message = static_cast<const _GetSeverityScore_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name id
  {
    size_t item_size = sizeof(ros_message->id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _GetSeverityScore_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_drone_interfaces__srv__GetSeverityScore_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_drone_interfaces
size_t max_serialized_size_drone_interfaces__srv__GetSeverityScore_Request(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: id
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = drone_interfaces__srv__GetSeverityScore_Request;
    is_plain =
      (
      offsetof(DataType, id) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _GetSeverityScore_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_drone_interfaces__srv__GetSeverityScore_Request(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_GetSeverityScore_Request = {
  "drone_interfaces::srv",
  "GetSeverityScore_Request",
  _GetSeverityScore_Request__cdr_serialize,
  _GetSeverityScore_Request__cdr_deserialize,
  _GetSeverityScore_Request__get_serialized_size,
  _GetSeverityScore_Request__max_serialized_size
};

static rosidl_message_type_support_t _GetSeverityScore_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_GetSeverityScore_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, drone_interfaces, srv, GetSeverityScore_Request)() {
  return &_GetSeverityScore_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "drone_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "drone_interfaces/srv/detail/get_severity_score__struct.h"
// already included above
// #include "drone_interfaces/srv/detail/get_severity_score__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _GetSeverityScore_Response__ros_msg_type = drone_interfaces__srv__GetSeverityScore_Response;

static bool _GetSeverityScore_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _GetSeverityScore_Response__ros_msg_type * ros_message = static_cast<const _GetSeverityScore_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: severity_score
  {
    cdr << ros_message->severity_score;
  }

  return true;
}

static bool _GetSeverityScore_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _GetSeverityScore_Response__ros_msg_type * ros_message = static_cast<_GetSeverityScore_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: severity_score
  {
    cdr >> ros_message->severity_score;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_drone_interfaces
size_t get_serialized_size_drone_interfaces__srv__GetSeverityScore_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _GetSeverityScore_Response__ros_msg_type * ros_message = static_cast<const _GetSeverityScore_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name severity_score
  {
    size_t item_size = sizeof(ros_message->severity_score);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _GetSeverityScore_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_drone_interfaces__srv__GetSeverityScore_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_drone_interfaces
size_t max_serialized_size_drone_interfaces__srv__GetSeverityScore_Response(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: severity_score
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = drone_interfaces__srv__GetSeverityScore_Response;
    is_plain =
      (
      offsetof(DataType, severity_score) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _GetSeverityScore_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_drone_interfaces__srv__GetSeverityScore_Response(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_GetSeverityScore_Response = {
  "drone_interfaces::srv",
  "GetSeverityScore_Response",
  _GetSeverityScore_Response__cdr_serialize,
  _GetSeverityScore_Response__cdr_deserialize,
  _GetSeverityScore_Response__get_serialized_size,
  _GetSeverityScore_Response__max_serialized_size
};

static rosidl_message_type_support_t _GetSeverityScore_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_GetSeverityScore_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, drone_interfaces, srv, GetSeverityScore_Response)() {
  return &_GetSeverityScore_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "drone_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "drone_interfaces/srv/get_severity_score.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t GetSeverityScore__callbacks = {
  "drone_interfaces::srv",
  "GetSeverityScore",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, drone_interfaces, srv, GetSeverityScore_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, drone_interfaces, srv, GetSeverityScore_Response)(),
};

static rosidl_service_type_support_t GetSeverityScore__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &GetSeverityScore__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, drone_interfaces, srv, GetSeverityScore)() {
  return &GetSeverityScore__handle;
}

#if defined(__cplusplus)
}
#endif
