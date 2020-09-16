#  __author__ = 'Alexey Buchkin'

import re
import pytest
from random import randrange


def test_phones_on_home_page(app):
    with pytest.allure.step('Given a contact list from UI'):
        all_contact_from_home_page = app.contact.get_contact_list()
    with pytest.allure.step('Given info random contact from home page'):
        index = randrange(len(all_contact_from_home_page))
        contact_from_home_page = all_contact_from_home_page[index]
    with pytest.allure.step('Given a info from contact from edit page'):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    with pytest.allure.step('Then equal info from home page with info from edit page'):
        assert contact_from_home_page.firstname == contact_from_edit_page.firstname
        assert contact_from_home_page.lastname == contact_from_edit_page.lastname
        assert contact_from_home_page.address == contact_from_edit_page.address
        assert contact_from_home_page.all_emails_from_homepage == merge_emails_from_edit_page(contact_from_edit_page)
        assert contact_from_home_page.all_phones_from_homepage == merge_phones_from_edit_page(contact_from_edit_page)


def test_phones_on_view_page(app):
    with pytest.allure.step('Given a contact list from UI'):
        all_contact_from_home_page = app.contact.get_contact_list()
    with pytest.allure.step('Given info random contact from view page'):
        index = randrange(len(all_contact_from_home_page))
        contact_from_view_page = app.contact.get_contact_info_from_view_page(index)
    with pytest.allure.step('Given a info from contact from edit page'):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    with pytest.allure.step('Then equal info from view page with info from edit page'):
        assert contact_from_view_page.home == contact_from_edit_page.home
        assert contact_from_view_page.mobile == contact_from_edit_page.mobile
        assert contact_from_view_page.work == contact_from_edit_page.work
        assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_from_edit_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       (contact.home, contact.mobile, contact.work, contact.phone2)))))


def merge_emails_from_edit_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                      (contact.email, contact.email2, contact.email3))))
