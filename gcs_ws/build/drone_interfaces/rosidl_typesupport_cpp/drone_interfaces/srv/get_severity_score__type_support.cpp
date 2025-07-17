// generated from rosidl_typesupport_cpp/resource/idl__type_support.cpp.em
// with input from drone_interfaces:srv/GetSeverityScore.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "drone_interfaces/srv/detail/get_severity_score__struct.hpp"
#include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
#include "rosidl_typesupport_cpp/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace drone_interfaces
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _GetSeverityScore_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _GetSeverityScore_Request_type_support_ids_t;

static const _GetSeverityScore_Request_type_support_ids_t _GetSeverityScore_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _GetSeverityScore_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _GetSeverityScore_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _GetSeverityScore_Request_type_support_symbol_names_t _GetSeverityScore_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, drone_interfaces, srv, GetSeverityScore_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, drone_interfaces, srv, GetSeverityScore_Request)),
  }
};

typedef struct _GetSeverityScore_Request_type_support_data_t
{
  void * data[2];
} _GetSeverityScore_Request_type_support_data_t;

static _GetSeverityScore_Request_type_support_data_t _GetSeverityScore_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _GetSeverityScore_Request_message_typesupport_map = {
  2,
  "drone_interfaces",
  &_GetSeverityScore_Request_message_typesupport_ids.typesupport_identifier[0],
  &_GetSeverityScore_Request_message_typesupport_symbol_names.symbol_name[0],
  &_GetSeverityScore_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t GetSeverityScore_Request_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_GetSeverityScore_Request_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace drone_interfaces

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<drone_interfaces::srv::GetSeverityScore_Request>()
{
  return &::drone_interfaces::srv::rosidl_typesupport_cpp::GetSeverityScore_Request_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, drone_interfaces, srv, GetSeverityScore_Request)() {
  return get_message_type_support_handle<drone_interfaces::srv::GetSeverityScore_Request>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "drone_interfaces/srv/detail/get_severity_score__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace drone_interfaces
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _GetSeverityScore_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _GetSeverityScore_Response_type_support_ids_t;

static const _GetSeverityScore_Response_type_support_ids_t _GetSeverityScore_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _GetSeverityScore_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _GetSeverityScore_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _GetSeverityScore_Response_type_support_symbol_names_t _GetSeverityScore_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, drone_interfaces, srv, GetSeverityScore_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, drone_interfaces, srv, GetSeverityScore_Response)),
  }
};

typedef struct _GetSeverityScore_Response_type_support_data_t
{
  void * data[2];
} _GetSeverityScore_Response_type_support_data_t;

static _GetSeverityScore_Response_type_support_data_t _GetSeverityScore_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _GetSeverityScore_Response_message_typesupport_map = {
  2,
  "drone_interfaces",
  &_GetSeverityScore_Response_message_typesupport_ids.typesupport_identifier[0],
  &_GetSeverityScore_Response_message_typesupport_symbol_names.symbol_name[0],
  &_GetSeverityScore_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t GetSeverityScore_Response_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_GetSeverityScore_Response_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace drone_interfaces

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<drone_interfaces::srv::GetSeverityScore_Response>()
{
  return &::drone_interfaces::srv::rosidl_typesupport_cpp::GetSeverityScore_Response_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, drone_interfaces, srv, GetSeverityScore_Response)() {
  return get_message_type_support_handle<drone_interfaces::srv::GetSeverityScore_Response>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "drone_interfaces/srv/detail/get_severity_score__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/service_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace drone_interfaces
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _GetSeverityScore_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _GetSeverityScore_type_support_ids_t;

static const _GetSeverityScore_type_support_ids_t _GetSeverityScore_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _GetSeverityScore_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _GetSeverityScore_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _GetSeverityScore_type_support_symbol_names_t _GetSeverityScore_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, drone_interfaces, srv, GetSeverityScore)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, drone_interfaces, srv, GetSeverityScore)),
  }
};

typedef struct _GetSeverityScore_type_support_data_t
{
  void * data[2];
} _GetSeverityScore_type_support_data_t;

static _GetSeverityScore_type_support_data_t _GetSeverityScore_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _GetSeverityScore_service_typesupport_map = {
  2,
  "drone_interfaces",
  &_GetSeverityScore_service_typesupport_ids.typesupport_identifier[0],
  &_GetSeverityScore_service_typesupport_symbol_names.symbol_name[0],
  &_GetSeverityScore_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t GetSeverityScore_service_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_GetSeverityScore_service_typesupport_map),
  ::rosidl_typesupport_cpp::get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace drone_interfaces

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<drone_interfaces::srv::GetSeverityScore>()
{
  return &::drone_interfaces::srv::rosidl_typesupport_cpp::GetSeverityScore_service_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_cpp, drone_interfaces, srv, GetSeverityScore)() {
  return ::rosidl_typesupport_cpp::get_service_type_support_handle<drone_interfaces::srv::GetSeverityScore>();
}

#ifdef __cplusplus
}
#endif
