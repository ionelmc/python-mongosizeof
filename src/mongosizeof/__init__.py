try:
    from ._cython_impl import bson_sizeof, col_sizeof, col_sizeof_row
except ImportError:
    from ._python_impl import bson_sizeof, col_sizeof, col_sizeof_row

__version__ = '0.3.0'
__all__ = 'bson_sizeof', 'col_sizeof', 'col_sizeof_row'
