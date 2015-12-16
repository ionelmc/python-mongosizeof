try:
    from ._cython_impl import bson_sizeof
except ImportError:
    from ._python_impl import bson_sizeof

__version__ = '0.2.0'
