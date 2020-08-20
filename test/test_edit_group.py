#  __author__ = 'Alexey Buchkin'

from model.group import Group
from random import randrange


def test_edit_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test1"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="gvdfbvcb22", header="bvcbvcbvcgdfgfd222", footer="bcvbvcgfdgfdgdf222")
    group.id = old_groups[index].id
    app.group.edit_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_some_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test1"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New Group 1")
    group.id = old_groups[index].id
    app.group.edit_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
