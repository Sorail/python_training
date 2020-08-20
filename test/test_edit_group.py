#  __author__ = 'Alexey Buchkin'

from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test1"))
    old_groups = app.group.get_group_list()
    group = Group(name="gvdfbvcb22", header="bvcbvcbvcgdfgfd222", footer="bcvbvcgfdgfdgdf222")
    group.id = old_groups[0].id
    app.group.edit_first(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test1"))
    old_groups = app.group.get_group_list()
    app.group.edit_first(Group(name="New Group 1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
