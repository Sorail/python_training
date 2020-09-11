#  __author__ = 'Alexey Buchkin'
from typing import List, Any

from model.group import Group
import random


def test_edit_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test1"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_new = Group(name="gvdfbvcb22", header="bvcbvcbvcgdfgfd222", footer="bcvbvcgfdgfdgdf222")
    group_new.id = group.id
    app.group.edit_by_id(group_new, group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    index = old_groups.index(group)
    old_groups[index] = group_new
    assert check_groups(new_groups, old_groups)
    if check_ui:
        assert check_groups(app.group.get_group_list(), new_groups)


def test_edit_some_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test1"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_new = Group(name="New Group 1")
    group_new.id = group.id
    app.group.edit_by_id(group_new, group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    index = old_groups.index(group)
    old_groups[index] = group_new
    assert check_groups(app.group.get_group_list(), new_groups)
    if check_ui:
        assert check_groups(app.group.get_group_list(), new_groups)


def check_groups(new_groups, old_groups):
    return sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
