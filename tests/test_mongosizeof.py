import pytest


@pytest.fixture(params=['_cython_impl', '_python_impl'])
def impl(request):
    return pytest.importorskip('mongosizeof.' + request.param)


def test_col_sizeof(impl, benchmark):
    benchmark(impl.col_sizeof, [
        {'a': i, 'b': i, 'c': i, 'd': i, 'e': i, 'f': i, 'g': i, 'h': i}
        for i in range(50000)])


def test_col_sizeof_str(impl):
    pytest.raises(TypeError, impl.col_sizeof, "foo")


class Crap(object):
    def __iter__(self):
        raise RuntimeError('crap')


def test_col_sizeof_logging(impl):
    assert impl.col_sizeof([{'a': Crap()}]) == 25
