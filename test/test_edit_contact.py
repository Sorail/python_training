#  __author__ = 'Alexey Buchkin'

from model.contact import Contact


def test_edit_first_contract(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                                   nickname="nickname", title="title", company="company", address="address",
                                   home="home", mobile="mobile", work="work", fax="fax",
                                   email="email@fdsf.ru", email2="email2@dfds.ru",
                                   email3="email3@fjdkjfkds.ru", homepage="homepage", bday="1",
                                   bmonth="December", byear="1970", aday="21", amonth="December", ayear="1971",
                                   address2="address2", phone2="phone2",
                                   notes="notes"))
    app.contact.edit_first(Contact(firstname="qazwsx123", middlename="edcrfv123", lastname="tgbyhn123",
                                   nickname="yhnujm123", title="zaqxsw123", company="cdevfr123", address="tgbyhnujm123",
                                   home="tgbrfv123", mobile="cderfv123", work="tgbnhy123", fax="rfvbgtyh123",
                                   email="123fdsfds@fdsf.ru", email2="123fdsfdg@dfds.ru",
                                   email3="123fdjjfdskl@fjdkjfkds.ru", homepage="123gjfdjhgdfjgkl", bday="15",
                                   bmonth="May", byear="1980", aday="21", amonth="September", ayear="1985",
                                   address2="123hgfhgfdgfdgdfgdfs", phone2="123gfdhsgfhgfhgfd",
                                   notes="123gfdsgfdgfdgdfsgfd"))
