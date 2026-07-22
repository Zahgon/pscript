
from __future__ import print_function, absolute_import

import sys
import ast
import json
import base64

if hasattr(base64, "encodebytes"):
    encodebytes = base64.encodebytes
    decodebytes = base64.decodebytes
else:
    encodebytes = base64.encodestring
    decodebytes = base64.decodestring

NoneType = None.__class__
_Ellipsis = Ellipsis


docheck = "pytest" in sys.modules


old_index_types = tuple(
    getattr(ast, x)
    for x in ("Slice", "Index", "ExtSlice", "Ellipsis")
    if getattr(ast, x, None) is not None
)


def parse(code, comments=False):
    pass


class Node(object):

    __slots__ = ["lineno", "col_offset"]

    class OPS:

        UAdd = "UAdd"
        USub = "USub"
        Not = "Not"
        Invert = "Invert"
        Add = "Add"
        Sub = "Sub"
        Mult = "Mult"
        Div = "Div"
        FloorDiv = "FloorDiv"
        Mod = "Mod"
        Pow = "Pow"
        LShift = "LShift"
        RShift = "RShift"
        BitOr = "BitOr"
        BitXor = "BitXor"
        BitAnd = "BitAnd"
        And = "And"
        Or = "Or"

    class COMP:

        Eq = "Eq"
        NotEq = "NotEq"
        Lt = "Lt"
        LtE = "LtE"
        Gt = "Gt"
        GtE = "GtE"
        Is = "Is"
        IsNot = "IsNot"
        In = "In"
        NotIn = "NotIn"

    def __init__(self, *args):
        names = self.__slots__
        assert len(args) == len(names)  # check this always
        if docheck:
            assert not hasattr(self, "__dict__"), "Nodes must have __slots__"
            assert self.__class__ is not Node, "Node is an abstract class"
            for name, val in zip(names, args):
                assert not isinstance(val, ast.AST)
                if name == "name":
                    assert isinstance(val, (str, NoneType)), "name not a string"
                elif name == "op":
                    assert val in Node.OPS.__dict__ or val in Node.COMP.__dict__
                elif name.endswith("_node"):
                    assert isinstance(val, (Node, NoneType)), "%r is not a Node" % name
                elif name.endswith("_nodes"):
                    islistofnodes = isinstance(val, list) and all(
                        isinstance(n, Node) for n in val
                    )
                    assert islistofnodes, "%r is not a list of nodes" % name
                else:
                    assert not isinstance(val, Node), "%r should not be a Node" % name
                    assert not (
                        isinstance(val, list) and all(isinstance(n, Node) for n in val)
                    )
        for name, val in zip(names, args):
            setattr(self, name, val)

    def tojson(self, indent=2):
        pass

    @classmethod
    def fromjson(cls, text):
        pass

    @classmethod
    def _fromdict(cls, d):
        pass

    def _todict(self):
        pass

    def __eq__(self, other):
        if not isinstance(other, Node):
            raise ValueError("Can only compare nodes to other nodes.")
        return self._todict() == other._todict()

    def __repr__(self):
        names = ", ".join([repr(x) for x in self.__slots__])
        return "<%s with %s at 0x%x>" % (self.__class__.__name__, names, id(self))

    def __str__(self):
        return self.tojson()


try:
    Node.OPS.__doc__ += ", ".join(
        [x for x in sorted(Node.OPS.__dict__) if not x.startswith("_")]
    )
    Node.COMP.__doc__ += ", ".join(
        [x for x in sorted(Node.COMP.__dict__) if not x.startswith("_")]
    )
except AttributeError:  # pragma: no cover
    pass  # Py < 3.3





class Comment(Node):

    __slots__ = ("value",)


class Module(Node):

    __slots__ = ("body_nodes",)




class Num(Node):

    __slots__ = ("value",)


class Str(Node):

    __slots__ = ("value",)


class FormattedValue(Node):

    __slots__ = "value_node", "conversion", "format_node"


class JoinedStr(Node):

    __slots__ = ("value_nodes",)


class Bytes(Node):

    __slots__ = ("value",)


class List(Node):

    __slots__ = ("element_nodes",)


