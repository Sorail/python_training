#  __author__ = 'Alexey Buchkin'

from model.group import Group
import pytest
import random


def test_delete_some_group(app, db, check_ui):
    with pytest.allure.step('Given check availability of at least one group'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test1"))
    with pytest.allure.step('Given a groups list'):
        old_groups = db.get_group_list()
    with pytest.allure.step('Given a random group from groups: %s' % old_groups):
        group = random.choice(old_groups)
    with pytest.allure.step('When I delete a group %s to the list' % group):
        app.group.delete_by_id(group.id)
    with pytest.allure.step('Then the new group list is equal to the old list with the remove group'):
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
