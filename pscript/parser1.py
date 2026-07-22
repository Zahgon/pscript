
import re

from . import commonast as ast
from . import stdlib
from .parser0 import Parser0, JSError, unify, reprs


_bool_funcs = "hasattr", "all", "any", "op_contains", "op_equals", "truthy"
_bool_meths = (
    "count",
    "isalnum",
    "isalpha",
    "isidentifier",
    "islower",
    "isnumeric",
    "isdigit",
    "isdecimal",
    "isspace",
    "istitle",
    "isupper",
    "startswith",
)
returning_bool = tuple(
    [stdlib.FUNCTION_PREFIX + x + "(" for x in _bool_funcs]
    + [stdlib.METHOD_PREFIX + x + "." for x in _bool_meths]
)


isidentifier1 = re.compile(r"^\w+$", re.UNICODE)

reserved_names = (
    "abstract",
    "instanceof",
    "boolean",
    "enum",
    "switch",
    "export",
    "interface",
    "synchronized",
    "extends",
    "let",
    "case",
    "throw",
    "catch",
    "final",
    "native",
    "throws",
    "new",
    "transient",
    "const",
    "package",
    "function",
    "private",
    "typeof",
    "debugger",
    "goto",
    "protected",
    "var",
    "default",
    "public",
    "void",
    "delete",
    "implements",
    "volatile",
    "do",
    "static",
)


class Parser1(Parser0):

    @property
    def _pscript_overload(self):
        pass


    def parse_Num(self, node):
        pass

    def parse_Str(self, node):
        pass

    def parse_JoinedStr(self, node):
        pass

    def parse_FormattedValue(self, node):  # can als be present standalone
        pass

    def _parse_FormattedValue_fmt(self, node):
        pass

    def parse_Bytes(self, node):
        raise JSError("No Bytes in JS")

    def parse_NameConstant(self, node):
        pass

    def parse_List(self, node):
        pass

    def parse_Tuple(self, node):
        pass

    def parse_Dict(self, node):
        pass

    def parse_Set(self, node):
        raise JSError("No Set in JS")


    def push_scope_prefix(self, prefix):
        pass

    def pop_scope_prefix(self):
        pass

    def parse_Name(self, node, fullname=None):
        pass

    def parse_Starred(self, node):
        raise JSError("Starred args are not supported.")


    def parse_Expr(self, node):
        pass

    def parse_UnaryOp(self, node):
        pass

    def parse_BinOp(self, node):
        pass

    def _format_string(self, node):
        pass

    def _wrap_truthy(self, node):
        pass

    def parse_BoolOp(self, node):
        pass

    def parse_Compare(self, node):
        pass

    def parse_Call(self, node):
        pass

    def _get_args(self, node, base_name, use_call_or_apply=False):
        pass

    def _get_positional_args(self, node):
        pass

    def _get_keyword_args(self, node):
        pass

    def parse_Attribute(self, node, fullname=None):
        pass


    def parse_Assign(self, node):
        pass

    def parse_AugAssign(self, node):  # -> x += 1
        pass

    def parse_Delete(self, node):
        pass

    def parse_Pass(self, node):
        pass


    def parse_Subscript(self, node):
        pass

    def parse_Index(self, node):
        pass

    def parse_Slice(self, node):
        pass

    def parse_ExtSlice(self, node):
        raise JSError("Multidimensional slicing not supported in JS")


    def parse_Import(self, node):
        pass

    def parse_Module(self, node):
        pass
