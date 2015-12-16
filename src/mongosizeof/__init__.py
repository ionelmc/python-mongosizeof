try:
    from ._cython_impl import bson_sizeof
except ImportError:
    from ._python_impl import bson_sizeof