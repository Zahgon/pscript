# -*- coding: utf-8

import re
import sys
import json

from . import commonast as ast
from . import stdlib, logger

reprs = json.dumps  # Save string representation without the u in u'xx'.


class JSError(Exception):

    pass


def unify(x):
    """Turn string or list of strings parts into string. Braces are
    placed around it if its not alphanumerical
    """

    if isinstance(x, (tuple, list)):
        x = "".join(x)

    if x[0] in "'\"" and x[0] == x[-1] and x.count(x[0]) == 2:
        return x  # string
    elif re.match(r"^[\.\w]*$", x, re.UNICODE):
        return x  # words consisting of normal chars, numbers and dots
    elif re.match(r"^[\.\w]*\(.*\)$", x, re.UNICODE) and x.count(")") == 1:
        return x  # function calls (e.g. 'super()' or 'foo.bar(...)')
    elif re.match(r"^[\.\w]*\[.*\]$", x, re.UNICODE) and x.count("]") == 1:
        return x  # indexing
    elif re.match(r"^\{.*\}$", x, re.UNICODE) and x.count("}") == 1:
        return x  # dicts
    else:
        return "(%s)" % x


class NameSpace(dict):

    _pscript_overload = True

    def set_nonlocal(self, key):
        pass

    def set_global(self, key):
        pass

    def use(self, key, how):
        pass

    def add(self, key):
        """Declare a name as defined in this namespace"""
        curval = self.get(key, 0)
        if curval not in (2, 3):  # dont overwrite nonlocal or global
            self[key] = 1

    def discard(self, key):
        pass

    def leak_stack(self, sub):
        pass

    def is_known(self, name):
        pass

    def get_defined(self):
        """Get list of variable names that the current scope defines."""
        return set([name for name, val in self.items() if val == 1])

    def get_globals(self):
        """Get list of variable names that are declared global in the
        current scope or its subscopes.
        """
        return set([name for name, val in self.items() if val in (3, 4)])

    def get_undefined(self):
        """Get (name, set) tuples for variables that are used, but not
        defined. The set contains the ways in which the variable is used
        (e.g. name.foo.bar).
        """
        return [(name, val) for name, val in self.items() if isinstance(val, set)]


class Parser0:


    NAME_MAP = {
        "True": "true",
        "False": "false",
        "None": "null",
        "unichr": "chr",
        "xrange": "range",
        "self": "this",
    }

    ATTRIBUTE_MAP = {
        "__class__": "Object.getPrototypeOf({})",
    }

    BINARY_OP = {
        "Add": "+",
        "Sub": "-",
        "Mult": "*",
        "Div": "/",
        "Mod": "%",
        "LShift": "<<",
        "RShift": ">>",
        "BitOr": "|",
        "BitXor": "^",
        "BitAnd": "&",
    }

    UNARY_OP = {
        "Invert": "~",
        "Not": "!",
        "UAdd": "+",
        "USub": "-",
    }

    BOOL_OP = {
        "And": "&&",
        "Or": "||",
    }

    COMP_OP = {
        "Eq": "==",
        "NotEq": "!=",
        "Lt": "<",
        "LtE": "<=",
        "Gt": ">",
        "GtE": ">=",
        "Is": "===",
        "IsNot": "!==",
    }

    def __init__(
        self, code, pysource=None, indent=0, docstrings=True, inline_stdlib=True
    ):
        self._pycode = code  # helpfull during debugging
        self._pysource = None
        if isinstance(pysource, str):
            self._pysource = pysource, 0
        elif isinstance(pysource, tuple):
            self._pysource = str(pysource[0]), int(pysource[1])
        elif pysource is not None:
            logger.warning("Parser ignores pysource; it must be str or (str, int).")
        self._root = ast.parse(code)
        self._stack = []
        self._indent = indent
        self._dummy_counter = 0
        self._scope_prefix = []  # stack of name prefixes to simulate local scope

        self._std_functions = set()
        self._std_methods = set()

        self._seen_func_names = set()
        self._seen_class_names = set()

        self._docstrings = bool(docstrings)  # whether to inclue docstrings

        self._functions, self._methods = {}, {}
        for name in dir(self.__class__):
            if name.startswith("function_op_"):
                pass  # special operator function that we use explicitly
            elif name.startswith("function_"):
                self._functions[name[9:]] = getattr(self, name)
            elif name.startswith("method_"):
                self._methods[name[7:]] = getattr(self, name)

        self.push_stack("module", "")

        try:
            self._parts = self.parse(self._root)
        except JSError as err:
            _, _, tb = sys.exc_info()
            try:
                msg = self._better_js_error(tb)
            except Exception:  # pragma: no cover
                raise (err) from None
            else:
                err.args = (msg + ":\n" + str(err),)
                raise (err)

        ns = self.vars  # do not self.pop_stack() so caller can inspect module vars
        defined_names = ns.get_defined()
        if defined_names:
            self._parts.insert(0, self.get_declarations(ns))

        if inline_stdlib:
            libcode = stdlib.get_partial_std_lib(
                self._std_functions, self._std_methods, self._indent
            )
            if libcode:
                self._parts.insert(0, libcode)

        if self._parts:
            self._parts[0] = "    " * indent + self._parts[0].lstrip()

    def dump(self):
        """Get the JS code as a string."""
        return "".join(self._parts)

    def _better_js_error(self, tb):  # pragma: no cover
        pass

    def push_stack(self, type, name):
        pass

    def pop_stack(self):
        pass

    def get_declarations(self, ns):
        pass

    def with_prefix(self, name, new=False):
        pass

    @property
    def vars(self):
        pass

    def lf(self, code=""):
        pass

    def dummy(self, name=""):
        pass

    def _handle_std_deps(self, code):
        pass

    def use_std_function(self, name, arg_nodes):
        pass

    def use_std_method(self, base, name, arg_nodes):
        pass

    def pop_docstring(self, node):
        pass

    def parse(self, node):
        pass
