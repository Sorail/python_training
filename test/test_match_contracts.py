#  __author__ = 'Alexey Buchkin'

from model.contact import Contact
import pytest


def test_match_contact(app, db):
    with pytest.allure.step('Given a contact list from UI'):
        contact_ui_list = app.contact.get_contact_list()
    with pytest.allure.step('Given a contact list from DB'):
        contact_db_list = db.get_contact_list()
    with pytest.allure.step('Then equal list from UI with list from DB'):
        assert sorted(contact_ui_list, key=Contact.id_or_max) == sorted(contact_db_list, key=Contact.id_or_max)
