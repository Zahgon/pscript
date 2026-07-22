
import sys


class RawJS:

    def __init__(self, code, _resolve_defining_module=True):
        if not isinstance(code, str):
            raise TypeError("RawJS requires str input.")
        self._lines = self._str2lines(code)

        try:
            raise Exception()
        except Exception as err:
            tb = getattr(err, "__traceback__", None)
            self._globals = tb.tb_frame.f_back.f_globals
            del tb
        self.__module__ = self._globals["__name__"]
        self._real_name = None

    def __repr__(self):
        if len(self._lines) == 1 and len(self._lines[0]) < 60:
            return '<%s "%s">' % (self.__class__.__name__, self.get_code(0))
        else:
            return "<%s with %i lines>" % (self.__class__.__name__, len(self._lines))

    def __str__(self):
        return self.get_code(0)

    @classmethod
    def _str2lines(cls, text):
        pass

    def get_defined_name(self, suggestion=None):
        pass

    def get_code(self, indent=0):
        pass


class JSConstant:

    def __init__(self, name="jsconstant"):
        self._name = name

    def __repr__(self):  # pragma: no cover
        return "<%s %s>" % (self.__class__.__name__, self._name)


class Stubs:
    __name__ = __name__
    __file__ = __file__
    JSConstant = JSConstant
    RawJS = RawJS

    def __getattr__(self, name):
        if name in ("JSConstant", "RawJS"):
            return getattr(self, name)
        else:
            return self.JSConstant(name)


sys.modules[__name__] = Stubs()