class Tuple(Node):

    __slots__ = ("element_nodes",)


class Set(Node):

    __slots__ = ("element_nodes",)


class Dict(Node):

    __slots__ = "key_nodes", "value_nodes"


class Ellipsis(Node):

    __slots__ = ()


class NameConstant(Node):

    __slots__ = ("value",)




class Name(Node):

    __slots__ = ("name",)


class Starred(Node):

    __slots__ = ("value_node",)


class Attribute(Node):

    __slots__ = "value_node", "attr"


class Subscript(Node):

    __slots__ = "value_node", "slice_node"


class Index(Node):

    __slots__ = ("value_node",)


class Slice(Node):

    __slots__ = "lower_node", "upper_node", "step_node"


class ExtSlice(Node):

    __slots__ = ("dim_nodes",)




class Expr(Node):

    __slots__ = ("value_node",)


class UnaryOp(Node):

    __slots__ = "op", "right_node"


class BinOp(Node):

    __slots__ = "op", "left_node", "right_node"


class BoolOp(Node):

    __slots__ = "op", "value_nodes"


class Compare(Node):

    __slots__ = "op", "left_node", "right_node"


class Call(Node):

    __slots__ = ("func_node", "arg_nodes", "kwarg_nodes")


class Keyword(Node):

    __slots__ = ("name", "value_node")


class IfExp(Node):

    __slots__ = "test_node", "body_node", "else_node"


class ListComp(Node):

    __slots__ = "element_node", "comp_nodes"


class SetComp(Node):

    __slots__ = "element_node", "comp_nodes"


class GeneratorExp(Node):

    __slots__ = "element_node", "comp_nodes"


class DictComp(Node):

    __slots__ = "key_node", "value_node", "comp_nodes"


class Comprehension(Node):

    __slots__ = "target_node", "iter_node", "if_nodes"




class Assign(Node):

    __slots__ = "target_nodes", "value_node"


class AugAssign(Node):

    __slots__ = "target_node", "op", "value_node"


class Raise(Node):

    __slots__ = "exc_node", "cause_node"


class Assert(Node):

    __slots__ = "test_node", "msg_node"


class Delete(Node):

    __slots__ = ("target_nodes",)


class Pass(Node):

    __slots__ = ()


class Import(Node):

    __slots__ = "root", "names", "level"




class If(Node):

    __slots__ = "test_node", "body_nodes", "else_nodes"


class For(Node):

    __slots__ = "target_node", "iter_node", "body_nodes", "else_nodes"


class While(Node):

    __slots__ = "test_node", "body_nodes", "else_nodes"


class Break(Node):

    __slots__ = ()


class Continue(Node):

    __slots__ = ()


class Try(Node):

    __slots__ = "body_nodes", "handler_nodes", "else_nodes", "finally_nodes"


class ExceptHandler(Node):

    __slots__ = "type_node", "name", "body_nodes"


class With(Node):

    __slots__ = "item_nodes", "body_nodes"


class WithItem(Node):

    __slots__ = "expr_node", "as_node"




class FunctionDef(Node):

    __slots__ = (
        "name",
        "decorator_nodes",
        "annotation_node",
        "arg_nodes",
        "kwarg_nodes",
        "args_node",
        "kwargs_node",
        "body_nodes",
    )


class Lambda(Node):

    __slots__ = ("arg_nodes", "kwarg_nodes", "args_node", "kwargs_node", "body_node")


class AsyncFunctionDef(Node):

    __slots__ = (
        "name",
        "decorator_nodes",
        "annotation_node",
        "arg_nodes",
        "kwarg_nodes",
        "args_node",
        "kwargs_node",
        "body_nodes",
    )


class Arg(Node):

    __slots__ = ("name", "value_node", "annotation_node")


class Return(Node):

    __slots__ = ("value_node",)


class Yield(Node):

    __slots__ = ("value_node",)


class YieldFrom(Node):

    __slots__ = ("value_node",)


class Await(Node):

    __slots__ = ("value_node",)


class Global(Node):

    __slots__ = ("names",)


class Nonlocal(Node):

    __slots__ = ("names",)


