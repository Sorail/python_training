#  __author__ = 'Alexey Buchkin'

from model.contact import Contact
from random import randrange


def test_edit_some_contract(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                                   nickname="nickname", title="title", company="company", address="address",
                                   home="home", mobile="mobile", work="work", fax="fax",
                                   email="email@fdsf.ru", email2="email2@dfds.ru",
                                   email3="email3@fjdkjfkds.ru", homepage="homepage", bday="1",
                                   bmonth="December", byear="1970", aday="21", amonth="December", ayear="1971",
                                   address2="address2", phone2="phone2",
                                   notes="notes"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contract = Contact(firstname="qazwsx", middlename="edcrfv", lastname="tgbyhn", nickname="yhnujm",
                       title="zaqxsw", company="cdevfr", address="tgbyhnujm", home="tgbrfv", mobile="cderfv",
                       work="tgbnhy", fax="rfvbgtyh", email="fdsfds@fdsf.ru", email2="fdsfdg@dfds.ru",
                       email3="fdjjfdskl@fjdkjfkds.ru", homepage="gjfdjhgdfjgkl", bday="12", bmonth="April",
                       byear="1980",
                       aday="15", amonth="March", ayear="1985", address2="hgfhgfdgfdgdfgdfs",
                       phone2="gfdhsgfhgfhgfd", notes="gfdsgfdgfdgdfsgfd")
    contract.id = old_contacts[index].id
    app.contact.edit_by_index(contract, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contract
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
