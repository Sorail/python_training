#  __author__ = 'Alexey Buchkin'

from model.group import Group
import pytest
import re
from model.contact import Contact


def test_group_list(app, db):
    with pytest.allure.step('Given a groups list from UI'):
        ui_list = app.group.get_group_list()

    def clean(group):
        return Group(id=group.id, name=group.name.strip())

    with pytest.allure.step('Given a groups list from DB'):
        db_list = map(clean, db.get_group_list())

    with pytest.allure.step('Then equal list from UI with list from DB'):
        assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contacts_on_home_page(app, db):
    with pytest.allure.step('Given a contact list from UI'):
        all_contact_from_home_page = app.contact.get_contact_list()
    with pytest.allure.step('Given a contact list from DB'):
        db_list = db.get_contact_list_with_info()
    with pytest.allure.step('Then equal list from UI with list from DB'):
        assert sorted(all_contact_from_home_page, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)


def clear(s):
    return re.sub("[() -]", "", s)