class ClassDef(Node):

    __slots__ = ("name", "decorator_nodes", "arg_nodes", "kwarg_nodes", "body_nodes")




class NativeAstConverter:

    def __init__(self, code):
        self._root = ast.parse(code)
        self._lines = code.splitlines()
        self._stack = []  # contains tuple elements: (list_obj, native_nodes)

    def _add_comments(self, container, lineno):
        pass

    def convert(self, comments=False):
        pass

    def _convert(self, n):
        pass

    def _convert_Module(self, n):
        pass


    def _convert_Constant(self, n):
        pass

    def _convert_Num(self, n):
        pass

    def _convert_Str(self, n):
        pass

    def _convert_JoinedStr(self, n):
        pass

    def _convert_FormattedValue(self, n):
        pass

    def _convert_Bytes(self, n):
        pass

    def _convert_List(self, n):
        pass

    def _convert_Tuple(self, n):
        pass

    def _convert_Set(self, n):
        pass

    def _convert_Dict(self, n):
        pass

    def _convert_Ellipsis(self, n):
        pass

    def _convert_NameConstant(self, n):
        pass


    def _convert_Name(self, n):
        pass

    def _convert_Starred(self, n):
        pass

    def _convert_Attribute(self, n):
        pass

    def _convert_Subscript(self, n):
        pass

    def _convert_index_like(self, n):
        pass

    def _convert_Index(self, n):
        pass

    def _convert_Slice(self, n):
        pass

    def _convert_ExtSlice(self, n):
        pass


    def _convert_Expr(self, n):
        pass

    def _convert_UnaryOp(self, n):
        pass

    def _convert_BinOp(self, n):
        pass

    def _convert_BoolOp(self, n):
        pass

    def _convert_Compare(self, n):
        pass

    def _convert_Call(self, n):
        pass

    def _convert_keyword(self, n):
        pass

    def _convert_IfExp(self, n):
        pass

    def _convert_ListComp(self, n):
        pass

    def _convert_SetComp(self, n):
        pass

    def _convert_GeneratorExp(self, n):
        pass

    def _convert_DictComp(self, n):
        pass

    def _convert_comprehension(self, n):
        pass


    def _convert_Assign(self, n):
        pass

    def _convert_AugAssign(self, n):
        pass

    def _convert_AnnAssign(self, n):
        pass

    def _convert_Print(self, n):  # pragma: no cover - Python 2.x compat
        pass

    def _convert_Exec(self, n):  # pragma: no cover - Python 2.x compat
        pass

    def _convert_Repr(self, n):  # pragma: no cover - Python 2.x compat
        pass

    def _convert_Raise(self, n):
        pass

    def _convert_Assert(self, n):
        pass

    def _convert_Delete(self, n):
        pass

    def _convert_Pass(self, n):
        pass

    def _convert_Import(self, n):
        pass

    def _convert_ImportFrom(self, n):
        pass


    def _convert_If(self, n):
        pass

    def _convert_For(self, n):
        pass

    def _convert_While(self, n):
        pass

    def _convert_Break(self, n):
        pass

    def _convert_Continue(self, n):
        pass

    def _convert_Try(self, n):
        pass

    def _convert_TryFinally(self, n):  # pragma: no cover - Py <= 3.2
        pass

    def _convert_TryExcept(self, n):  # pragma: no cover - Py <= 3.2
        pass

    def _convert_ExceptHandler(self, n):
        pass

    def _convert_With(self, n):
        pass

    def _convert_withitem(self, n):
        pass


    def _convert_functiondefs(self, n, cls):
        pass

    def _convert_FunctionDef(self, n):
        pass

    def _convert_Lambda(self, n):
        pass

    def _convert_AsyncFunctionDef(self, n):
        pass

    def _convert_arg(self, n):
        pass

    def _convert_Return(self, n):
        pass

    def _convert_Yield(self, n):
        pass

    def _convert_YieldFrom(self, n):
        pass

    def _convert_Await(self, n):
        pass

    def _convert_Global(self, n):
        pass

    def _convert_Nonlocal(self, n):
        pass

    def _convert_ClassDef(self, n):
        pass
