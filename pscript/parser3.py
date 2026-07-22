
from . import commonast as ast
from . import stdlib
from .parser2 import Parser2, JSError, unify
from .stubs import RawJS




class Parser3(Parser2):

    def function_this_is_js(self, node):
        pass

    def function_RawJS(self, node):
        pass


    def function_isinstance(self, node):
        pass

    def function_issubclass(self, node):
        pass

    def function_print(self, node):
        pass

    def function_len(self, node):
        pass

    def function_max(self, node):
        pass

    def function_min(self, node):
        pass

    def function_callable(self, node):
        pass

    def function_chr(self, node):
        pass

    def function_ord(self, node):
        pass

    def function_dict(self, node):
        pass

    def function_list(self, node):
        pass

    def function_tuple(self, node):
        pass

    def function_range(self, node):
        pass

    def function_sorted(self, node):
        pass


    def method_sort(self, node, base):
        pass

    def method_format(self, node, base):
        pass




def make_function(name, nargs, function_deps, method_deps):
    pass


def make_method(name, nargs, function_deps, method_deps):
    pass


for name, code in stdlib.METHODS.items():
    nargs, function_deps, method_deps = stdlib.get_std_info(code)
    if nargs and not hasattr(Parser3, "method_" + name):
        m = make_method(name, tuple(nargs), function_deps, method_deps)
        setattr(Parser3, "method_" + name, m)

for name, code in stdlib.FUNCTIONS.items():
    nargs, function_deps, method_deps = stdlib.get_std_info(code)
    if nargs and not hasattr(Parser3, "function_" + name):
        m = make_function(name, tuple(nargs), function_deps, method_deps)
        setattr(Parser3, "function_" + name, m)
