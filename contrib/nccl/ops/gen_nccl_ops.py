"""Python wrappers around TensorFlow ops.

This file is MACHINE GENERATED! Do not edit.
Original C++ source file: nccl_ops.cc
"""

import collections as _collections

from tensorflow.python.eager import execute as _execute
from tensorflow.python.eager import context as _context
from tensorflow.python.eager import core as _core
from tensorflow.python.framework import dtypes as _dtypes
from tensorflow.python.framework import tensor_shape as _tensor_shape

from tensorflow.core.framework import op_def_pb2 as _op_def_pb2
# Needed to trigger the call to _set_call_cpp_shape_fn.
from tensorflow.python.framework import common_shapes as _common_shapes
from tensorflow.python.framework import op_def_registry as _op_def_registry
from tensorflow.python.framework import ops as _ops
from tensorflow.python.framework import op_def_library as _op_def_library
from tensorflow.python.util.tf_export import tf_export


@tf_export('nccl_all_reduce')
def nccl_all_reduce(input, reduction, num_devices, shared_name, name=None):
  r"""Outputs a tensor containing the reduction across all input tensors passed to ops

  within the same `shared_name.

  The graph should be constructed so if one op runs with shared_name value `c`,
  then `num_devices` ops will run with shared_name value `c`.  Failure to do so
  will cause the graph execution to fail to complete.

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `int64`.
      the input to the reduction
    reduction: A `string` from: `"min", "max", "prod", "sum"`.
      the reduction operation to perform.
    num_devices: An `int`.
      The number of devices participating in this reduction.
    shared_name: A `string`.
      Identifier that shared between ops of the same reduction.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
    the value of the reduction across all `num_devices` devices.
  """
  reduction = _execute.make_str(reduction, "reduction")
  num_devices = _execute.make_int(num_devices, "num_devices")
  shared_name = _execute.make_str(shared_name, "shared_name")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "NcclAllReduce", input=input, reduction=reduction,
        num_devices=num_devices, shared_name=shared_name, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("reduction", _op.get_attr("reduction"), "T", _op.get_attr("T"),
              "num_devices", _op.get_attr("num_devices"), "shared_name",
              _op.get_attr("shared_name"))
  else:
    _attr_T, (input,) = _execute.args_to_matching_eager([input], _ctx)
    _inputs_flat = [input]
    _attrs = ("reduction", reduction, "T", _attr_T, "num_devices",
              num_devices, "shared_name", shared_name)
    _result = _execute.execute(b"NcclAllReduce", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "NcclAllReduce", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("NcclAllReduce")(None)


@tf_export('nccl_broadcast')
def nccl_broadcast(input, shape, name=None):
  r"""Sends `input` to all devices that are connected to the output.

  The graph should be constructed so that all ops connected to the output have a
  valid device assignment, and the op itself is assigned one of these devices.

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `int64`.
      The input to the broadcast.
    shape: A `tf.TensorShape` or list of `ints`.
      The shape of the input tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`. The same as input.
  """
  shape = _execute.make_shape(shape, "shape")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "NcclBroadcast", input=input, shape=shape, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "shape", _op.get_attr("shape"))
  else:
    _attr_T, (input,) = _execute.args_to_matching_eager([input], _ctx)
    _inputs_flat = [input]
    _attrs = ("T", _attr_T, "shape", shape)
    _result = _execute.execute(b"NcclBroadcast", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "NcclBroadcast", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("NcclBroadcast")(None)


@tf_export('nccl_reduce')
def nccl_reduce(input, reduction, name=None):
  r"""Reduces `input` from `num_devices` using `reduction` to a single device.

  The graph should be constructed so that all inputs have a valid device
  assignment, and the op itself is assigned one of these devices.

  Args:
    input: A list of at least 1 `Tensor` objects with the same type in: `float32`, `float64`, `int32`, `int64`.
      The input to the reduction.
    reduction: A `string` from: `"min", "max", "prod", "sum"`.
      the reduction operation to perform.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
    the value of the reduction across all `num_devices` devices.
  """
  if not isinstance(input, (list, tuple)):
    raise TypeError(
        "Expected list for 'input' argument to "
        "'nccl_reduce' Op, not %r." % input)
  _attr_num_devices = len(input)
  reduction = _execute.make_str(reduction, "reduction")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "NcclReduce", input=input, reduction=reduction, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("reduction", _op.get_attr("reduction"), "T", _op.get_attr("T"),
              "num_devices", _op.get_attr("num_devices"))
  else:
    _attr_T, input = _execute.args_to_matching_eager(list(input), _ctx)
    _inputs_flat = list(input)
    _attrs = ("reduction", reduction, "T", _attr_T, "num_devices",
              _attr_num_devices)
    _result = _execute.execute(b"NcclReduce", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "NcclReduce", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("NcclReduce")(None)

def _InitOpDefLibrary(op_list_proto_bytes):
  op_list = _op_def_pb2.OpList()
  op_list.ParseFromString(op_list_proto_bytes)
  _op_def_registry.register_op_list(op_list)
  op_def_lib = _op_def_library.OpDefLibrary()
  op_def_lib.add_op_list(op_list)
  return op_def_lib
# op {
#   name: "NcclAllReduce"
#   input_arg {
#     name: "input"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "data"
#     type_attr: "T"
#   }
#   attr {
#     name: "reduction"
#     type: "string"
#     allowed_values {
#       list {
#         s: "min"
#         s: "max"
#         s: "prod"
#         s: "sum"
#       }
#     }
#   }
#   attr {
#     name: "T"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_DOUBLE
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
#   attr {
#     name: "num_devices"
#     type: "int"
#   }
#   attr {
#     name: "shared_name"
#     type: "string"
#   }
#   is_stateful: true
# }
# op {
#   name: "NcclBroadcast"
#   input_arg {
#     name: "input"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "output"
#     type_attr: "T"
#   }
#   attr {
#     name: "T"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_DOUBLE
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
#   attr {
#     name: "shape"
#     type: "shape"
#   }
#   is_stateful: true
# }
# op {
#   name: "NcclReduce"
#   input_arg {
#     name: "input"
#     type_attr: "T"
#     number_attr: "num_devices"
#   }
#   output_arg {
#     name: "data"
#     type_attr: "T"
#   }
#   attr {
#     name: "reduction"
#     type: "string"
#     allowed_values {
#       list {
#         s: "min"
#         s: "max"
#         s: "prod"
#         s: "sum"
#       }
#     }
#   }
#   attr {
#     name: "T"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_DOUBLE
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
#   attr {
#     name: "num_devices"
#     type: "int"
#     has_minimum: true
#     minimum: 1
#   }
#   is_stateful: true
# }
_op_def_lib = _InitOpDefLibrary(b"\n\227\001\n\rNcclAllReduce\022\n\n\005input\"\001T\032\t\n\004data\"\001T\",\n\treduction\022\006string:\027\n\025\022\003min\022\003max\022\004prod\022\003sum\"\023\n\001T\022\004type:\010\n\0062\004\001\002\003\t\"\022\n\013num_devices\022\003int\"\025\n\013shared_name\022\006string\210\001\001\nP\n\rNcclBroadcast\022\n\n\005input\"\001T\032\013\n\006output\"\001T\"\023\n\001T\022\004type:\010\n\0062\004\001\002\003\t\"\016\n\005shape\022\005shape\210\001\001\n\216\001\n\nNcclReduce\022\027\n\005input\"\001T*\013num_devices\032\t\n\004data\"\001T\",\n\treduction\022\006string:\027\n\025\022\003min\022\003max\022\004prod\022\003sum\"\023\n\001T\022\004type:\010\n\0062\004\001\002\003\t\"\026\n\013num_devices\022\003int(\0010\001\210\001\001")
