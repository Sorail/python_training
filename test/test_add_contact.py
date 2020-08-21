# -*- coding: utf-8 -*-
#  __author__ = 'Alexey Buchkin'

from model.contact import Contact


def test_add_contract(app):
    old_contacts = app.contact.get_contact_list()
    contract = Contact(firstname="qazwsx", middlename="edcrfv", lastname="tgbyhn", nickname="yhnujm",
                              title="zaqxsw", company="cdevfr", address="tgbyhnujm", home="+7894454515", mobile="+9854",
                              work="+988456458474", fax="rfvbgtyh", email="fdsfds@fdsf.ru", email2="fdsfdg@dfds.ru",
                              email3="fdjjfdskl@fjdkjfkds.ru", homepage="gjfdjhgdfjgkl", bday="12", bmonth="April",
                              byear="1980",
                              aday="15", amonth="March", ayear="1985", address2="hgfhgfdgfdgdfgdfs",
                              phone2="+79854456648", notes="gfdsgfdgfdgdfsgfd")
    app.contact.create(contract)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contract)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
