"""Python wrappers around TensorFlow ops.

This file is MACHINE GENERATED! Do not edit.
Original C++ source file: stateless_random_ops.cc
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


@tf_export('stateless_random_normal')
def stateless_random_normal(shape, seed, dtype=_dtypes.float32, name=None):
  r"""TODO: add doc.

  Args:
    shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    seed: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    dtype: An optional `tf.DType` from: `tf.half, tf.float32, tf.float64`. Defaults to `tf.float32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `dtype`.
  """
  if dtype is None:
    dtype = _dtypes.float32
  dtype = _execute.make_type(dtype, "dtype")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "StatelessRandomNormal", shape=shape, seed=seed, dtype=dtype,
        name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("dtype", _op.get_attr("dtype"), "T", _op.get_attr("T"), "Tseed",
              _op.get_attr("Tseed"))
  else:
    _attr_T, (shape,) = _execute.args_to_matching_eager([shape], _ctx, _dtypes.int32)
    _attr_Tseed, (seed,) = _execute.args_to_matching_eager([seed], _ctx, _dtypes.int64)
    _inputs_flat = [shape, seed]
    _attrs = ("dtype", dtype, "T", _attr_T, "Tseed", _attr_Tseed)
    _result = _execute.execute(b"StatelessRandomNormal", 1,
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
  _execute.record_gradient(
      "StatelessRandomNormal", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("StatelessRandomNormal")(None)


@tf_export('stateless_random_uniform')
def stateless_random_uniform(shape, seed, dtype=_dtypes.float32, name=None):
  r"""TODO: add doc.

  Args:
    shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    seed: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    dtype: An optional `tf.DType` from: `tf.half, tf.float32, tf.float64`. Defaults to `tf.float32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `dtype`.
  """
  if dtype is None:
    dtype = _dtypes.float32
  dtype = _execute.make_type(dtype, "dtype")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "StatelessRandomUniform", shape=shape, seed=seed, dtype=dtype,
        name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("dtype", _op.get_attr("dtype"), "T", _op.get_attr("T"), "Tseed",
              _op.get_attr("Tseed"))
  else:
    _attr_T, (shape,) = _execute.args_to_matching_eager([shape], _ctx, _dtypes.int32)
    _attr_Tseed, (seed,) = _execute.args_to_matching_eager([seed], _ctx, _dtypes.int64)
    _inputs_flat = [shape, seed]
    _attrs = ("dtype", dtype, "T", _attr_T, "Tseed", _attr_Tseed)
    _result = _execute.execute(b"StatelessRandomUniform", 1,
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
  _execute.record_gradient(
      "StatelessRandomUniform", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("StatelessRandomUniform")(None)


@tf_export('stateless_truncated_normal')
def stateless_truncated_normal(shape, seed, dtype=_dtypes.float32, name=None):
  r"""TODO: add doc.

  Args:
    shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    seed: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    dtype: An optional `tf.DType` from: `tf.half, tf.float32, tf.float64`. Defaults to `tf.float32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `dtype`.
  """
  if dtype is None:
    dtype = _dtypes.float32
  dtype = _execute.make_type(dtype, "dtype")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "StatelessTruncatedNormal", shape=shape, seed=seed, dtype=dtype,
        name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("dtype", _op.get_attr("dtype"), "T", _op.get_attr("T"), "Tseed",
              _op.get_attr("Tseed"))
  else:
    _attr_T, (shape,) = _execute.args_to_matching_eager([shape], _ctx, _dtypes.int32)
    _attr_Tseed, (seed,) = _execute.args_to_matching_eager([seed], _ctx, _dtypes.int64)
    _inputs_flat = [shape, seed]
    _attrs = ("dtype", dtype, "T", _attr_T, "Tseed", _attr_Tseed)
    _result = _execute.execute(b"StatelessTruncatedNormal", 1,
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
  _execute.record_gradient(
      "StatelessTruncatedNormal", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("StatelessTruncatedNormal")(None)

def _InitOpDefLibrary(op_list_proto_bytes):
  op_list = _op_def_pb2.OpList()
  op_list.ParseFromString(op_list_proto_bytes)
  _op_def_registry.register_op_list(op_list)
  op_def_lib = _op_def_library.OpDefLibrary()
  op_def_lib.add_op_list(op_list)
  return op_def_lib
# op {
#   name: "StatelessRandomNormal"
#   input_arg {
#     name: "shape"
#     type_attr: "T"
#   }
#   input_arg {
#     name: "seed"
#     type_attr: "Tseed"
#   }
#   output_arg {
#     name: "output"
#     type_attr: "dtype"
#   }
#   attr {
#     name: "dtype"
#     type: "type"
#     default_value {
#       type: DT_FLOAT
#     }
#     allowed_values {
#       list {
#         type: DT_HALF
#         type: DT_FLOAT
#         type: DT_DOUBLE
#       }
#     }
#   }
#   attr {
#     name: "T"
#     type: "type"
#     default_value {
#       type: DT_INT32
#     }
#     allowed_values {
#       list {
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
#   attr {
#     name: "Tseed"
#     type: "type"
#     default_value {
#       type: DT_INT64
#     }
#     allowed_values {
#       list {
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
# }
# op {
#   name: "StatelessRandomUniform"
#   input_arg {
#     name: "shape"
#     type_attr: "T"
#   }
#   input_arg {
#     name: "seed"
#     type_attr: "Tseed"
#   }
#   output_arg {
#     name: "output"
#     type_attr: "dtype"
#   }
#   attr {
#     name: "dtype"
#     type: "type"
#     default_value {
#       type: DT_FLOAT
#     }
#     allowed_values {
#       list {
#         type: DT_HALF
#         type: DT_FLOAT
#         type: DT_DOUBLE
#       }
#     }
#   }
#   attr {
#     name: "T"
#     type: "type"
#     default_value {
#       type: DT_INT32
#     }
#     allowed_values {
#       list {
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
#   attr {
#     name: "Tseed"
#     type: "type"
#     default_value {
#       type: DT_INT64
#     }
#     allowed_values {
#       list {
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
# }
# op {
#   name: "StatelessTruncatedNormal"
#   input_arg {
#     name: "shape"
#     type_attr: "T"
#   }
#   input_arg {
#     name: "seed"
#     type_attr: "Tseed"
#   }
#   output_arg {
#     name: "output"
#     type_attr: "dtype"
#   }
#   attr {
#     name: "dtype"
#     type: "type"
#     default_value {
#       type: DT_FLOAT
#     }
#     allowed_values {
#       list {
#         type: DT_HALF
#         type: DT_FLOAT
#         type: DT_DOUBLE
#       }
#     }
#   }
#   attr {
#     name: "T"
#     type: "type"
#     default_value {
#       type: DT_INT32
#     }
#     allowed_values {
#       list {
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
#   attr {
#     name: "Tseed"
#     type: "type"
#     default_value {
#       type: DT_INT64
#     }
#     allowed_values {
#       list {
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
# }
_op_def_lib = _InitOpDefLibrary(b"\n\221\001\n\025StatelessRandomNormal\022\n\n\005shape\"\001T\022\r\n\004seed\"\005Tseed\032\017\n\006output\"\005dtype\"\032\n\005dtype\022\004type\032\0020\001:\007\n\0052\003\023\001\002\"\025\n\001T\022\004type\032\0020\003:\006\n\0042\002\003\t\"\031\n\005Tseed\022\004type\032\0020\t:\006\n\0042\002\003\t\n\222\001\n\026StatelessRandomUniform\022\n\n\005shape\"\001T\022\r\n\004seed\"\005Tseed\032\017\n\006output\"\005dtype\"\032\n\005dtype\022\004type\032\0020\001:\007\n\0052\003\023\001\002\"\025\n\001T\022\004type\032\0020\003:\006\n\0042\002\003\t\"\031\n\005Tseed\022\004type\032\0020\t:\006\n\0042\002\003\t\n\224\001\n\030StatelessTruncatedNormal\022\n\n\005shape\"\001T\022\r\n\004seed\"\005Tseed\032\017\n\006output\"\005dtype\"\032\n\005dtype\022\004type\032\0020\001:\007\n\0052\003\023\001\002\"\025\n\001T\022\004type\032\0020\003:\006\n\0042\002\003\t\"\031\n\005Tseed\022\004type\032\0020\t:\006\n\0042\002\003\t")
