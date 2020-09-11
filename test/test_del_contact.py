#  __author__ = 'Alexey Buchkin'

from model.contact import Contact
import random


def test_delete_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                                   nickname="nickname", title="title", company="company", address="address",
                                   home="home", mobile="mobile", work="work", fax="fax",
                                   email="email@fdsf.ru", email2="email2@dfds.ru",
                                   email3="email3@fjdkjfkds.ru", homepage="homepage", bday="1",
                                   bmonth="December", byear="1970", aday="21", amonth="December", ayear="1971",
                                   address2="address2", phone2="phone2",
                                   notes="notes"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(db.get_contact_list())
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts,
                      key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                       key=Contact.id_or_max)
