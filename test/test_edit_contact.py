#  __author__ = 'Alexey Buchkin'

from model.contact import Contact
import random


def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                                   nickname="nickname", title="title", company="company", address="address",
                                   home="+985445548", mobile="+98564545", work="+8984848", fax="+9854411",
                                   email="email@fdsf.ru", email2="email2@dfds.ru",
                                   email3="email3@fjdkjfkds.ru", homepage="homepage", bday="1",
                                   bmonth="December", byear="1970", aday="21", amonth="December", ayear="1971",
                                   address2="address2", phone2="+9845547848",
                                   notes="notes"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_new = Contact(firstname="qazwsx", middlename="edcrfv", lastname="tgbyhn", nickname="yhnujm",
                       title="zaqxsw", company="cdevfr", address="tgbyhnujm", home="+9855", mobile="+966541",
                       work="+65954", fax="+665999", email="fdsfds@fdsf.ru", email2="fdsfdg@dfds.ru",
                       email3="fdjjfdskl@fjdkjfkds.ru", homepage="gjfdjhgdfjgkl", bday="12", bmonth="April",
                       byear="1980",
                       aday="15", amonth="August", ayear="1985", address2="hgfhgfdgfdgdfgdfs",
                       phone2="+65561114", notes="gfdsgfdgfdgdfsgfd")
    contact_new.id = contact.id
    app.contact.edit_by_id(contact_new, contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(db.get_contact_list())
    index = old_contacts.index(contact)
    old_contacts[index] = contact_new
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts,
                      key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                       key=Contact.id_or_max)
