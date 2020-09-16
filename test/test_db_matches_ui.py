#  __author__ = 'Alexey Buchkin'

from model.group import Group
import pytest


def test_group_list(app, db):
    with pytest.allure.step('Given a groups list from UI'):
        ui_list = app.group.get_group_list()

    def clean(group):
        return Group(id=group.id, name=group.name.strip())

    with pytest.allure.step('Given a groups list from DB'):
        db_list = map(clean, db.get_group_list())

    with pytest.allure.step('Then equal list from UI with list from DB'):
        assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
