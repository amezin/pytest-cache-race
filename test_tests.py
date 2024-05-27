import pytest


@pytest.mark.parametrize('n', list((n,) for n in range(42)))
def test_test(my_fixture, n):
    pass
