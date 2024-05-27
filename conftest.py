import pytest


@pytest.fixture(scope='session')
def my_fixture(request):
    return request.config.cache.mkdir('testdir')
