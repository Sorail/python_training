#  __author__ = 'Alexey Buchkin'

from model.contact import Contact
from model.group import Group

import random


def test_del_contact_from_group(app, orm, check_ui):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test1"))
    group = random.choice(orm.get_group_list())
    if len(orm.get_contacts_in_groups()) == 0:
        app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                                   nickname="nickname", title="title", company="company", address="address",
                                   home="+985445548", mobile="+98564545", work="+8984848", fax="+9854411",
                                   email="email@fdsf.ru", email2="email2@dfds.ru",
                                   email3="email3@fjdkjfkds.ru", homepage="homepage", bday="1",
                                   bmonth="December", byear="1970", aday="21", amonth="December", ayear="1971",
                                   address2="address2", phone2="+9845547848",
                                   notes="notes", group=group))
    contacts = orm.get_contacts_in_groups()
    contact = random.choice(contacts)
    group = orm.get_group_from_contract(contact)[0]
    old_contact_in_group = orm.get_contacts_in_group(group)
    app.contact.del_group_by_id(contact, group)
    new_contact_in_group = orm.get_contacts_in_group(group)
    old_contact_in_group.remove(contact)
    assert old_contact_in_group == new_contact_in_group
    if check_ui:
        assert sorted(new_contact_in_group,
                      key=Contact.id_or_max) == sorted(app.contact.get_contact_in_group_list(group),
                                                       key=Contact.id_or_max)
