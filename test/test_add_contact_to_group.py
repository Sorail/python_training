#  __author__ = 'Alexey Buchkin'

from model.contact import Contact
from model.group import Group
import pytest
import random


def test_add_contact_to_group(app, orm, check_ui):
    with pytest.allure.step('Given check availability of at least one contract not in groups'):
        if len(orm.get_contacts_not_in_groups()) == 0:
            app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                                       nickname="nickname", title="title", company="company", address="address",
                                       home="+985445548", mobile="+98564545", work="+8984848", fax="+9854411",
                                       email="email@fdsf.ru", email2="email2@dfds.ru",
                                       email3="email3@fjdkjfkds.ru", homepage="homepage", bday="1",
                                       bmonth="December", byear="1970", aday="21", amonth="December", ayear="1971",
                                       address2="address2", phone2="+9845547848",
                                       notes="notes"))
    with pytest.allure.step('Given check availability of at least one group'):
        if len(orm.get_group_list()) == 0:
            app.group.create(Group(name="test1"))

    with pytest.allure.step('Given a contacts list not in groups'):
        contacts = orm.get_contacts_not_in_groups()
    with pytest.allure.step('Given a groups list'):
        groups = orm.get_group_list()
    with pytest.allure.step('Given a random contact from contacts: %s' % contacts):
        contact = random.choice(contacts)
    with pytest.allure.step('Given a random group from groups: %s' % groups):
        group = random.choice(groups)
    with pytest.allure.step('Given a contacts in a group: %s' % group):
        old_contact_in_group = orm.get_contacts_in_group(group)
    with pytest.allure.step('When I add contact: %s to group: %s' % (contact, group)):
        app.contact.add_group_by_id(contact, group)
    with pytest.allure.step('Then the new list contracts in group: %s is equal '
                            'to the old list with the added contact' % group):
        new_contact_in_group = orm.get_contacts_in_group(group)
        old_contact_in_group.append(contact)
        assert old_contact_in_group == new_contact_in_group
        if check_ui:
            assert sorted(new_contact_in_group,
                          key=Contact.id_or_max) == sorted(app.contact.get_contact_in_group_list(group),
                                                           key=Contact.id_or_max)
