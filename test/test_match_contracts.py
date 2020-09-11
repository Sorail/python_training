#  __author__ = 'Alexey Buchkin'

from model.contact import Contact


def test_match_contact(app, db):
    contact_ui_list = app.contact.get_contact_list()
    contact_db_list = db.get_contact_list()
    assert sorted(contact_ui_list, key=Contact.id_or_max) == sorted(contact_db_list, key=Contact.id_or_max)
