#  __author__ = 'Alexey Buchkin'

from model.contact import Contact
import pytest
import random


def test_delete_first_contact(app, db, check_ui):
    with pytest.allure.step('Given check availability of at least one contract'):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                                       nickname="nickname", title="title", company="company", address="address",
                                       home="home", mobile="mobile", work="work", fax="fax",
                                       email="email@fdsf.ru", email2="email2@dfds.ru",
                                       email3="email3@fjdkjfkds.ru", homepage="homepage", bday="1",
                                       bmonth="December", byear="1970", aday="21", amonth="December", ayear="1971",
                                       address2="address2", phone2="phone2",
                                       notes="notes"))
    with pytest.allure.step('Given a contacts list'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('Given a random contact from contacts: %s' % old_contacts):
        contact = random.choice(old_contacts)
    with pytest.allure.step('When I delete contract: %s' % contact):
        app.contact.delete_by_id(contact.id)
    with pytest.allure.step('Then the new list contracts is equal to the old list with the remove contact: %s ' % contact):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) - 1 == len(db.get_contact_list())
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts,
                          key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                           key=Contact.id_or_max)
