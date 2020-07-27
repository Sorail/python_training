# -*- coding: utf-8 -*-
#  __author__ = 'Alexey Buchkin'

from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="gvdfbvcb", header="bvcbvcbvcgdfgfd", footer="bcvbvcgfdgfdgdf"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
