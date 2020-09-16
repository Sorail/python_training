#  __author__ = 'Alexey Buchkin'

from model.contact import Contact
from model.group import Group
import pytest
import random


def test_del_contact_from_group(app, orm, check_ui):
    with pytest.allure.step('Given check availability of at least one group'):
        if len(orm.get_group_list()) == 0:
            app.group.create(Group(name="test1"))
    with pytest.allure.step('Given a random group from group'):
        group = random.choice(orm.get_group_list())
    with pytest.allure.step('Given check availability of at least one contract in groups'):
        if len(orm.get_contacts_in_groups()) == 0:
            app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                                       nickname="nickname", title="title", company="company", address="address",
                                       home="+985445548", mobile="+98564545", work="+8984848", fax="+9854411",
                                       email="email@fdsf.ru", email2="email2@dfds.ru",
                                       email3="email3@fjdkjfkds.ru", homepage="homepage", bday="1",
                                       bmonth="December", byear="1970", aday="21", amonth="December", ayear="1971",
                                       address2="address2", phone2="+9845547848",
                                       notes="notes", group=group))
    with pytest.allure.step('Given a contacts list in groups'):
        contacts = orm.get_contacts_in_groups()
    with pytest.allure.step('Given a random contact from contacts: %s' % contacts):
        contact = random.choice(contacts)
    with pytest.allure.step('Given a group from contact: %s' % contact):
        group = orm.get_group_from_contract(contact)[0]
    with pytest.allure.step('Given a contacts in a group: %s' % group):
        old_contact_in_group = orm.get_contacts_in_group(group)
    with pytest.allure.step('When I delete contact: %s from group: %s' % (contact, group)):
        app.contact.del_group_by_id(contact, group)
    with pytest.allure.step('Then the new list contracts is equal to the old '
                            'list with the remove group from contact %s: ' % contact):
        new_contact_in_group = orm.get_contacts_in_group(group)
        old_contact_in_group.remove(contact)
        assert old_contact_in_group == new_contact_in_group
        if check_ui:
            assert sorted(new_contact_in_group,
                          key=Contact.id_or_max) == sorted(app.contact.get_contact_in_group_list(group),
                                                           key=Contact.id_or_max)
