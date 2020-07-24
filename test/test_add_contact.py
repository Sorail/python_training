# -*- coding: utf-8 -*-
#  __author__ = 'Alexey Buchkin'


import pytest

from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contract(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact(firstname="qazwsx", middlename="edcrfv", lastname="tgbyhn", nickname="yhnujm",
                              title="zaqxsw", company="cdevfr", address="tgbyhnujm", home="tgbrfv", mobile="cderfv",
                              work="tgbnhy", fax="rfvbgtyh", email="fdsfds@fdsf.ru", email2="fdsfdg@dfds.ru",
                              email3="fdjjfdskl@fjdkjfkds.ru", homepage="gjfdjhgdfjgkl", bday="12", bmonth="April",
                              byear="1980",
                              aday="15", amonth="March", ayear="1856", address2="hgfhgfdgfdgdfgdfs",
                              phone2="gfdhsgfhgfhgfd", notes="gfdsgfdgfdgdfsgfd"))
    app.session.logout()
