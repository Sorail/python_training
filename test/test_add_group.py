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
    app.helper.session.login(username="admin", password="secret")
    app.helper.group.create(Group(name="gvdfbvcb", header="bvcbvcbvcgdfgfd", footer="bcvbvcgfdgfdgdf"))
    app.helper.session.logout()


def test_add_empty_group(app):
    app.helper.session.login(username="admin", password="secret")
    app.helper.group.create(Group(name="", header="", footer=""))
    app.helper.session.logout()
