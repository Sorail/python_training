#  __author__ = 'Alexey Buchkin'

from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first(Group(name="gvdfbvcb22", header="bvcbvcbvcgdfgfd222", footer="bcvbvcgfdgfdgdf222"))


def test_edit_first_group_name(app):
    app.group.edit_first(Group(name="New Group 1"))
