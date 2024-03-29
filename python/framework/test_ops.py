"""Python wrappers around TensorFlow ops.

This file is MACHINE GENERATED! Do not edit.
Original C++ source file: test_ops.cc
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


@tf_export('a')
def a(name=None):
  r"""TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "A", name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    _inputs_flat = []
    _attrs = None
    _result = _execute.execute(b"A", 1, inputs=_inputs_flat, attrs=_attrs,
                               ctx=_ctx, name=name)
  _execute.record_gradient(
      "A", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("A")(None)


@tf_export('attr')
def attr(a, name=None):
  r"""TODO: add doc.

  Args:
    a: An `int`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  a = _execute.make_int(a, "a")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "Attr", a=a, name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = ("a", a)
    _result = _execute.execute(b"Attr", 0, inputs=_inputs_flat, attrs=_attrs,
                               ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("Attr")(None)


@tf_export('attr_bool')
def attr_bool(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A `bool`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  a = _execute.make_bool(a, "a")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "AttrBool", a=a, name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = ("a", a)
    _result = _execute.execute(b"AttrBool", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("AttrBool")(None)


@tf_export('attr_bool_list')
def attr_bool_list(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A list of `bools`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  if not isinstance(a, (list, tuple)):
    raise TypeError(
        "Expected list for 'a' argument to "
        "'attr_bool_list' Op, not %r." % a)
  a = [_execute.make_bool(_b, "a") for _b in a]
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "AttrBoolList", a=a, name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = ("a", a)
    _result = _execute.execute(b"AttrBoolList", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("AttrBoolList")(None)


@tf_export('attr_default')
def attr_default(a="banana", name=None):
  r"""TODO: add doc.

  Args:
    a: An optional `string`. Defaults to `"banana"`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  if a is None:
    a = "banana"
  a = _execute.make_str(a, "a")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "AttrDefault", a=a, name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = ("a", a)
    _result = _execute.execute(b"AttrDefault", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("AttrDefault")(None)


@tf_export('attr_empty_list_default')
def attr_empty_list_default(a=[], name=None):
  r"""TODO: add doc.

  Args:
    a: An optional list of `floats`. Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  if a is None:
    a = []
  if not isinstance(a, (list, tuple)):
    raise TypeError(
        "Expected list for 'a' argument to "
        "'attr_empty_list_default' Op, not %r." % a)
  a = [_execute.make_float(_f, "a") for _f in a]
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "AttrEmptyListDefault", a=a, name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = ("a", a)
    _result = _execute.execute(b"AttrEmptyListDefault", 0,
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
    _result = None
  return _result

_ops.RegisterShape("AttrEmptyListDefault")(None)


@tf_export('attr_enum')
def attr_enum(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A `string` from: `"apples", "oranges"`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  a = _execute.make_str(a, "a")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "AttrEnum", a=a, name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = ("a", a)
    _result = _execute.execute(b"AttrEnum", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("AttrEnum")(None)


@tf_export('attr_enum_list')
def attr_enum_list(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A list of `strings` from: `"apples", "oranges"`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  if not isinstance(a, (list, tuple)):
    raise TypeError(
        "Expected list for 'a' argument to "
        "'attr_enum_list' Op, not %r." % a)
  a = [_execute.make_str(_s, "a") for _s in a]
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "AttrEnumList", a=a, name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = ("a", a)
    _result = _execute.execute(b"AttrEnumList", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("AttrEnumList")(None)


@tf_export('attr_float')
def attr_float(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A `float`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  a = _execute.make_float(a, "a")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "AttrFloat", a=a, name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = ("a", a)
    _result = _execute.execute(b"AttrFloat", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("AttrFloat")(None)


@tf_export('attr_list_default')
def attr_list_default(a=[5, 15], name=None):
  r"""TODO: add doc.

  Args:
    a: An optional list of `ints`. Defaults to `[5, 15]`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  if a is None:
    a = [5, 15]
  if not isinstance(a, (list, tuple)):
    raise TypeError(
        "Expected list for 'a' argument to "
        "'attr_list_default' Op, not %r." % a)
  a = [_execute.make_int(_i, "a") for _i in a]
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "AttrListDefault", a=a, name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = ("a", a)
    _result = _execute.execute(b"AttrListDefault", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("AttrListDefault")(None)


@tf_export('attr_list_min')
def attr_list_min(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A list of `ints` that has length `>= 2`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  if not isinstance(a, (list, tuple)):
    raise TypeError(
        "Expected list for 'a' argument to "
        "'attr_list_min' Op, not %r." % a)
  a = [_execute.make_int(_i, "a") for _i in a]
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "AttrListMin", a=a, name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = ("a", a)
    _result = _execute.execute(b"AttrListMin", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("AttrListMin")(None)


@tf_export('attr_list_type_default')
def attr_list_type_default(a, b, name=None):
  r"""TODO: add doc.

  Args:
    a: A list of at least 1 `Tensor` objects with the same type.
    b: A list with the same length as `a` of `Tensor` objects with the same type as `a`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  if not isinstance(a, (list, tuple)):
    raise TypeError(
        "Expected list for 'a' argument to "
        "'attr_list_type_default' Op, not %r." % a)
  _attr_N = len(a)
  if not isinstance(b, (list, tuple)):
    raise TypeError(
        "Expected list for 'b' argument to "
        "'attr_list_type_default' Op, not %r." % b)
  if len(b) != _attr_N:
    raise ValueError(
        "List argument 'b' to 'attr_list_type_default' Op with length %d "
        "must match length %d of argument 'a'." %
        (len(b), _attr_N))
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "AttrListTypeDefault", a=a, b=b, name=name)
    return _op
  else:
    _attr_T, _inputs_T = _execute.args_to_matching_eager(list(a) + list(b), _ctx, _dtypes.int32)
    _inputs_T = [_inputs_T[:_attr_N]] + _inputs_T[_attr_N:]
    _inputs_T = _inputs_T[:1] + [_inputs_T[1:]]
    (a, b) = _inputs_T
    _inputs_flat = list(a) + list(b)
    _attrs = ("T", _attr_T, "N", _attr_N)
    _result = _execute.execute(b"AttrListTypeDefault", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("AttrListTypeDefault")(None)


@tf_export('attr_min')
def attr_min(a, name=None):
  r"""TODO: add doc.

  Args:
    a: An `int` that is `>= 5`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  a = _execute.make_int(a, "a")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "AttrMin", a=a, name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = ("a", a)
    _result = _execute.execute(b"AttrMin", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("AttrMin")(None)


@tf_export('attr_partial_shape')
def attr_partial_shape(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A `tf.TensorShape` or list of `ints`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  a = _execute.make_shape(a, "a")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "AttrPartialShape", a=a, name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = ("a", a)
    _result = _execute.execute(b"AttrPartialShape", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("AttrPartialShape")(None)


@tf_export('attr_partial_shape_list')
def attr_partial_shape_list(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A list of shapes (each a `tf.TensorShape` or list of `ints`).
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  if not isinstance(a, (list, tuple)):
    raise TypeError(
        "Expected list for 'a' argument to "
        "'attr_partial_shape_list' Op, not %r." % a)
  a = [_execute.make_shape(_s, "a") for _s in a]
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "AttrPartialShapeList", a=a, name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = ("a", a)
    _result = _execute.execute(b"AttrPartialShapeList", 0,
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
    _result = None
  return _result

_ops.RegisterShape("AttrPartialShapeList")(None)


@tf_export('attr_shape')
def attr_shape(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A `tf.TensorShape` or list of `ints`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  a = _execute.make_shape(a, "a")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "AttrShape", a=a, name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = ("a", a)
    _result = _execute.execute(b"AttrShape", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("AttrShape")(None)


@tf_export('attr_shape_list')
def attr_shape_list(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A list of shapes (each a `tf.TensorShape` or list of `ints`).
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  if not isinstance(a, (list, tuple)):
    raise TypeError(
        "Expected list for 'a' argument to "
        "'attr_shape_list' Op, not %r." % a)
  a = [_execute.make_shape(_s, "a") for _s in a]
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "AttrShapeList", a=a, name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = ("a", a)
    _result = _execute.execute(b"AttrShapeList", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("AttrShapeList")(None)


@tf_export('attr_type_default')
def attr_type_default(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A `Tensor`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "AttrTypeDefault", a=a, name=name)
    return _op
  else:
    _attr_T, (a,) = _execute.args_to_matching_eager([a], _ctx, _dtypes.int32)
    _inputs_flat = [a]
    _attrs = ("T", _attr_T)
    _result = _execute.execute(b"AttrTypeDefault", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("AttrTypeDefault")(None)


@tf_export('b')
def b(name=None):
  r"""TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "B", name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    _inputs_flat = []
    _attrs = None
    _result = _execute.execute(b"B", 1, inputs=_inputs_flat, attrs=_attrs,
                               ctx=_ctx, name=name)
  _execute.record_gradient(
      "B", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("B")(None)


@tf_export('binary')
def binary(a, b, name=None):
  r"""TODO: add doc.

  Args:
    a: A `Tensor`.
    b: A `Tensor`. Must have the same type as `a`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `a`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "Binary", a=a, b=b, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"))
  else:
    _attr_T, _inputs_T = _execute.args_to_matching_eager([a, b], _ctx)
    (a, b) = _inputs_T
    _inputs_flat = [a, b]
    _attrs = ("T", _attr_T)
    _result = _execute.execute(b"Binary", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "Binary", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("Binary")(None)


_complex_struct_outputs = ["a", "b", "c"]
_ComplexStructOutput = _collections.namedtuple(
    "ComplexStruct", _complex_struct_outputs)


@tf_export('complex_struct')
def complex_struct(n_a, n_b, t_c, name=None):
  r"""TODO: add doc.

  Args:
    n_a: An `int` that is `>= 0`.
    n_b: An `int` that is `>= 0`.
    t_c: A list of `tf.DTypes`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (a, b, c).

    a: A list of `n_a` `Tensor` objects with type `int32`.
    b: A list of `n_b` `Tensor` objects with type `int64`.
    c: A list of `Tensor` objects of type `t_c`.
  """
  n_a = _execute.make_int(n_a, "n_a")
  n_b = _execute.make_int(n_b, "n_b")
  if not isinstance(t_c, (list, tuple)):
    raise TypeError(
        "Expected list for 't_c' argument to "
        "'complex_struct' Op, not %r." % t_c)
  t_c = [_execute.make_type(_t, "t_c") for _t in t_c]
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ComplexStruct", n_a=n_a, n_b=n_b, t_c=t_c, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("n_a", _op.get_attr("n_a"), "n_b", _op.get_attr("n_b"), "t_c",
              _op.get_attr("t_c"))
  else:
    _inputs_flat = []
    _attrs = ("n_a", n_a, "n_b", n_b, "t_c", t_c)
    _result = _execute.execute(b"ComplexStruct", n_a + n_b + len(t_c),
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
  _execute.record_gradient(
      "ComplexStruct", _inputs_flat, _attrs, _result, name)
  _result = [_result[:n_a]] + _result[n_a:]
  _result = _result[:1] + [_result[1:1 + n_b]] + _result[1 + n_b:]
  _result = _result[:2] + [_result[2:]]
  _result = _ComplexStructOutput._make(_result)
  return _result

_ops.RegisterShape("ComplexStruct")(None)


@tf_export('copy_op')
def copy_op(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A `Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `a`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "CopyOp", a=a, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"))
  else:
    _attr_T, (a,) = _execute.args_to_matching_eager([a], _ctx)
    _inputs_flat = [a]
    _attrs = ("T", _attr_T)
    _result = _execute.execute(b"CopyOp", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "CopyOp", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("CopyOp")(None)


@tf_export('default_attrs')
def default_attrs(string_val="abc", string_list_val=["abc", ""], int_val=123, int_list_val=[1, 2, 3], float_val=10, float_list_val=[10], bool_val=True, bool_list_val=[True, False], type_val=_dtypes.int32, type_list_val=[_dtypes.int32, _dtypes.float32], shape_val=[2, 1], shape_list_val=[[], [1]], tensor_val=_execute.make_tensor("""dtype: DT_INT32 tensor_shape { } int_val: 1""", "tensor_val"), tensor_list_val=[_execute.make_tensor(_pb, "tensor_list_val") for _pb in ("""dtype: DT_INT32 tensor_shape { } int_val: 1""",)], name=None):
  r"""TODO: add doc.

  Args:
    string_val: An optional `string`. Defaults to `"abc"`.
    string_list_val: An optional list of `strings`. Defaults to `["abc", ""]`.
    int_val: An optional `int`. Defaults to `123`.
    int_list_val: An optional list of `ints`. Defaults to `[1, 2, 3]`.
    float_val: An optional `float`. Defaults to `10`.
    float_list_val: An optional list of `floats`. Defaults to `[10]`.
    bool_val: An optional `bool`. Defaults to `True`.
    bool_list_val: An optional list of `bools`. Defaults to `[True, False]`.
    type_val: An optional `tf.DType`. Defaults to `tf.int32`.
    type_list_val: An optional list of `tf.DTypes`. Defaults to `[tf.int32, tf.float32]`.
    shape_val: An optional `tf.TensorShape` or list of `ints`. Defaults to `[2, 1]`.
    shape_list_val: An optional list of shapes (each a `tf.TensorShape` or list of `ints`). Defaults to `[[], [1]]`.
    tensor_val: An optional `tf.TensorProto`. Defaults to `dtype: DT_INT32 tensor_shape { } int_val: 1`.
    tensor_list_val: An optional list of `tf.TensorProto` objects. Defaults to `[dtype: DT_INT32 tensor_shape { } int_val: 1]`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  if string_val is None:
    string_val = "abc"
  string_val = _execute.make_str(string_val, "string_val")
  if string_list_val is None:
    string_list_val = ["abc", ""]
  if not isinstance(string_list_val, (list, tuple)):
    raise TypeError(
        "Expected list for 'string_list_val' argument to "
        "'default_attrs' Op, not %r." % string_list_val)
  string_list_val = [_execute.make_str(_s, "string_list_val") for _s in string_list_val]
  if int_val is None:
    int_val = 123
  int_val = _execute.make_int(int_val, "int_val")
  if int_list_val is None:
    int_list_val = [1, 2, 3]
  if not isinstance(int_list_val, (list, tuple)):
    raise TypeError(
        "Expected list for 'int_list_val' argument to "
        "'default_attrs' Op, not %r." % int_list_val)
  int_list_val = [_execute.make_int(_i, "int_list_val") for _i in int_list_val]
  if float_val is None:
    float_val = 10
  float_val = _execute.make_float(float_val, "float_val")
  if float_list_val is None:
    float_list_val = [10]
  if not isinstance(float_list_val, (list, tuple)):
    raise TypeError(
        "Expected list for 'float_list_val' argument to "
        "'default_attrs' Op, not %r." % float_list_val)
  float_list_val = [_execute.make_float(_f, "float_list_val") for _f in float_list_val]
  if bool_val is None:
    bool_val = True
  bool_val = _execute.make_bool(bool_val, "bool_val")
  if bool_list_val is None:
    bool_list_val = [True, False]
  if not isinstance(bool_list_val, (list, tuple)):
    raise TypeError(
        "Expected list for 'bool_list_val' argument to "
        "'default_attrs' Op, not %r." % bool_list_val)
  bool_list_val = [_execute.make_bool(_b, "bool_list_val") for _b in bool_list_val]
  if type_val is None:
    type_val = _dtypes.int32
  type_val = _execute.make_type(type_val, "type_val")
  if type_list_val is None:
    type_list_val = [_dtypes.int32, _dtypes.float32]
  if not isinstance(type_list_val, (list, tuple)):
    raise TypeError(
        "Expected list for 'type_list_val' argument to "
        "'default_attrs' Op, not %r." % type_list_val)
  type_list_val = [_execute.make_type(_t, "type_list_val") for _t in type_list_val]
  if shape_val is None:
    shape_val = [2, 1]
  shape_val = _execute.make_shape(shape_val, "shape_val")
  if shape_list_val is None:
    shape_list_val = [[], [1]]
  if not isinstance(shape_list_val, (list, tuple)):
    raise TypeError(
        "Expected list for 'shape_list_val' argument to "
        "'default_attrs' Op, not %r." % shape_list_val)
  shape_list_val = [_execute.make_shape(_s, "shape_list_val") for _s in shape_list_val]
  if tensor_val is None:
    tensor_val = _execute.make_tensor("""dtype: DT_INT32 tensor_shape { } int_val: 1""", "tensor_val")
  tensor_val = _execute.make_tensor(tensor_val, "tensor_val")
  if tensor_list_val is None:
    tensor_list_val = [_execute.make_tensor(_pb, "tensor_list_val") for _pb in ("""dtype: DT_INT32 tensor_shape { } int_val: 1""",)]
  if not isinstance(tensor_list_val, (list, tuple)):
    raise TypeError(
        "Expected list for 'tensor_list_val' argument to "
        "'default_attrs' Op, not %r." % tensor_list_val)
  tensor_list_val = [_execute.make_tensor(_t, "tensor_list_val") for _t in tensor_list_val]
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "DefaultAttrs", string_val=string_val,
        string_list_val=string_list_val, int_val=int_val,
        int_list_val=int_list_val, float_val=float_val,
        float_list_val=float_list_val, bool_val=bool_val,
        bool_list_val=bool_list_val, type_val=type_val,
        type_list_val=type_list_val, shape_val=shape_val,
        shape_list_val=shape_list_val, tensor_val=tensor_val,
        tensor_list_val=tensor_list_val, name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = ("string_val", string_val, "string_list_val", string_list_val,
              "int_val", int_val, "int_list_val", int_list_val, "float_val",
              float_val, "float_list_val", float_list_val, "bool_val",
              bool_val, "bool_list_val", bool_list_val, "type_val", type_val,
              "type_list_val", type_list_val, "shape_val", shape_val,
              "shape_list_val", shape_list_val, "tensor_val", tensor_val,
              "tensor_list_val", tensor_list_val)
    _result = _execute.execute(b"DefaultAttrs", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("DefaultAttrs")(None)


_five_float_outputs_outputs = ["a", "b", "c", "d", "e"]
_FiveFloatOutputsOutput = _collections.namedtuple(
    "FiveFloatOutputs", _five_float_outputs_outputs)


@tf_export('five_float_outputs')
def five_float_outputs(name=None):
  r"""TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (a, b, c, d, e).

    a: A `Tensor` of type `float32`.
    b: A `Tensor` of type `float32`.
    c: A `Tensor` of type `float32`.
    d: A `Tensor` of type `float32`.
    e: A `Tensor` of type `float32`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "FiveFloatOutputs", name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    _inputs_flat = []
    _attrs = None
    _result = _execute.execute(b"FiveFloatOutputs", 5, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "FiveFloatOutputs", _inputs_flat, _attrs, _result, name)
  _result = _FiveFloatOutputsOutput._make(_result)
  return _result

_ops.RegisterShape("FiveFloatOutputs")(None)


@tf_export('float_input')
def float_input(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A `Tensor` of type `float32`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "FloatInput", a=a, name=name)
    return _op
  else:
    a = _ops.convert_to_tensor(a, _dtypes.float32)
    _inputs_flat = [a]
    _attrs = None
    _result = _execute.execute(b"FloatInput", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("FloatInput")(None)


@tf_export('float_output')
def float_output(name=None):
  r"""TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "FloatOutput", name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    _inputs_flat = []
    _attrs = None
    _result = _execute.execute(b"FloatOutput", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "FloatOutput", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("FloatOutput")(None)


_float_output_string_output_outputs = ["a", "b"]
_FloatOutputStringOutputOutput = _collections.namedtuple(
    "FloatOutputStringOutput", _float_output_string_output_outputs)


@tf_export('float_output_string_output')
def float_output_string_output(name=None):
  r"""TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (a, b).

    a: A `Tensor` of type `float32`.
    b: A `Tensor` of type `string`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "FloatOutputStringOutput", name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    _inputs_flat = []
    _attrs = None
    _result = _execute.execute(b"FloatOutputStringOutput", 2,
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
  _execute.record_gradient(
      "FloatOutputStringOutput", _inputs_flat, _attrs, _result, name)
  _result = _FloatOutputStringOutputOutput._make(_result)
  return _result

_ops.RegisterShape("FloatOutputStringOutput")(None)


_foo1_outputs = ["d", "e"]
_Foo1Output = _collections.namedtuple(
    "Foo1", _foo1_outputs)


@tf_export('foo1')
def foo1(a, b, c, name=None):
  r"""TODO: add doc.

  Args:
    a: A `Tensor` of type `float32`.
    b: A `Tensor` of type `int32`.
    c: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (d, e).

    d: A `Tensor` of type `float32`.
    e: A `Tensor` of type `int32`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "Foo1", a=a, b=b, c=c, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    a = _ops.convert_to_tensor(a, _dtypes.float32)
    b = _ops.convert_to_tensor(b, _dtypes.int32)
    c = _ops.convert_to_tensor(c, _dtypes.int32)
    _inputs_flat = [a, b, c]
    _attrs = None
    _result = _execute.execute(b"Foo1", 2, inputs=_inputs_flat, attrs=_attrs,
                               ctx=_ctx, name=name)
  _execute.record_gradient(
      "Foo1", _inputs_flat, _attrs, _result, name)
  _result = _Foo1Output._make(_result)
  return _result

_ops.RegisterShape("Foo1")(None)


_foo2_outputs = ["d", "e"]
_Foo2Output = _collections.namedtuple(
    "Foo2", _foo2_outputs)


@tf_export('foo2')
def foo2(a, b, c, name=None):
  r"""TODO: add doc.

  Args:
    a: A `Tensor` of type `float32`.
    b: A `Tensor` of type `string`.
    c: A `Tensor` of type `string`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (d, e).

    d: A `Tensor` of type `float32`.
    e: A `Tensor` of type `int32`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "Foo2", a=a, b=b, c=c, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    a = _ops.convert_to_tensor(a, _dtypes.float32)
    b = _ops.convert_to_tensor(b, _dtypes.string)
    c = _ops.convert_to_tensor(c, _dtypes.string)
    _inputs_flat = [a, b, c]
    _attrs = None
    _result = _execute.execute(b"Foo2", 2, inputs=_inputs_flat, attrs=_attrs,
                               ctx=_ctx, name=name)
  _execute.record_gradient(
      "Foo2", _inputs_flat, _attrs, _result, name)
  _result = _Foo2Output._make(_result)
  return _result

_ops.RegisterShape("Foo2")(None)


_foo3_outputs = ["d", "e"]
_Foo3Output = _collections.namedtuple(
    "Foo3", _foo3_outputs)


@tf_export('foo3')
def foo3(a, b, c, name=None):
  r"""TODO: add doc.

  Args:
    a: A `Tensor` of type `float32`.
    b: A `Tensor` of type `string`.
    c: A `Tensor` of type `float32`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (d, e).

    d: A `Tensor` of type `float32`.
    e: A `Tensor` of type `int32`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "Foo3", a=a, b=b, c=c, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    a = _ops.convert_to_tensor(a, _dtypes.float32)
    b = _ops.convert_to_tensor(b, _dtypes.string)
    c = _ops.convert_to_tensor(c, _dtypes.float32)
    _inputs_flat = [a, b, c]
    _attrs = None
    _result = _execute.execute(b"Foo3", 2, inputs=_inputs_flat, attrs=_attrs,
                               ctx=_ctx, name=name)
  _execute.record_gradient(
      "Foo3", _inputs_flat, _attrs, _result, name)
  _result = _Foo3Output._make(_result)
  return _result

_ops.RegisterShape("Foo3")(None)


@tf_export('func_attr')
def func_attr(f, name=None):
  r"""TODO: add doc.

  Args:
    f: A function decorated with @Defun.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "FuncAttr", f=f, name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = ("f", f)
    _result = _execute.execute(b"FuncAttr", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("FuncAttr")(None)


@tf_export('graph_def_version')
def graph_def_version(name=None):
  r"""TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "GraphDefVersion", name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    _inputs_flat = []
    _attrs = None
    _result = _execute.execute(b"GraphDefVersion", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "GraphDefVersion", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("GraphDefVersion")(None)


@tf_export('in_polymorphic_twice')
def in_polymorphic_twice(a, b, name=None):
  r"""TODO: add doc.

  Args:
    a: A list of `Tensor` objects with the same type.
    b: A list of `Tensor` objects with the same type as `a`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  if not isinstance(a, (list, tuple)):
    raise TypeError(
        "Expected list for 'a' argument to "
        "'in_polymorphic_twice' Op, not %r." % a)
  _attr_N = len(a)
  if not isinstance(b, (list, tuple)):
    raise TypeError(
        "Expected list for 'b' argument to "
        "'in_polymorphic_twice' Op, not %r." % b)
  _attr_M = len(b)
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "InPolymorphicTwice", a=a, b=b, name=name)
    return _op
  else:
    _attr_T, _inputs_T = _execute.args_to_matching_eager(list(a) + list(b), _ctx)
    _inputs_T = [_inputs_T[:_attr_N]] + _inputs_T[_attr_N:]
    _inputs_T = _inputs_T[:1] + [_inputs_T[1:]]
    (a, b) = _inputs_T
    _inputs_flat = list(a) + list(b)
    _attrs = ("T", _attr_T, "N", _attr_N, "M", _attr_M)
    _result = _execute.execute(b"InPolymorphicTwice", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("InPolymorphicTwice")(None)


@tf_export('int64_output')
def int64_output(name=None):
  r"""TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int64`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "Int64Output", name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    _inputs_flat = []
    _attrs = None
    _result = _execute.execute(b"Int64Output", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "Int64Output", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("Int64Output")(None)


@tf_export('int_attr')
def int_attr(foo=1, name=None):
  r"""TODO: add doc.

  Args:
    foo: An optional `int`. Defaults to `1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int64`.
  """
  if foo is None:
    foo = 1
  foo = _execute.make_int(foo, "foo")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "IntAttr", foo=foo, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("foo", _op.get_attr("foo"))
  else:
    _inputs_flat = []
    _attrs = ("foo", foo)
    _result = _execute.execute(b"IntAttr", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "IntAttr", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("IntAttr")(None)


@tf_export('int_input')
def int_input(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "IntInput", a=a, name=name)
    return _op
  else:
    a = _ops.convert_to_tensor(a, _dtypes.int32)
    _inputs_flat = [a]
    _attrs = None
    _result = _execute.execute(b"IntInput", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("IntInput")(None)


@tf_export('int_input_float_input')
def int_input_float_input(a, b, name=None):
  r"""TODO: add doc.

  Args:
    a: A `Tensor` of type `int32`.
    b: A `Tensor` of type `float32`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "IntInputFloatInput", a=a, b=b, name=name)
    return _op
  else:
    a = _ops.convert_to_tensor(a, _dtypes.int32)
    b = _ops.convert_to_tensor(b, _dtypes.float32)
    _inputs_flat = [a, b]
    _attrs = None
    _result = _execute.execute(b"IntInputFloatInput", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("IntInputFloatInput")(None)


@tf_export('int_input_int_output')
def int_input_int_output(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "IntInputIntOutput", a=a, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    a = _ops.convert_to_tensor(a, _dtypes.int32)
    _inputs_flat = [a]
    _attrs = None
    _result = _execute.execute(b"IntInputIntOutput", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "IntInputIntOutput", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("IntInputIntOutput")(None)


@tf_export('int_output')
def int_output(name=None):
  r"""TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "IntOutput", name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    _inputs_flat = []
    _attrs = None
    _result = _execute.execute(b"IntOutput", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "IntOutput", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("IntOutput")(None)


_int_output_float_output_outputs = ["a", "b"]
_IntOutputFloatOutputOutput = _collections.namedtuple(
    "IntOutputFloatOutput", _int_output_float_output_outputs)


@tf_export('int_output_float_output')
def int_output_float_output(name=None):
  r"""TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (a, b).

    a: A `Tensor` of type `int32`.
    b: A `Tensor` of type `float32`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "IntOutputFloatOutput", name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    _inputs_flat = []
    _attrs = None
    _result = _execute.execute(b"IntOutputFloatOutput", 2,
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
  _execute.record_gradient(
      "IntOutputFloatOutput", _inputs_flat, _attrs, _result, name)
  _result = _IntOutputFloatOutputOutput._make(_result)
  return _result

_ops.RegisterShape("IntOutputFloatOutput")(None)


@tf_export('kernel_label')
def kernel_label(name=None):
  r"""TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "KernelLabel", name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    _inputs_flat = []
    _attrs = None
    _result = _execute.execute(b"KernelLabel", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "KernelLabel", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("KernelLabel")(None)


@tf_export('kernel_label_required')
def kernel_label_required(input, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "KernelLabelRequired", input=input, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    input = _ops.convert_to_tensor(input, _dtypes.int32)
    _inputs_flat = [input]
    _attrs = None
    _result = _execute.execute(b"KernelLabelRequired", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "KernelLabelRequired", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("KernelLabelRequired")(None)


@tf_export('list_input')
def list_input(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A list of at least 1 `Tensor` objects with the same type.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  if not isinstance(a, (list, tuple)):
    raise TypeError(
        "Expected list for 'a' argument to "
        "'list_input' Op, not %r." % a)
  _attr_N = len(a)
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ListInput", a=a, name=name)
    return _op
  else:
    _attr_T, a = _execute.args_to_matching_eager(list(a), _ctx)
    _inputs_flat = list(a)
    _attrs = ("N", _attr_N, "T", _attr_T)
    _result = _execute.execute(b"ListInput", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("ListInput")(None)


@tf_export('list_output')
def list_output(T, name=None):
  r"""TODO: add doc.

  Args:
    T: A list of `tf.DTypes` that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `T`.
  """
  if not isinstance(T, (list, tuple)):
    raise TypeError(
        "Expected list for 'T' argument to "
        "'list_output' Op, not %r." % T)
  T = [_execute.make_type(_t, "T") for _t in T]
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ListOutput", T=T, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"))
  else:
    _inputs_flat = []
    _attrs = ("T", T)
    _result = _execute.execute(b"ListOutput", len(T), inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "ListOutput", _inputs_flat, _attrs, _result, name)
  return _result

_ops.RegisterShape("ListOutput")(None)


_mixed_struct_outputs = ["a", "b"]
_MixedStructOutput = _collections.namedtuple(
    "MixedStruct", _mixed_struct_outputs)


@tf_export('mixed_struct')
def mixed_struct(n_a, name=None):
  r"""TODO: add doc.

  Args:
    n_a: An `int` that is `>= 0`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (a, b).

    a: A list of `n_a` `Tensor` objects with type `int32`.
    b: A `Tensor` of type `float32`.
  """
  n_a = _execute.make_int(n_a, "n_a")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "MixedStruct", n_a=n_a, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("n_a", _op.get_attr("n_a"))
  else:
    _inputs_flat = []
    _attrs = ("n_a", n_a)
    _result = _execute.execute(b"MixedStruct", n_a + 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "MixedStruct", _inputs_flat, _attrs, _result, name)
  _result = [_result[:n_a]] + _result[n_a:]
  _result = _MixedStructOutput._make(_result)
  return _result

_ops.RegisterShape("MixedStruct")(None)


@tf_export('n_in_polymorphic_twice')
def n_in_polymorphic_twice(a, b, name=None):
  r"""TODO: add doc.

  Args:
    a: A list of `Tensor` objects with the same type.
    b: A list with the same length as `a` of `Tensor` objects with the same type as `a`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  if not isinstance(a, (list, tuple)):
    raise TypeError(
        "Expected list for 'a' argument to "
        "'n_in_polymorphic_twice' Op, not %r." % a)
  _attr_N = len(a)
  if not isinstance(b, (list, tuple)):
    raise TypeError(
        "Expected list for 'b' argument to "
        "'n_in_polymorphic_twice' Op, not %r." % b)
  if len(b) != _attr_N:
    raise ValueError(
        "List argument 'b' to 'n_in_polymorphic_twice' Op with length %d "
        "must match length %d of argument 'a'." %
        (len(b), _attr_N))
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "NInPolymorphicTwice", a=a, b=b, name=name)
    return _op
  else:
    _attr_T, _inputs_T = _execute.args_to_matching_eager(list(a) + list(b), _ctx)
    _inputs_T = [_inputs_T[:_attr_N]] + _inputs_T[_attr_N:]
    _inputs_T = _inputs_T[:1] + [_inputs_T[1:]]
    (a, b) = _inputs_T
    _inputs_flat = list(a) + list(b)
    _attrs = ("T", _attr_T, "N", _attr_N)
    _result = _execute.execute(b"NInPolymorphicTwice", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("NInPolymorphicTwice")(None)


@tf_export('n_in_twice')
def n_in_twice(a, b, name=None):
  r"""TODO: add doc.

  Args:
    a: A list of `Tensor` objects with type `int32`.
    b: A list with the same length as `a` of `Tensor` objects with type `string`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  if not isinstance(a, (list, tuple)):
    raise TypeError(
        "Expected list for 'a' argument to "
        "'n_in_twice' Op, not %r." % a)
  _attr_N = len(a)
  if not isinstance(b, (list, tuple)):
    raise TypeError(
        "Expected list for 'b' argument to "
        "'n_in_twice' Op, not %r." % b)
  if len(b) != _attr_N:
    raise ValueError(
        "List argument 'b' to 'n_in_twice' Op with length %d "
        "must match length %d of argument 'a'." %
        (len(b), _attr_N))
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "NInTwice", a=a, b=b, name=name)
    return _op
  else:
    a = _ops.convert_n_to_tensor(a, _dtypes.int32)
    b = _ops.convert_n_to_tensor(b, _dtypes.string)
    _inputs_flat = list(a) + list(b)
    _attrs = ("N", _attr_N)
    _result = _execute.execute(b"NInTwice", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("NInTwice")(None)


@tf_export('n_in_two_type_variables')
def n_in_two_type_variables(a, b, name=None):
  r"""TODO: add doc.

  Args:
    a: A list of `Tensor` objects with the same type.
    b: A list with the same length as `a` of `Tensor` objects with the same type.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  if not isinstance(a, (list, tuple)):
    raise TypeError(
        "Expected list for 'a' argument to "
        "'n_in_two_type_variables' Op, not %r." % a)
  _attr_N = len(a)
  if not isinstance(b, (list, tuple)):
    raise TypeError(
        "Expected list for 'b' argument to "
        "'n_in_two_type_variables' Op, not %r." % b)
  if len(b) != _attr_N:
    raise ValueError(
        "List argument 'b' to 'n_in_two_type_variables' Op with length %d "
        "must match length %d of argument 'a'." %
        (len(b), _attr_N))
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "NInTwoTypeVariables", a=a, b=b, name=name)
    return _op
  else:
    _attr_S, a = _execute.args_to_matching_eager(list(a), _ctx)
    _attr_T, b = _execute.args_to_matching_eager(list(b), _ctx)
    _inputs_flat = list(a) + list(b)
    _attrs = ("S", _attr_S, "T", _attr_T, "N", _attr_N)
    _result = _execute.execute(b"NInTwoTypeVariables", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("NInTwoTypeVariables")(None)


@tf_export('n_ints_in')
def n_ints_in(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A list of at least 2 `Tensor` objects with type `int32`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  if not isinstance(a, (list, tuple)):
    raise TypeError(
        "Expected list for 'a' argument to "
        "'n_ints_in' Op, not %r." % a)
  _attr_N = len(a)
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "NIntsIn", a=a, name=name)
    return _op
  else:
    a = _ops.convert_n_to_tensor(a, _dtypes.int32)
    _inputs_flat = list(a)
    _attrs = ("N", _attr_N)
    _result = _execute.execute(b"NIntsIn", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("NIntsIn")(None)


@tf_export('n_ints_out')
def n_ints_out(N, name=None):
  r"""TODO: add doc.

  Args:
    N: An `int` that is `>= 2`.
    name: A name for the operation (optional).

  Returns:
    A list of `N` `Tensor` objects with type `int32`.
  """
  N = _execute.make_int(N, "N")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "NIntsOut", N=N, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("N", _op.get_attr("N"))
  else:
    _inputs_flat = []
    _attrs = ("N", N)
    _result = _execute.execute(b"NIntsOut", N, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "NIntsOut", _inputs_flat, _attrs, _result, name)
  return _result

_ops.RegisterShape("NIntsOut")(None)


@tf_export('n_ints_out_default')
def n_ints_out_default(N=3, name=None):
  r"""TODO: add doc.

  Args:
    N: An optional `int` that is `>= 2`. Defaults to `3`.
    name: A name for the operation (optional).

  Returns:
    A list of `N` `Tensor` objects with type `int32`.
  """
  if N is None:
    N = 3
  N = _execute.make_int(N, "N")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "NIntsOutDefault", N=N, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("N", _op.get_attr("N"))
  else:
    _inputs_flat = []
    _attrs = ("N", N)
    _result = _execute.execute(b"NIntsOutDefault", N, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "NIntsOutDefault", _inputs_flat, _attrs, _result, name)
  return _result

_ops.RegisterShape("NIntsOutDefault")(None)


@tf_export('n_polymorphic_in')
def n_polymorphic_in(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A list of at least 2 `Tensor` objects with the same type.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  if not isinstance(a, (list, tuple)):
    raise TypeError(
        "Expected list for 'a' argument to "
        "'n_polymorphic_in' Op, not %r." % a)
  _attr_N = len(a)
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "NPolymorphicIn", a=a, name=name)
    return _op
  else:
    _attr_T, a = _execute.args_to_matching_eager(list(a), _ctx)
    _inputs_flat = list(a)
    _attrs = ("T", _attr_T, "N", _attr_N)
    _result = _execute.execute(b"NPolymorphicIn", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("NPolymorphicIn")(None)


@tf_export('n_polymorphic_out')
def n_polymorphic_out(T, N, name=None):
  r"""TODO: add doc.

  Args:
    T: A `tf.DType`.
    N: An `int` that is `>= 2`.
    name: A name for the operation (optional).

  Returns:
    A list of `N` `Tensor` objects with type `T`.
  """
  T = _execute.make_type(T, "T")
  N = _execute.make_int(N, "N")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "NPolymorphicOut", T=T, N=N, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "N", _op.get_attr("N"))
  else:
    _inputs_flat = []
    _attrs = ("T", T, "N", N)
    _result = _execute.execute(b"NPolymorphicOut", N, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "NPolymorphicOut", _inputs_flat, _attrs, _result, name)
  return _result

_ops.RegisterShape("NPolymorphicOut")(None)


@tf_export('n_polymorphic_out_default')
def n_polymorphic_out_default(T=_dtypes.bool, N=2, name=None):
  r"""TODO: add doc.

  Args:
    T: An optional `tf.DType`. Defaults to `tf.bool`.
    N: An optional `int` that is `>= 2`. Defaults to `2`.
    name: A name for the operation (optional).

  Returns:
    A list of `N` `Tensor` objects with type `T`.
  """
  if T is None:
    T = _dtypes.bool
  T = _execute.make_type(T, "T")
  if N is None:
    N = 2
  N = _execute.make_int(N, "N")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "NPolymorphicOutDefault", T=T, N=N, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "N", _op.get_attr("N"))
  else:
    _inputs_flat = []
    _attrs = ("T", T, "N", N)
    _result = _execute.execute(b"NPolymorphicOutDefault", N,
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
  _execute.record_gradient(
      "NPolymorphicOutDefault", _inputs_flat, _attrs, _result, name)
  return _result

_ops.RegisterShape("NPolymorphicOutDefault")(None)


@tf_export('n_polymorphic_restrict_in')
def n_polymorphic_restrict_in(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A list of at least 2 `Tensor` objects with the same type in: `string`, `bool`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  if not isinstance(a, (list, tuple)):
    raise TypeError(
        "Expected list for 'a' argument to "
        "'n_polymorphic_restrict_in' Op, not %r." % a)
  _attr_N = len(a)
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "NPolymorphicRestrictIn", a=a, name=name)
    return _op
  else:
    _attr_T, a = _execute.args_to_matching_eager(list(a), _ctx)
    _inputs_flat = list(a)
    _attrs = ("T", _attr_T, "N", _attr_N)
    _result = _execute.execute(b"NPolymorphicRestrictIn", 0,
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
    _result = None
  return _result

_ops.RegisterShape("NPolymorphicRestrictIn")(None)


@tf_export('n_polymorphic_restrict_out')
def n_polymorphic_restrict_out(T, N, name=None):
  r"""TODO: add doc.

  Args:
    T: A `tf.DType` from: `tf.string, tf.bool`.
    N: An `int` that is `>= 2`.
    name: A name for the operation (optional).

  Returns:
    A list of `N` `Tensor` objects with type `T`.
  """
  T = _execute.make_type(T, "T")
  N = _execute.make_int(N, "N")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "NPolymorphicRestrictOut", T=T, N=N, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "N", _op.get_attr("N"))
  else:
    _inputs_flat = []
    _attrs = ("T", T, "N", N)
    _result = _execute.execute(b"NPolymorphicRestrictOut", N,
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
  _execute.record_gradient(
      "NPolymorphicRestrictOut", _inputs_flat, _attrs, _result, name)
  return _result

_ops.RegisterShape("NPolymorphicRestrictOut")(None)


@tf_export('none')
def none(name=None):
  r"""TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "None", name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = None
    _result = _execute.execute(b"None", 0, inputs=_inputs_flat, attrs=_attrs,
                               ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("None")(None)


@tf_export('old')
def old(name=None):
  r"""TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "Old", name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = None
    _result = _execute.execute(b"Old", 0, inputs=_inputs_flat, attrs=_attrs,
                               ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("Old")(None)


@tf_export('op_with_default_attr')
def op_with_default_attr(default_float=123, name=None):
  r"""TODO: add doc.

  Args:
    default_float: An optional `float`. Defaults to `123`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """
  if default_float is None:
    default_float = 123
  default_float = _execute.make_float(default_float, "default_float")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "OpWithDefaultAttr", default_float=default_float, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("default_float", _op.get_attr("default_float"))
  else:
    _inputs_flat = []
    _attrs = ("default_float", default_float)
    _result = _execute.execute(b"OpWithDefaultAttr", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "OpWithDefaultAttr", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("OpWithDefaultAttr")(None)


@tf_export('op_with_future_default_attr')
def op_with_future_default_attr(name=None):
  r"""TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "OpWithFutureDefaultAttr", name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = None
    _result = _execute.execute(b"OpWithFutureDefaultAttr", 0,
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
    _result = None
  return _result

_ops.RegisterShape("OpWithFutureDefaultAttr")(None)


@tf_export('out_t')
def out_t(T, name=None):
  r"""TODO: add doc.

  Args:
    T: A `tf.DType`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `T`.
  """
  T = _execute.make_type(T, "T")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "OutT", T=T, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"))
  else:
    _inputs_flat = []
    _attrs = ("T", T)
    _result = _execute.execute(b"OutT", 1, inputs=_inputs_flat, attrs=_attrs,
                               ctx=_ctx, name=name)
  _execute.record_gradient(
      "OutT", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("OutT")(None)


@tf_export('out_type_list')
def out_type_list(T, name=None):
  r"""TODO: add doc.

  Args:
    T: A list of `tf.DTypes`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `T`.
  """
  if not isinstance(T, (list, tuple)):
    raise TypeError(
        "Expected list for 'T' argument to "
        "'out_type_list' Op, not %r." % T)
  T = [_execute.make_type(_t, "T") for _t in T]
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "OutTypeList", T=T, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"))
  else:
    _inputs_flat = []
    _attrs = ("T", T)
    _result = _execute.execute(b"OutTypeList", len(T), inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "OutTypeList", _inputs_flat, _attrs, _result, name)
  return _result

_ops.RegisterShape("OutTypeList")(None)


@tf_export('out_type_list_restrict')
def out_type_list_restrict(t, name=None):
  r"""TODO: add doc.

  Args:
    t: A list of `tf.DTypes` from: `tf.string, tf.bool` that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `t`.
  """
  if not isinstance(t, (list, tuple)):
    raise TypeError(
        "Expected list for 't' argument to "
        "'out_type_list_restrict' Op, not %r." % t)
  t = [_execute.make_type(_t, "t") for _t in t]
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "OutTypeListRestrict", t=t, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("t", _op.get_attr("t"))
  else:
    _inputs_flat = []
    _attrs = ("t", t)
    _result = _execute.execute(b"OutTypeListRestrict", len(t),
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
  _execute.record_gradient(
      "OutTypeListRestrict", _inputs_flat, _attrs, _result, name)
  return _result

_ops.RegisterShape("OutTypeListRestrict")(None)


@tf_export('polymorphic')
def polymorphic(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A `Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `a`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "Polymorphic", a=a, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"))
  else:
    _attr_T, (a,) = _execute.args_to_matching_eager([a], _ctx)
    _inputs_flat = [a]
    _attrs = ("T", _attr_T)
    _result = _execute.execute(b"Polymorphic", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "Polymorphic", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("Polymorphic")(None)


@tf_export('polymorphic_default_out')
def polymorphic_default_out(T=_dtypes.string, name=None):
  r"""TODO: add doc.

  Args:
    T: An optional `tf.DType`. Defaults to `tf.string`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `T`.
  """
  if T is None:
    T = _dtypes.string
  T = _execute.make_type(T, "T")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "PolymorphicDefaultOut", T=T, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"))
  else:
    _inputs_flat = []
    _attrs = ("T", T)
    _result = _execute.execute(b"PolymorphicDefaultOut", 1,
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
  _execute.record_gradient(
      "PolymorphicDefaultOut", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("PolymorphicDefaultOut")(None)


@tf_export('polymorphic_out')
def polymorphic_out(T, name=None):
  r"""TODO: add doc.

  Args:
    T: A `tf.DType`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `T`.
  """
  T = _execute.make_type(T, "T")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "PolymorphicOut", T=T, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"))
  else:
    _inputs_flat = []
    _attrs = ("T", T)
    _result = _execute.execute(b"PolymorphicOut", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "PolymorphicOut", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("PolymorphicOut")(None)


@tf_export('ref_in')
def ref_in(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A mutable `Tensor`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "RefIn", a=a, name=name)
    return _op
  else:
    raise RuntimeError(
        "ref_in op does not support eager execution. Arg 'a'' is a ref.")
    _result = None
  return _result

_ops.RegisterShape("RefIn")(None)


@tf_export('ref_input_float_input')
def ref_input_float_input(a, b, name=None):
  r"""TODO: add doc.

  Args:
    a: A `Tensor` of type mutable `float32`.
    b: A `Tensor` of type `float32`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "RefInputFloatInput", a=a, b=b, name=name)
    return _op
  else:
    raise RuntimeError(
        "ref_input_float_input op does not support eager execution. Arg 'a'' is a ref.")
    _result = None
  return _result

_ops.RegisterShape("RefInputFloatInput")(None)


@tf_export('ref_input_float_input_int_output')
def ref_input_float_input_int_output(a, b, name=None):
  r"""TODO: add doc.

  Args:
    a: A `Tensor` of type mutable `float32`.
    b: A `Tensor` of type `float32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "RefInputFloatInputIntOutput", a=a, b=b, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    raise RuntimeError(
        "ref_input_float_input_int_output op does not support eager execution. Arg 'a'' is a ref.")
  _execute.record_gradient(
      "RefInputFloatInputIntOutput", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("RefInputFloatInputIntOutput")(None)


@tf_export('ref_input_int_input')
def ref_input_int_input(a, b, name=None):
  r"""TODO: add doc.

  Args:
    a: A `Tensor` of type mutable `int32`.
    b: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "RefInputIntInput", a=a, b=b, name=name)
    return _op
  else:
    raise RuntimeError(
        "ref_input_int_input op does not support eager execution. Arg 'a'' is a ref.")
    _result = None
  return _result

_ops.RegisterShape("RefInputIntInput")(None)


@tf_export('ref_out')
def ref_out(T, name=None):
  r"""TODO: add doc.

  Args:
    T: A `tf.DType`.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor` of type `T`.
  """
  T = _execute.make_type(T, "T")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "RefOut", T=T, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"))
  else:
    raise RuntimeError(
        "ref_out op does not support eager execution. Arg 'a'' is a ref.")
  _execute.record_gradient(
      "RefOut", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("RefOut")(None)


@tf_export('ref_output')
def ref_output(name=None):
  r"""TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type mutable `int32`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "RefOutput", name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    raise RuntimeError(
        "ref_output op does not support eager execution. Arg 'a'' is a ref.")
  _execute.record_gradient(
      "RefOutput", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("RefOutput")(None)


_ref_output_float_output_outputs = ["a", "b"]
_RefOutputFloatOutputOutput = _collections.namedtuple(
    "RefOutputFloatOutput", _ref_output_float_output_outputs)


@tf_export('ref_output_float_output')
def ref_output_float_output(name=None):
  r"""TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (a, b).

    a: A `Tensor` of type mutable `float32`.
    b: A `Tensor` of type `float32`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "RefOutputFloatOutput", name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    raise RuntimeError(
        "ref_output_float_output op does not support eager execution. Arg 'a'' is a ref.")
  _execute.record_gradient(
      "RefOutputFloatOutput", _inputs_flat, _attrs, _result, name)
  _result = _RefOutputFloatOutputOutput._make(_result)
  return _result

_ops.RegisterShape("RefOutputFloatOutput")(None)


@tf_export('requires_older_graph_version')
def requires_older_graph_version(name=None):
  r"""TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "RequiresOlderGraphVersion", name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    _inputs_flat = []
    _attrs = None
    _result = _execute.execute(b"RequiresOlderGraphVersion", 1,
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
  _execute.record_gradient(
      "RequiresOlderGraphVersion", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("RequiresOlderGraphVersion")(None)


@tf_export('reserved_attr')
def reserved_attr(range, name=None):
  r"""TODO: add doc.

  Args:
    range: An `int`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  range = _execute.make_int(range, "range")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ReservedAttr", range=range, name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = ("range", range)
    _result = _execute.execute(b"ReservedAttr", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("ReservedAttr")(None)


@tf_export('reserved_input')
def reserved_input(input, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ReservedInput", input=input, name=name)
    return _op
  else:
    input = _ops.convert_to_tensor(input, _dtypes.int32)
    _inputs_flat = [input]
    _attrs = None
    _result = _execute.execute(b"ReservedInput", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("ReservedInput")(None)


@tf_export('resource_create_op')
def resource_create_op(resource, name=None):
  r"""TODO: add doc.

  Args:
    resource: A `Tensor` of type `resource`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ResourceCreateOp", resource=resource, name=name)
    return _op
  else:
    resource = _ops.convert_to_tensor(resource, _dtypes.resource)
    _inputs_flat = [resource]
    _attrs = None
    _result = _execute.execute(b"ResourceCreateOp", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("ResourceCreateOp")(None)


@tf_export('resource_initialized_op')
def resource_initialized_op(resource, name=None):
  r"""TODO: add doc.

  Args:
    resource: A `Tensor` of type `resource`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ResourceInitializedOp", resource=resource, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    resource = _ops.convert_to_tensor(resource, _dtypes.resource)
    _inputs_flat = [resource]
    _attrs = None
    _result = _execute.execute(b"ResourceInitializedOp", 1,
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
  _execute.record_gradient(
      "ResourceInitializedOp", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("ResourceInitializedOp")(None)


@tf_export('resource_using_op')
def resource_using_op(resource, name=None):
  r"""TODO: add doc.

  Args:
    resource: A `Tensor` of type `resource`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ResourceUsingOp", resource=resource, name=name)
    return _op
  else:
    resource = _ops.convert_to_tensor(resource, _dtypes.resource)
    _inputs_flat = [resource]
    _attrs = None
    _result = _execute.execute(b"ResourceUsingOp", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("ResourceUsingOp")(None)


@tf_export('restrict')
def restrict(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A `Tensor`. Must be one of the following types: `string`, `bool`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `a`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "Restrict", a=a, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"))
  else:
    _attr_T, (a,) = _execute.args_to_matching_eager([a], _ctx)
    _inputs_flat = [a]
    _attrs = ("T", _attr_T)
    _result = _execute.execute(b"Restrict", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "Restrict", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("Restrict")(None)


@tf_export('simple')
def simple(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "Simple", a=a, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    a = _ops.convert_to_tensor(a, _dtypes.int32)
    _inputs_flat = [a]
    _attrs = None
    _result = _execute.execute(b"Simple", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "Simple", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("Simple")(None)


@tf_export('simple_struct')
def simple_struct(n_a, name=None):
  r"""TODO: add doc.

  Args:
    n_a: An `int` that is `>= 0`.
    name: A name for the operation (optional).

  Returns:
    A list of `n_a` `Tensor` objects with type `int32`.
  """
  n_a = _execute.make_int(n_a, "n_a")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "SimpleStruct", n_a=n_a, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("n_a", _op.get_attr("n_a"))
  else:
    _inputs_flat = []
    _attrs = ("n_a", n_a)
    _result = _execute.execute(b"SimpleStruct", n_a, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "SimpleStruct", _inputs_flat, _attrs, _result, name)
  return _result

_ops.RegisterShape("SimpleStruct")(None)


@tf_export('string_list_attr')
def string_list_attr(a, b, name=None):
  r"""TODO: add doc.

  Args:
    a: A list of `strings`.
    b: A `string`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  if not isinstance(a, (list, tuple)):
    raise TypeError(
        "Expected list for 'a' argument to "
        "'string_list_attr' Op, not %r." % a)
  a = [_execute.make_str(_s, "a") for _s in a]
  b = _execute.make_str(b, "b")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "StringListAttr", a=a, b=b, name=name)
    return _op
  else:
    _inputs_flat = []
    _attrs = ("a", a, "b", b)
    _result = _execute.execute(b"StringListAttr", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("StringListAttr")(None)


@tf_export('stub_resource_handle_op')
def stub_resource_handle_op(container="", shared_name="", name=None):
  r"""Creates a handle to a StubResource

  Args:
    container: An optional `string`. Defaults to `""`.
    shared_name: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  """
  if container is None:
    container = ""
  container = _execute.make_str(container, "container")
  if shared_name is None:
    shared_name = ""
  shared_name = _execute.make_str(shared_name, "shared_name")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "StubResourceHandleOp", container=container, shared_name=shared_name,
        name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("container", _op.get_attr("container"), "shared_name",
              _op.get_attr("shared_name"))
  else:
    _inputs_flat = []
    _attrs = ("container", container, "shared_name", shared_name)
    _result = _execute.execute(b"StubResourceHandleOp", 1,
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
  _execute.record_gradient(
      "StubResourceHandleOp", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("StubResourceHandleOp")(None)


_test_string_output_outputs = ["output1", "output2"]
_TestStringOutputOutput = _collections.namedtuple(
    "TestStringOutput", _test_string_output_outputs)


@tf_export('test_string_output')
def test_string_output(input, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor` of type `float32`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output1, output2).

    output1: A `Tensor` of type `float32`.
    output2: A `Tensor` of type `string`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "TestStringOutput", input=input, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    input = _ops.convert_to_tensor(input, _dtypes.float32)
    _inputs_flat = [input]
    _attrs = None
    _result = _execute.execute(b"TestStringOutput", 2, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "TestStringOutput", _inputs_flat, _attrs, _result, name)
  _result = _TestStringOutputOutput._make(_result)
  return _result

_ops.RegisterShape("TestStringOutput")(None)


@tf_export('two_float_inputs')
def two_float_inputs(a, b, name=None):
  r"""TODO: add doc.

  Args:
    a: A `Tensor` of type `float32`.
    b: A `Tensor` of type `float32`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "TwoFloatInputs", a=a, b=b, name=name)
    return _op
  else:
    a = _ops.convert_to_tensor(a, _dtypes.float32)
    b = _ops.convert_to_tensor(b, _dtypes.float32)
    _inputs_flat = [a, b]
    _attrs = None
    _result = _execute.execute(b"TwoFloatInputs", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("TwoFloatInputs")(None)


@tf_export('two_float_inputs_float_output')
def two_float_inputs_float_output(a, b, name=None):
  r"""TODO: add doc.

  Args:
    a: A `Tensor` of type `float32`.
    b: A `Tensor` of type `float32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "TwoFloatInputsFloatOutput", a=a, b=b, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    a = _ops.convert_to_tensor(a, _dtypes.float32)
    b = _ops.convert_to_tensor(b, _dtypes.float32)
    _inputs_flat = [a, b]
    _attrs = None
    _result = _execute.execute(b"TwoFloatInputsFloatOutput", 1,
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
  _execute.record_gradient(
      "TwoFloatInputsFloatOutput", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("TwoFloatInputsFloatOutput")(None)


@tf_export('two_float_inputs_int_output')
def two_float_inputs_int_output(a, b, name=None):
  r"""TODO: add doc.

  Args:
    a: A `Tensor` of type `float32`.
    b: A `Tensor` of type `float32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "TwoFloatInputsIntOutput", a=a, b=b, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    a = _ops.convert_to_tensor(a, _dtypes.float32)
    b = _ops.convert_to_tensor(b, _dtypes.float32)
    _inputs_flat = [a, b]
    _attrs = None
    _result = _execute.execute(b"TwoFloatInputsIntOutput", 1,
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
  _execute.record_gradient(
      "TwoFloatInputsIntOutput", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("TwoFloatInputsIntOutput")(None)


_two_float_outputs_outputs = ["a", "b"]
_TwoFloatOutputsOutput = _collections.namedtuple(
    "TwoFloatOutputs", _two_float_outputs_outputs)


@tf_export('two_float_outputs')
def two_float_outputs(name=None):
  r"""TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (a, b).

    a: A `Tensor` of type `float32`.
    b: A `Tensor` of type `float32`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "TwoFloatOutputs", name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    _inputs_flat = []
    _attrs = None
    _result = _execute.execute(b"TwoFloatOutputs", 2, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "TwoFloatOutputs", _inputs_flat, _attrs, _result, name)
  _result = _TwoFloatOutputsOutput._make(_result)
  return _result

_ops.RegisterShape("TwoFloatOutputs")(None)


@tf_export('two_int_inputs')
def two_int_inputs(a, b, name=None):
  r"""TODO: add doc.

  Args:
    a: A `Tensor` of type `int32`.
    b: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "TwoIntInputs", a=a, b=b, name=name)
    return _op
  else:
    a = _ops.convert_to_tensor(a, _dtypes.int32)
    b = _ops.convert_to_tensor(b, _dtypes.int32)
    _inputs_flat = [a, b]
    _attrs = None
    _result = _execute.execute(b"TwoIntInputs", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("TwoIntInputs")(None)


_two_int_outputs_outputs = ["a", "b"]
_TwoIntOutputsOutput = _collections.namedtuple(
    "TwoIntOutputs", _two_int_outputs_outputs)


@tf_export('two_int_outputs')
def two_int_outputs(name=None):
  r"""TODO: add doc.

  Args:
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (a, b).

    a: A `Tensor` of type `int32`.
    b: A `Tensor` of type `int32`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "TwoIntOutputs", name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    _inputs_flat = []
    _attrs = None
    _result = _execute.execute(b"TwoIntOutputs", 2, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "TwoIntOutputs", _inputs_flat, _attrs, _result, name)
  _result = _TwoIntOutputsOutput._make(_result)
  return _result

_ops.RegisterShape("TwoIntOutputs")(None)


@tf_export('two_refs_in')
def two_refs_in(a, b, name=None):
  r"""TODO: add doc.

  Args:
    a: A mutable `Tensor`.
    b: A mutable `Tensor`. Must have the same type as `a`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "TwoRefsIn", a=a, b=b, name=name)
    return _op
  else:
    raise RuntimeError(
        "two_refs_in op does not support eager execution. Arg 'b'' is a ref.")
    _result = None
  return _result

_ops.RegisterShape("TwoRefsIn")(None)


@tf_export('type_list')
def type_list(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A list of `Tensor` objects.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "TypeList", a=a, name=name)
    return _op
  else:
    _attr_T, a = _execute.convert_to_mixed_eager_tensors(a, _ctx)
    _inputs_flat = list(a)
    _attrs = ("T", _attr_T)
    _result = _execute.execute(b"TypeList", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("TypeList")(None)


@tf_export('type_list_restrict')
def type_list_restrict(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A list of `Tensor` objects with types from: `string`, `bool`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "TypeListRestrict", a=a, name=name)
    return _op
  else:
    _attr_T, a = _execute.convert_to_mixed_eager_tensors(a, _ctx)
    _inputs_flat = list(a)
    _attrs = ("T", _attr_T)
    _result = _execute.execute(b"TypeListRestrict", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("TypeListRestrict")(None)


@tf_export('type_list_twice')
def type_list_twice(a, b, name=None):
  r"""TODO: add doc.

  Args:
    a: A list of `Tensor` objects.
    b: A list of `Tensor` objects. Must have the same type as `a`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "TypeListTwice", a=a, b=b, name=name)
    return _op
  else:
    _attr_T, (a, b) = _execute.args_to_mixed_eager_tensors((a, b), _ctx)
    _inputs_flat = list(a) + list(b)
    _attrs = ("T", _attr_T)
    _result = _execute.execute(b"TypeListTwice", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
    _result = None
  return _result

_ops.RegisterShape("TypeListTwice")(None)


@tf_export('unary')
def unary(a, name=None):
  r"""TODO: add doc.

  Args:
    a: A `Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `a`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "Unary", a=a, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"))
  else:
    _attr_T, (a,) = _execute.args_to_matching_eager([a], _ctx)
    _inputs_flat = [a]
    _attrs = ("T", _attr_T)
    _result = _execute.execute(b"Unary", 1, inputs=_inputs_flat, attrs=_attrs,
                               ctx=_ctx, name=name)
  _execute.record_gradient(
      "Unary", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("Unary")(None)

def _InitOpDefLibrary(op_list_proto_bytes):
  op_list = _op_def_pb2.OpList()
  op_list.ParseFromString(op_list_proto_bytes)
  _op_def_registry.register_op_list(op_list)
  op_def_lib = _op_def_library.OpDefLibrary()
  op_def_lib.add_op_list(op_list)
  return op_def_lib
# op {
#   name: "A"
#   output_arg {
#     name: "out"
#     type: DT_FLOAT
#   }
# }
# op {
#   name: "Attr"
#   attr {
#     name: "a"
#     type: "int"
#   }
# }
# op {
#   name: "AttrBool"
#   attr {
#     name: "a"
#     type: "bool"
#   }
# }
# op {
#   name: "AttrBoolList"
#   attr {
#     name: "a"
#     type: "list(bool)"
#   }
# }
# op {
#   name: "AttrDefault"
#   attr {
#     name: "a"
#     type: "string"
#     default_value {
#       s: "banana"
#     }
#   }
# }
# op {
#   name: "AttrEmptyListDefault"
#   attr {
#     name: "a"
#     type: "list(float)"
#     default_value {
#       list {
#       }
#     }
#   }
# }
# op {
#   name: "AttrEnum"
#   attr {
#     name: "a"
#     type: "string"
#     allowed_values {
#       list {
#         s: "apples"
#         s: "oranges"
#       }
#     }
#   }
# }
# op {
#   name: "AttrEnumList"
#   attr {
#     name: "a"
#     type: "list(string)"
#     allowed_values {
#       list {
#         s: "apples"
#         s: "oranges"
#       }
#     }
#   }
# }
# op {
#   name: "AttrFloat"
#   attr {
#     name: "a"
#     type: "float"
#   }
# }
# op {
#   name: "AttrListDefault"
#   attr {
#     name: "a"
#     type: "list(int)"
#     default_value {
#       list {
#         i: 5
#         i: 15
#       }
#     }
#   }
# }
# op {
#   name: "AttrListMin"
#   attr {
#     name: "a"
#     type: "list(int)"
#     has_minimum: true
#     minimum: 2
#   }
# }
# op {
#   name: "AttrListTypeDefault"
#   input_arg {
#     name: "a"
#     type_attr: "T"
#     number_attr: "N"
#   }
#   input_arg {
#     name: "b"
#     type_attr: "T"
#     number_attr: "N"
#   }
#   attr {
#     name: "T"
#     type: "type"
#     default_value {
#       type: DT_INT32
#     }
#   }
#   attr {
#     name: "N"
#     type: "int"
#     has_minimum: true
#     minimum: 1
#   }
# }
# op {
#   name: "AttrMin"
#   attr {
#     name: "a"
#     type: "int"
#     has_minimum: true
#     minimum: 5
#   }
# }
# op {
#   name: "AttrPartialShape"
#   attr {
#     name: "a"
#     type: "shape"
#   }
# }
# op {
#   name: "AttrPartialShapeList"
#   attr {
#     name: "a"
#     type: "list(shape)"
#   }
# }
# op {
#   name: "AttrShape"
#   attr {
#     name: "a"
#     type: "shape"
#   }
# }
# op {
#   name: "AttrShapeList"
#   attr {
#     name: "a"
#     type: "list(shape)"
#   }
# }
# op {
#   name: "AttrTypeDefault"
#   input_arg {
#     name: "a"
#     type_attr: "T"
#   }
#   attr {
#     name: "T"
#     type: "type"
#     default_value {
#       type: DT_INT32
#     }
#   }
# }
# op {
#   name: "B"
#   output_arg {
#     name: "out"
#     type: DT_FLOAT
#   }
# }
# op {
#   name: "Binary"
#   input_arg {
#     name: "a"
#     type_attr: "T"
#   }
#   input_arg {
#     name: "b"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "out"
#     type_attr: "T"
#   }
#   attr {
#     name: "T"
#     type: "type"
#   }
# }
# op {
#   name: "ComplexStruct"
#   output_arg {
#     name: "a"
#     type: DT_INT32
#     number_attr: "n_a"
#   }
#   output_arg {
#     name: "b"
#     type: DT_INT64
#     number_attr: "n_b"
#   }
#   output_arg {
#     name: "c"
#     type_list_attr: "t_c"
#   }
#   attr {
#     name: "n_a"
#     type: "int"
#     has_minimum: true
#   }
#   attr {
#     name: "n_b"
#     type: "int"
#     has_minimum: true
#   }
#   attr {
#     name: "t_c"
#     type: "list(type)"
#     has_minimum: true
#   }
# }
# op {
#   name: "CopyOp"
#   input_arg {
#     name: "a"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "b"
#     type_attr: "T"
#   }
#   attr {
#     name: "T"
#     type: "type"
#   }
# }
# op {
#   name: "DefaultAttrs"
#   attr {
#     name: "string_val"
#     type: "string"
#     default_value {
#       s: "abc"
#     }
#   }
#   attr {
#     name: "string_list_val"
#     type: "list(string)"
#     default_value {
#       list {
#         s: "abc"
#         s: ""
#       }
#     }
#   }
#   attr {
#     name: "int_val"
#     type: "int"
#     default_value {
#       i: 123
#     }
#   }
#   attr {
#     name: "int_list_val"
#     type: "list(int)"
#     default_value {
#       list {
#         i: 1
#         i: 2
#         i: 3
#       }
#     }
#   }
#   attr {
#     name: "float_val"
#     type: "float"
#     default_value {
#       f: 10
#     }
#   }
#   attr {
#     name: "float_list_val"
#     type: "list(float)"
#     default_value {
#       list {
#         f: 10
#       }
#     }
#   }
#   attr {
#     name: "bool_val"
#     type: "bool"
#     default_value {
#       b: true
#     }
#   }
#   attr {
#     name: "bool_list_val"
#     type: "list(bool)"
#     default_value {
#       list {
#         b: true
#         b: false
#       }
#     }
#   }
#   attr {
#     name: "type_val"
#     type: "type"
#     default_value {
#       type: DT_INT32
#     }
#   }
#   attr {
#     name: "type_list_val"
#     type: "list(type)"
#     default_value {
#       list {
#         type: DT_INT32
#         type: DT_FLOAT
#       }
#     }
#   }
#   attr {
#     name: "shape_val"
#     type: "shape"
#     default_value {
#       shape {
#         dim {
#           size: 2
#         }
#         dim {
#           size: 1
#         }
#       }
#     }
#   }
#   attr {
#     name: "shape_list_val"
#     type: "list(shape)"
#     default_value {
#       list {
#         shape {
#         }
#         shape {
#           dim {
#             size: 1
#           }
#         }
#       }
#     }
#   }
#   attr {
#     name: "tensor_val"
#     type: "tensor"
#     default_value {
#       tensor {
#         dtype: DT_INT32
#         tensor_shape {
#         }
#         int_val: 1
#       }
#     }
#   }
#   attr {
#     name: "tensor_list_val"
#     type: "list(tensor)"
#     default_value {
#       list {
#         tensor {
#           dtype: DT_INT32
#           tensor_shape {
#           }
#           int_val: 1
#         }
#       }
#     }
#   }
# }
# op {
#   name: "FiveFloatOutputs"
#   output_arg {
#     name: "a"
#     type: DT_FLOAT
#   }
#   output_arg {
#     name: "b"
#     type: DT_FLOAT
#   }
#   output_arg {
#     name: "c"
#     type: DT_FLOAT
#   }
#   output_arg {
#     name: "d"
#     type: DT_FLOAT
#   }
#   output_arg {
#     name: "e"
#     type: DT_FLOAT
#   }
# }
# op {
#   name: "FloatInput"
#   input_arg {
#     name: "a"
#     type: DT_FLOAT
#   }
# }
# op {
#   name: "FloatOutput"
#   output_arg {
#     name: "a"
#     type: DT_FLOAT
#   }
# }
# op {
#   name: "FloatOutputStringOutput"
#   output_arg {
#     name: "a"
#     type: DT_FLOAT
#   }
#   output_arg {
#     name: "b"
#     type: DT_STRING
#   }
# }
# op {
#   name: "Foo1"
#   input_arg {
#     name: "a"
#     type: DT_FLOAT
#   }
#   input_arg {
#     name: "b"
#     type: DT_INT32
#   }
#   input_arg {
#     name: "c"
#     type: DT_INT32
#   }
#   output_arg {
#     name: "d"
#     type: DT_FLOAT
#   }
#   output_arg {
#     name: "e"
#     type: DT_INT32
#   }
# }
# op {
#   name: "Foo2"
#   input_arg {
#     name: "a"
#     type: DT_FLOAT
#   }
#   input_arg {
#     name: "b"
#     type: DT_STRING
#   }
#   input_arg {
#     name: "c"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "d"
#     type: DT_FLOAT
#   }
#   output_arg {
#     name: "e"
#     type: DT_INT32
#   }
# }
# op {
#   name: "Foo3"
#   input_arg {
#     name: "a"
#     type: DT_FLOAT
#   }
#   input_arg {
#     name: "b"
#     type: DT_STRING
#   }
#   input_arg {
#     name: "c"
#     type: DT_FLOAT
#   }
#   output_arg {
#     name: "d"
#     type: DT_FLOAT
#   }
#   output_arg {
#     name: "e"
#     type: DT_INT32
#   }
# }
# op {
#   name: "FuncAttr"
#   attr {
#     name: "f"
#     type: "func"
#   }
# }
# op {
#   name: "GraphDefVersion"
#   output_arg {
#     name: "version"
#     type: DT_INT32
#   }
#   is_stateful: true
# }
# op {
#   name: "InPolymorphicTwice"
#   input_arg {
#     name: "a"
#     type_attr: "T"
#     number_attr: "N"
#   }
#   input_arg {
#     name: "b"
#     type_attr: "T"
#     number_attr: "M"
#   }
#   attr {
#     name: "T"
#     type: "type"
#   }
#   attr {
#     name: "N"
#     type: "int"
#     has_minimum: true
#   }
#   attr {
#     name: "M"
#     type: "int"
#     has_minimum: true
#   }
# }
# op {
#   name: "Int64Output"
#   output_arg {
#     name: "out"
#     type: DT_INT64
#   }
# }
# op {
#   name: "IntAttr"
#   output_arg {
#     name: "out"
#     type: DT_INT64
#   }
#   attr {
#     name: "foo"
#     type: "int"
#     default_value {
#       i: 1
#     }
#   }
# }
# op {
#   name: "IntInput"
#   input_arg {
#     name: "a"
#     type: DT_INT32
#   }
# }
# op {
#   name: "IntInputFloatInput"
#   input_arg {
#     name: "a"
#     type: DT_INT32
#   }
#   input_arg {
#     name: "b"
#     type: DT_FLOAT
#   }
# }
# op {
#   name: "IntInputIntOutput"
#   input_arg {
#     name: "a"
#     type: DT_INT32
#   }
#   output_arg {
#     name: "b"
#     type: DT_INT32
#   }
# }
# op {
#   name: "IntOutput"
#   output_arg {
#     name: "a"
#     type: DT_INT32
#   }
# }
# op {
#   name: "IntOutputFloatOutput"
#   output_arg {
#     name: "a"
#     type: DT_INT32
#   }
#   output_arg {
#     name: "b"
#     type: DT_FLOAT
#   }
# }
# op {
#   name: "KernelLabel"
#   output_arg {
#     name: "result"
#     type: DT_STRING
#   }
# }
# op {
#   name: "KernelLabelRequired"
#   input_arg {
#     name: "input"
#     type: DT_INT32
#   }
#   output_arg {
#     name: "result"
#     type: DT_STRING
#   }
# }
# op {
#   name: "ListInput"
#   input_arg {
#     name: "a"
#     type_attr: "T"
#     number_attr: "N"
#   }
#   attr {
#     name: "N"
#     type: "int"
#     has_minimum: true
#     minimum: 1
#   }
#   attr {
#     name: "T"
#     type: "type"
#   }
# }
# op {
#   name: "ListOutput"
#   output_arg {
#     name: "a"
#     type_list_attr: "T"
#   }
#   attr {
#     name: "T"
#     type: "list(type)"
#     has_minimum: true
#     minimum: 1
#   }
# }
# op {
#   name: "MixedStruct"
#   output_arg {
#     name: "a"
#     type: DT_INT32
#     number_attr: "n_a"
#   }
#   output_arg {
#     name: "b"
#     type: DT_FLOAT
#   }
#   attr {
#     name: "n_a"
#     type: "int"
#     has_minimum: true
#   }
# }
# op {
#   name: "NInPolymorphicTwice"
#   input_arg {
#     name: "a"
#     type_attr: "T"
#     number_attr: "N"
#   }
#   input_arg {
#     name: "b"
#     type_attr: "T"
#     number_attr: "N"
#   }
#   attr {
#     name: "T"
#     type: "type"
#   }
#   attr {
#     name: "N"
#     type: "int"
#     has_minimum: true
#   }
# }
# op {
#   name: "NInTwice"
#   input_arg {
#     name: "a"
#     type: DT_INT32
#     number_attr: "N"
#   }
#   input_arg {
#     name: "b"
#     type: DT_STRING
#     number_attr: "N"
#   }
#   attr {
#     name: "N"
#     type: "int"
#     has_minimum: true
#   }
# }
# op {
#   name: "NInTwoTypeVariables"
#   input_arg {
#     name: "a"
#     type_attr: "S"
#     number_attr: "N"
#   }
#   input_arg {
#     name: "b"
#     type_attr: "T"
#     number_attr: "N"
#   }
#   attr {
#     name: "S"
#     type: "type"
#   }
#   attr {
#     name: "T"
#     type: "type"
#   }
#   attr {
#     name: "N"
#     type: "int"
#     has_minimum: true
#   }
# }
# op {
#   name: "NIntsIn"
#   input_arg {
#     name: "a"
#     type: DT_INT32
#     number_attr: "N"
#   }
#   attr {
#     name: "N"
#     type: "int"
#     has_minimum: true
#     minimum: 2
#   }
# }
# op {
#   name: "NIntsOut"
#   output_arg {
#     name: "a"
#     type: DT_INT32
#     number_attr: "N"
#   }
#   attr {
#     name: "N"
#     type: "int"
#     has_minimum: true
#     minimum: 2
#   }
# }
# op {
#   name: "NIntsOutDefault"
#   output_arg {
#     name: "a"
#     type: DT_INT32
#     number_attr: "N"
#   }
#   attr {
#     name: "N"
#     type: "int"
#     default_value {
#       i: 3
#     }
#     has_minimum: true
#     minimum: 2
#   }
# }
# op {
#   name: "NPolymorphicIn"
#   input_arg {
#     name: "a"
#     type_attr: "T"
#     number_attr: "N"
#   }
#   attr {
#     name: "T"
#     type: "type"
#   }
#   attr {
#     name: "N"
#     type: "int"
#     has_minimum: true
#     minimum: 2
#   }
# }
# op {
#   name: "NPolymorphicOut"
#   output_arg {
#     name: "a"
#     type_attr: "T"
#     number_attr: "N"
#   }
#   attr {
#     name: "T"
#     type: "type"
#   }
#   attr {
#     name: "N"
#     type: "int"
#     has_minimum: true
#     minimum: 2
#   }
# }
# op {
#   name: "NPolymorphicOutDefault"
#   output_arg {
#     name: "a"
#     type_attr: "T"
#     number_attr: "N"
#   }
#   attr {
#     name: "T"
#     type: "type"
#     default_value {
#       type: DT_BOOL
#     }
#   }
#   attr {
#     name: "N"
#     type: "int"
#     default_value {
#       i: 2
#     }
#     has_minimum: true
#     minimum: 2
#   }
# }
# op {
#   name: "NPolymorphicRestrictIn"
#   input_arg {
#     name: "a"
#     type_attr: "T"
#     number_attr: "N"
#   }
#   attr {
#     name: "T"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_STRING
#         type: DT_BOOL
#       }
#     }
#   }
#   attr {
#     name: "N"
#     type: "int"
#     has_minimum: true
#     minimum: 2
#   }
# }
# op {
#   name: "NPolymorphicRestrictOut"
#   output_arg {
#     name: "a"
#     type_attr: "T"
#     number_attr: "N"
#   }
#   attr {
#     name: "T"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_STRING
#         type: DT_BOOL
#       }
#     }
#   }
#   attr {
#     name: "N"
#     type: "int"
#     has_minimum: true
#     minimum: 2
#   }
# }
# op {
#   name: "None"
# }
# op {
#   name: "Old"
#   deprecation {
#     version: 8
#     explanation: "For reasons"
#   }
# }
# op {
#   name: "OpWithDefaultAttr"
#   output_arg {
#     name: "a"
#     type: DT_INT32
#   }
#   attr {
#     name: "default_float"
#     type: "float"
#     default_value {
#       f: 123
#     }
#   }
# }
# op {
#   name: "OpWithFutureDefaultAttr"
# }
# op {
#   name: "OutT"
#   output_arg {
#     name: "a"
#     type_attr: "T"
#   }
#   attr {
#     name: "T"
#     type: "type"
#   }
# }
# op {
#   name: "OutTypeList"
#   output_arg {
#     name: "out"
#     type_list_attr: "T"
#   }
#   attr {
#     name: "T"
#     type: "list(type)"
#     has_minimum: true
#   }
# }
# op {
#   name: "OutTypeListRestrict"
#   output_arg {
#     name: "out"
#     type_list_attr: "t"
#   }
#   attr {
#     name: "t"
#     type: "list(type)"
#     has_minimum: true
#     minimum: 1
#     allowed_values {
#       list {
#         type: DT_STRING
#         type: DT_BOOL
#       }
#     }
#   }
# }
# op {
#   name: "Polymorphic"
#   input_arg {
#     name: "a"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "out"
#     type_attr: "T"
#   }
#   attr {
#     name: "T"
#     type: "type"
#   }
# }
# op {
#   name: "PolymorphicDefaultOut"
#   output_arg {
#     name: "out"
#     type_attr: "T"
#   }
#   attr {
#     name: "T"
#     type: "type"
#     default_value {
#       type: DT_STRING
#     }
#   }
# }
# op {
#   name: "PolymorphicOut"
#   output_arg {
#     name: "out"
#     type_attr: "T"
#   }
#   attr {
#     name: "T"
#     type: "type"
#   }
# }
# op {
#   name: "RefIn"
#   input_arg {
#     name: "a"
#     type_attr: "T"
#     is_ref: true
#   }
#   attr {
#     name: "T"
#     type: "type"
#   }
# }
# op {
#   name: "RefInputFloatInput"
#   input_arg {
#     name: "a"
#     type: DT_FLOAT
#     is_ref: true
#   }
#   input_arg {
#     name: "b"
#     type: DT_FLOAT
#   }
# }
# op {
#   name: "RefInputFloatInputIntOutput"
#   input_arg {
#     name: "a"
#     type: DT_FLOAT
#     is_ref: true
#   }
#   input_arg {
#     name: "b"
#     type: DT_FLOAT
#   }
#   output_arg {
#     name: "c"
#     type: DT_INT32
#   }
# }
# op {
#   name: "RefInputIntInput"
#   input_arg {
#     name: "a"
#     type: DT_INT32
#     is_ref: true
#   }
#   input_arg {
#     name: "b"
#     type: DT_INT32
#   }
# }
# op {
#   name: "RefOut"
#   output_arg {
#     name: "a"
#     type_attr: "T"
#     is_ref: true
#   }
#   attr {
#     name: "T"
#     type: "type"
#   }
# }
# op {
#   name: "RefOutput"
#   output_arg {
#     name: "a"
#     type: DT_INT32
#     is_ref: true
#   }
# }
# op {
#   name: "RefOutputFloatOutput"
#   output_arg {
#     name: "a"
#     type: DT_FLOAT
#     is_ref: true
#   }
#   output_arg {
#     name: "b"
#     type: DT_FLOAT
#   }
# }
# op {
#   name: "RequiresOlderGraphVersion"
#   output_arg {
#     name: "version"
#     type: DT_INT32
#   }
#   is_stateful: true
# }
# op {
#   name: "ReservedAttr"
#   attr {
#     name: "range"
#     type: "int"
#   }
# }
# op {
#   name: "ReservedInput"
#   input_arg {
#     name: "input"
#     type: DT_INT32
#   }
# }
# op {
#   name: "ResourceCreateOp"
#   input_arg {
#     name: "resource"
#     type: DT_RESOURCE
#   }
#   is_stateful: true
# }
# op {
#   name: "ResourceInitializedOp"
#   input_arg {
#     name: "resource"
#     type: DT_RESOURCE
#   }
#   output_arg {
#     name: "initialized"
#     type: DT_BOOL
#   }
#   is_stateful: true
# }
# op {
#   name: "ResourceUsingOp"
#   input_arg {
#     name: "resource"
#     type: DT_RESOURCE
#   }
#   is_stateful: true
# }
# op {
#   name: "Restrict"
#   input_arg {
#     name: "a"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "out"
#     type_attr: "T"
#   }
#   attr {
#     name: "T"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_STRING
#         type: DT_BOOL
#       }
#     }
#   }
# }
# op {
#   name: "Simple"
#   input_arg {
#     name: "a"
#     type: DT_INT32
#   }
#   output_arg {
#     name: "out"
#     type: DT_FLOAT
#   }
# }
# op {
#   name: "SimpleStruct"
#   output_arg {
#     name: "a"
#     type: DT_INT32
#     number_attr: "n_a"
#   }
#   attr {
#     name: "n_a"
#     type: "int"
#     has_minimum: true
#   }
# }
# op {
#   name: "StringListAttr"
#   attr {
#     name: "a"
#     type: "list(string)"
#   }
#   attr {
#     name: "b"
#     type: "string"
#   }
# }
# op {
#   name: "StubResourceHandleOp"
#   output_arg {
#     name: "resource"
#     type: DT_RESOURCE
#   }
#   attr {
#     name: "container"
#     type: "string"
#     default_value {
#       s: ""
#     }
#   }
#   attr {
#     name: "shared_name"
#     type: "string"
#     default_value {
#       s: ""
#     }
#   }
#   is_stateful: true
# }
# op {
#   name: "TestStringOutput"
#   input_arg {
#     name: "input"
#     type: DT_FLOAT
#   }
#   output_arg {
#     name: "output1"
#     type: DT_FLOAT
#   }
#   output_arg {
#     name: "output2"
#     type: DT_STRING
#   }
# }
# op {
#   name: "TwoFloatInputs"
#   input_arg {
#     name: "a"
#     type: DT_FLOAT
#   }
#   input_arg {
#     name: "b"
#     type: DT_FLOAT
#   }
# }
# op {
#   name: "TwoFloatInputsFloatOutput"
#   input_arg {
#     name: "a"
#     type: DT_FLOAT
#   }
#   input_arg {
#     name: "b"
#     type: DT_FLOAT
#   }
#   output_arg {
#     name: "c"
#     type: DT_FLOAT
#   }
# }
# op {
#   name: "TwoFloatInputsIntOutput"
#   input_arg {
#     name: "a"
#     type: DT_FLOAT
#   }
#   input_arg {
#     name: "b"
#     type: DT_FLOAT
#   }
#   output_arg {
#     name: "c"
#     type: DT_INT32
#   }
# }
# op {
#   name: "TwoFloatOutputs"
#   output_arg {
#     name: "a"
#     type: DT_FLOAT
#   }
#   output_arg {
#     name: "b"
#     type: DT_FLOAT
#   }
# }
# op {
#   name: "TwoIntInputs"
#   input_arg {
#     name: "a"
#     type: DT_INT32
#   }
#   input_arg {
#     name: "b"
#     type: DT_INT32
#   }
# }
# op {
#   name: "TwoIntOutputs"
#   output_arg {
#     name: "a"
#     type: DT_INT32
#   }
#   output_arg {
#     name: "b"
#     type: DT_INT32
#   }
# }
# op {
#   name: "TwoRefsIn"
#   input_arg {
#     name: "a"
#     type_attr: "T"
#     is_ref: true
#   }
#   input_arg {
#     name: "b"
#     type_attr: "T"
#     is_ref: true
#   }
#   attr {
#     name: "T"
#     type: "type"
#   }
# }
# op {
#   name: "TypeList"
#   input_arg {
#     name: "a"
#     type_list_attr: "T"
#   }
#   attr {
#     name: "T"
#     type: "list(type)"
#     has_minimum: true
#   }
# }
# op {
#   name: "TypeListRestrict"
#   input_arg {
#     name: "a"
#     type_list_attr: "T"
#   }
#   attr {
#     name: "T"
#     type: "list(type)"
#     has_minimum: true
#     minimum: 1
#     allowed_values {
#       list {
#         type: DT_STRING
#         type: DT_BOOL
#       }
#     }
#   }
# }
# op {
#   name: "TypeListTwice"
#   input_arg {
#     name: "a"
#     type_list_attr: "T"
#   }
#   input_arg {
#     name: "b"
#     type_list_attr: "T"
#   }
#   attr {
#     name: "T"
#     type: "list(type)"
#     has_minimum: true
#   }
# }
# op {
#   name: "Unary"
#   input_arg {
#     name: "a"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "b"
#     type_attr: "T"
#   }
#   attr {
#     name: "T"
#     type: "type"
#   }
# }
_op_def_lib = _InitOpDefLibrary(b"\n\014\n\001A\032\007\n\003out\030\001\n\020\n\004Attr\"\010\n\001a\022\003int\n\025\n\010AttrBool\"\t\n\001a\022\004bool\n\037\n\014AttrBoolList\"\017\n\001a\022\nlist(bool)\n$\n\013AttrDefault\"\025\n\001a\022\006string\032\010\022\006banana\n,\n\024AttrEmptyListDefault\"\024\n\001a\022\013list(float)\032\002\n\000\n,\n\010AttrEnum\" \n\001a\022\006string:\023\n\021\022\006apples\022\007oranges\n6\n\014AttrEnumList\"&\n\001a\022\014list(string):\023\n\021\022\006apples\022\007oranges\n\027\n\tAttrFloat\"\n\n\001a\022\005float\n)\n\017AttrListDefault\"\026\n\001a\022\tlist(int)\032\006\n\004\032\002\005\017\n!\n\013AttrListMin\"\022\n\001a\022\tlist(int)(\0010\002\nH\n\023AttrListTypeDefault\022\t\n\001a\"\001T*\001N\022\t\n\001b\"\001T*\001N\"\r\n\001T\022\004type\032\0020\003\"\014\n\001N\022\003int(\0010\001\n\027\n\007AttrMin\"\014\n\001a\022\003int(\0010\005\n\036\n\020AttrPartialShape\"\n\n\001a\022\005shape\n(\n\024AttrPartialShapeList\"\020\n\001a\022\013list(shape)\n\027\n\tAttrShape\"\n\n\001a\022\005shape\n!\n\rAttrShapeList\"\020\n\001a\022\013list(shape)\n(\n\017AttrTypeDefault\022\006\n\001a\"\001T\"\r\n\001T\022\004type\032\0020\003\n\014\n\001B\032\007\n\003out\030\001\n-\n\006Binary\022\006\n\001a\"\001T\022\006\n\001b\"\001T\032\010\n\003out\"\001T\"\t\n\001T\022\004type\nb\n\rComplexStruct\032\n\n\001a\030\003*\003n_a\032\n\n\001b\030\t*\003n_b\032\010\n\001c2\003t_c\"\014\n\003n_a\022\003int(\001\"\014\n\003n_b\022\003int(\001\"\023\n\003t_c\022\nlist(type)(\001\n#\n\006CopyOp\022\006\n\001a\"\001T\032\006\n\001b\"\001T\"\t\n\001T\022\004type\n\343\003\n\014DefaultAttrs\"\033\n\nstring_val\022\006string\032\005\022\003abc\"*\n\017string_list_val\022\014list(string)\032\t\n\007\022\003abc\022\000\"\022\n\007int_val\022\003int\032\002\030{\"\"\n\014int_list_val\022\tlist(int)\032\007\n\005\032\003\001\002\003\"\031\n\tfloat_val\022\005float\032\005%\000\000 A\"\'\n\016float_list_val\022\013list(float)\032\010\n\006\"\004\000\000 A\"\024\n\010bool_val\022\004bool\032\002(\001\"#\n\rbool_list_val\022\nlist(bool)\032\006\n\004*\002\001\000\"\024\n\010type_val\022\004type\032\0020\003\"#\n\rtype_list_val\022\nlist(type)\032\006\n\0042\002\003\001\"\036\n\tshape_val\022\005shape\032\n:\010\022\002\010\002\022\002\010\001\")\n\016shape_list_val\022\013list(shape)\032\n\n\010:\000:\004\022\002\010\001\"\037\n\ntensor_val\022\006tensor\032\tB\007\010\003\022\000:\001\001\",\n\017tensor_list_val\022\014list(tensor)\032\013\n\tB\007\010\003\022\000:\001\001\n5\n\020FiveFloatOutputs\032\005\n\001a\030\001\032\005\n\001b\030\001\032\005\n\001c\030\001\032\005\n\001d\030\001\032\005\n\001e\030\001\n\023\n\nFloatInput\022\005\n\001a\030\001\n\024\n\013FloatOutput\032\005\n\001a\030\001\n\'\n\027FloatOutputStringOutput\032\005\n\001a\030\001\032\005\n\001b\030\007\n)\n\004Foo1\022\005\n\001a\030\001\022\005\n\001b\030\003\022\005\n\001c\030\003\032\005\n\001d\030\001\032\005\n\001e\030\003\n)\n\004Foo2\022\005\n\001a\030\001\022\005\n\001b\030\007\022\005\n\001c\030\007\032\005\n\001d\030\001\032\005\n\001e\030\003\n)\n\004Foo3\022\005\n\001a\030\001\022\005\n\001b\030\007\022\005\n\001c\030\001\032\005\n\001d\030\001\032\005\n\001e\030\003\n\025\n\010FuncAttr\"\t\n\001f\022\004func\n!\n\017GraphDefVersion\032\013\n\007version\030\003\210\001\001\nM\n\022InPolymorphicTwice\022\t\n\001a\"\001T*\001N\022\t\n\001b\"\001T*\001M\"\t\n\001T\022\004type\"\n\n\001N\022\003int(\001\"\n\n\001M\022\003int(\001\n\026\n\013Int64Output\032\007\n\003out\030\t\n\"\n\007IntAttr\032\007\n\003out\030\t\"\016\n\003foo\022\003int\032\002\030\001\n\021\n\010IntInput\022\005\n\001a\030\003\n\"\n\022IntInputFloatInput\022\005\n\001a\030\003\022\005\n\001b\030\001\n!\n\021IntInputIntOutput\022\005\n\001a\030\003\032\005\n\001b\030\003\n\022\n\tIntOutput\032\005\n\001a\030\003\n$\n\024IntOutputFloatOutput\032\005\n\001a\030\003\032\005\n\001b\030\001\n\031\n\013KernelLabel\032\n\n\006result\030\007\n,\n\023KernelLabelRequired\022\t\n\005input\030\003\032\n\n\006result\030\007\n/\n\tListInput\022\t\n\001a\"\001T*\001N\"\014\n\001N\022\003int(\0010\001\"\t\n\001T\022\004type\n)\n\nListOutput\032\006\n\001a2\001T\"\023\n\001T\022\nlist(type)(\0010\001\n.\n\013MixedStruct\032\n\n\001a\030\003*\003n_a\032\005\n\001b\030\001\"\014\n\003n_a\022\003int(\001\nB\n\023NInPolymorphicTwice\022\t\n\001a\"\001T*\001N\022\t\n\001b\"\001T*\001N\"\t\n\001T\022\004type\"\n\n\001N\022\003int(\001\n*\n\010NInTwice\022\010\n\001a\030\003*\001N\022\010\n\001b\030\007*\001N\"\n\n\001N\022\003int(\001\nM\n\023NInTwoTypeVariables\022\t\n\001a\"\001S*\001N\022\t\n\001b\"\001T*\001N\"\t\n\001S\022\004type\"\t\n\001T\022\004type\"\n\n\001N\022\003int(\001\n!\n\007NIntsIn\022\010\n\001a\030\003*\001N\"\014\n\001N\022\003int(\0010\002\n\"\n\010NIntsOut\032\010\n\001a\030\003*\001N\"\014\n\001N\022\003int(\0010\002\n-\n\017NIntsOutDefault\032\010\n\001a\030\003*\001N\"\020\n\001N\022\003int\032\002\030\003(\0010\002\n4\n\016NPolymorphicIn\022\t\n\001a\"\001T*\001N\"\t\n\001T\022\004type\"\014\n\001N\022\003int(\0010\002\n5\n\017NPolymorphicOut\032\t\n\001a\"\001T*\001N\"\t\n\001T\022\004type\"\014\n\001N\022\003int(\0010\002\nD\n\026NPolymorphicOutDefault\032\t\n\001a\"\001T*\001N\"\r\n\001T\022\004type\032\0020\n\"\020\n\001N\022\003int\032\002\030\002(\0010\002\nD\n\026NPolymorphicRestrictIn\022\t\n\001a\"\001T*\001N\"\021\n\001T\022\004type:\006\n\0042\002\007\n\"\014\n\001N\022\003int(\0010\002\nE\n\027NPolymorphicRestrictOut\032\t\n\001a\"\001T*\001N\"\021\n\001T\022\004type:\006\n\0042\002\007\n\"\014\n\001N\022\003int(\0010\002\n\006\n\004None\n\026\n\003OldB\017\010\010\022\013For reasons\n9\n\021OpWithDefaultAttr\032\005\n\001a\030\003\"\035\n\rdefault_float\022\005float\032\005%\000\000\366B\n\031\n\027OpWithFutureDefaultAttr\n\031\n\004OutT\032\006\n\001a\"\001T\"\t\n\001T\022\004type\n*\n\013OutTypeList\032\010\n\003out2\001T\"\021\n\001T\022\nlist(type)(\001\n<\n\023OutTypeListRestrict\032\010\n\003out2\001t\"\033\n\001t\022\nlist(type)(\0010\001:\006\n\0042\002\007\n\n*\n\013Polymorphic\022\006\n\001a\"\001T\032\010\n\003out\"\001T\"\t\n\001T\022\004type\n0\n\025PolymorphicDefaultOut\032\010\n\003out\"\001T\"\r\n\001T\022\004type\032\0020\007\n%\n\016PolymorphicOut\032\010\n\003out\"\001T\"\t\n\001T\022\004type\n\035\n\005RefIn\022\t\n\001a\"\001T\200\001\001\"\t\n\001T\022\004type\n%\n\022RefInputFloatInput\022\010\n\001a\030\001\200\001\001\022\005\n\001b\030\001\n5\n\033RefInputFloatInputIntOutput\022\010\n\001a\030\001\200\001\001\022\005\n\001b\030\001\032\005\n\001c\030\003\n#\n\020RefInputIntInput\022\010\n\001a\030\003\200\001\001\022\005\n\001b\030\003\n\036\n\006RefOut\032\t\n\001a\"\001T\200\001\001\"\t\n\001T\022\004type\n\025\n\tRefOutput\032\010\n\001a\030\003\200\001\001\n\'\n\024RefOutputFloatOutput\032\010\n\001a\030\001\200\001\001\032\005\n\001b\030\001\n+\n\031RequiresOlderGraphVersion\032\013\n\007version\030\003\210\001\001\n\034\n\014ReservedAttr\"\014\n\005range\022\003int\n\032\n\rReservedInput\022\t\n\005input\030\003\n#\n\020ResourceCreateOp\022\014\n\010resource\030\024\210\001\001\n9\n\025ResourceInitializedOp\022\014\n\010resource\030\024\032\017\n\013initialized\030\n\210\001\001\n\"\n\017ResourceUsingOp\022\014\n\010resource\030\024\210\001\001\n/\n\010Restrict\022\006\n\001a\"\001T\032\010\n\003out\"\001T\"\021\n\001T\022\004type:\006\n\0042\002\007\n\n\030\n\006Simple\022\005\n\001a\030\003\032\007\n\003out\030\001\n(\n\014SimpleStruct\032\n\n\001a\030\003*\003n_a\"\014\n\003n_a\022\003int(\001\n0\n\016StringListAttr\"\021\n\001a\022\014list(string)\"\013\n\001b\022\006string\n[\n\024StubResourceHandleOp\032\014\n\010resource\030\024\"\027\n\tcontainer\022\006string\032\002\022\000\"\031\n\013shared_name\022\006string\032\002\022\000\210\001\001\n7\n\020TestStringOutput\022\t\n\005input\030\001\032\013\n\007output1\030\001\032\013\n\007output2\030\007\n\036\n\016TwoFloatInputs\022\005\n\001a\030\001\022\005\n\001b\030\001\n0\n\031TwoFloatInputsFloatOutput\022\005\n\001a\030\001\022\005\n\001b\030\001\032\005\n\001c\030\001\n.\n\027TwoFloatInputsIntOutput\022\005\n\001a\030\001\022\005\n\001b\030\001\032\005\n\001c\030\003\n\037\n\017TwoFloatOutputs\032\005\n\001a\030\001\032\005\n\001b\030\001\n\034\n\014TwoIntInputs\022\005\n\001a\030\003\022\005\n\001b\030\003\n\035\n\rTwoIntOutputs\032\005\n\001a\030\003\032\005\n\001b\030\003\n,\n\tTwoRefsIn\022\t\n\001a\"\001T\200\001\001\022\t\n\001b\"\001T\200\001\001\"\t\n\001T\022\004type\n%\n\010TypeList\022\006\n\001a2\001T\"\021\n\001T\022\nlist(type)(\001\n7\n\020TypeListRestrict\022\006\n\001a2\001T\"\033\n\001T\022\nlist(type)(\0010\001:\006\n\0042\002\007\n\n2\n\rTypeListTwice\022\006\n\001a2\001T\022\006\n\001b2\001T\"\021\n\001T\022\nlist(type)(\001\n\"\n\005Unary\022\006\n\001a\"\001T\032\006\n\001b\"\001T\"\t\n\001T\022\004type")
