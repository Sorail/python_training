#  __author__ = 'Alexey Buchkin'

#  __author__ = 'Alexey Buchkin'

import pytest

from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
