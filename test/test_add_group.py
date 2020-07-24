# -*- coding: utf-8 -*-
#  __author__ = 'Alexey Buchkin'

import pytest

from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="gvdfbvcb", header="bvcbvcbvcgdfgfd", footer="bcvbvcgfdgfdgdf"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
