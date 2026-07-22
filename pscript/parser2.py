
from . import commonast as ast
from . import stdlib
from . import logger
from .parser1 import Parser1, JSError, unify, reprs


RAW_DOC_WARNING = (
    "Function %s only has a docstring, which used to be "
    "intepreted as raw JS. Wrap a call to RawJS(...) around the "
    'docstring, or add "pass" to the function body to prevent '
    "this behavior."
)

JS_RESERVED_WORDS = set()


RESERVED = {
    "true",
    "false",
    "null",
    "break",
    "case",
    "catch",
    "class",
    "const",
    "continue",
    "debugger",
    "default",
    "delete",
    "do",
    "else",
    "export",
    "extends",
    "finally",
    "for",
    "function",
    "if",
    "import",
    "in",
    "instanceof",
    "new",
    "return",
    "super",
    "switch",
    "this",
    "throw",
    "try",
    "typeof",
    "var",
    "void",
    "while",
    "with",
    "yield",
    "implements",
    "interface",
    "let",
    "package",
    "private",
    "protected",
    "public",
    "static",
    "enum",
    "await",  # only in module code
}


class Parser2(Parser1):


    def parse_Raise(self, node):
        pass

    def parse_Assert(self, node):
        pass

    def parse_Try(self, node):
        pass

    def parse_ExceptHandler(self, node):
        pass

    def parse_With(self, node):
        pass



    def parse_IfExp(self, node):
        pass

    def parse_If(self, node):
        pass

    def parse_For(self, node):
        pass

    def _make_iterable(self, name1, name2, newlines=True):
        pass

    def parse_While(self, node):
        pass

    def parse_Break(self, node):
        pass

    def parse_Continue(self, node):
        pass


    def parse_ListComp_funtionless(self, node, result_name):
        pass

    def parse_ListComp(self, node):
        pass



    def _iterator_assign(self, val, *names):
        pass


    def parse_FunctionDef(self, node, lambda_=False, asyn=False):
        pass

    def parse_Lambda(self, node):
        pass

    def parse_AsyncFunctionDef(self, node):
        pass

    def parse_Return(self, node):
        pass

    def parse_ClassDef(self, node):
        pass

    def function_super(self, node):
        pass


    def parse_Await(self, node):
        pass

    def parse_Global(self, node):
        pass

    def parse_Nonlocal(self, node):
        pass


def get_class_definition(name, base="Object", docstring=""):
    pass
