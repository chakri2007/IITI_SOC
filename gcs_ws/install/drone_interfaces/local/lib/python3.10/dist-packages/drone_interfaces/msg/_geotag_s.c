// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from drone_interfaces:msg/Geotag.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "drone_interfaces/msg/detail/geotag__struct.h"
#include "drone_interfaces/msg/detail/geotag__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool drone_interfaces__msg__geotag__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[36];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("drone_interfaces.msg._geotag.Geotag", full_classname_dest, 35) == 0);
  }
  drone_interfaces__msg__Geotag * ros_message = _ros_message;
  {  // id
    PyObject * field = PyObject_GetAttrString(_pymsg, "id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->id = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // lat
    PyObject * field = PyObject_GetAttrString(_pymsg, "lat");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->lat = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // lon
    PyObject * field = PyObject_GetAttrString(_pymsg, "lon");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->lon = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // alt
    PyObject * field = PyObject_GetAttrString(_pymsg, "alt");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->alt = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // severity_score
    PyObject * field = PyObject_GetAttrString(_pymsg, "severity_score");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->severity_score = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * drone_interfaces__msg__geotag__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Geotag */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("drone_interfaces.msg._geotag");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Geotag");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  drone_interfaces__msg__Geotag * ros_message = (drone_interfaces__msg__Geotag *)raw_ros_message;
  {  // id
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // lat
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->lat);
    {
      int rc = PyObject_SetAttrString(_pymessage, "lat", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // lon
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->lon);
    {
      int rc = PyObject_SetAttrString(_pymessage, "lon", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // alt
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->alt);
    {
      int rc = PyObject_SetAttrString(_pymessage, "alt", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // severity_score
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->severity_score);
    {
      int rc = PyObject_SetAttrString(_pymessage, "severity_score", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
