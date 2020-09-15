#  __author__ = 'Alexey Buchkin'

from selenium.webdriver.support.ui import Select
from model.contact import Contact
from time import sleep
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("new_group").click()
        wd.find_element_by_xpath("//option[@value='[none]']").click()
        self.fill_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        # select contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None
        sleep(3)

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        # select contact
        wd.find_element_by_xpath("//input[@id='%s']" % id).click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None
        sleep(3)

    def edit_first(self, contact):
        self.edit_by_index(contact, 0)

    def edit_by_index(self, contact, index):
        wd = self.app.wd
        self.open_edit_by_index(index)
        self.fill_form(contact)
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_by_id(self, contact, id):
        wd = self.app.wd
        self.open_edit_by_id(id)
        self.fill_form(contact)
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        # select contact for edit
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

    def open_edit_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        # select contact for edit
        wd.find_element_by_xpath(("//input[@id='%s']//..//..//img[@title='Edit']" % id)).click()

    def open_details_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        # select contact for view
        wd.find_elements_by_xpath("//img[@title='Details']")[index].click()

    def fill_form(self, contact):
        wd = self.app.wd
        # fill contact form
        self.change_field("firstname", contact.firstname)
        self.change_field("middlename", contact.middlename)
        self.change_field("lastname", contact.lastname)
        self.change_field("nickname", contact.nickname)
        self.change_field("title", contact.title)
        self.change_field("company", contact.company)
        self.change_field("address", contact.address)
        self.change_field("home", contact.home)
        self.change_field("mobile", contact.mobile)
        self.change_field("work", contact.work)
        self.change_field("fax", contact.fax)
        self.change_field("email", contact.email)
        self.change_field("email2", contact.email2)
        self.change_field("email3", contact.email3)
        self.change_field("homepage", contact.homepage)
        self.change_field("bday", contact.bday)
        self.change_field("bmonth", contact.bmonth)
        self.change_field("byear", contact.byear)
        self.change_field("aday", contact.aday)
        self.change_field("amonth", contact.amonth)
        self.change_field("ayear", contact.ayear)
        self.change_field("address2", contact.address2)
        self.change_field("phone2", contact.phone2)
        self.change_field("notes", contact.notes)
        self.change_field("new_group", contact.group)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            if "day" in field_name:
                wd.find_element_by_name(field_name).click()
                # Select(wd.find_element_by_name(field_name)).select_by_visible_text("%s" % text)
                wd.find_element_by_xpath("(//select[@name='%s']/option[@value='%s'])" % (field_name, text)).click()
            elif "month" in field_name:
                wd.find_element_by_name(field_name).click()
                Select(wd.find_element_by_name(field_name)).select_by_visible_text("%s" % text)
                wd.find_element_by_xpath("(//select[@name='%s']/option[text()='%s'])" % (field_name, text)).click()
            elif "year" in field_name:
                wd.find_element_by_xpath("//input[@name='%s']" % field_name).click()
                wd.find_element_by_xpath("//input[@name='%s']" % field_name).clear()
                wd.find_element_by_xpath("//input[@name='%s']" % field_name).send_keys(text)
            elif "group" in field_name:
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_xpath("(//select[@name='%s']/option[@value='%s'])" % (field_name, text.id)).click()
            else:
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)

    def return_to_home_page(self):
        wd = self.app.wd
        # return to home page
        wd.find_element_by_link_text("home page").click()

    def open_contact_page(self):
        wd = self.app.wd
        if (wd.current_url.endswith("") or wd.current_url.endswith("/index.php")) \
                and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0:
            return
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                contact_values = element.find_elements_by_css_selector("td")
                contact_firstname = contact_values[2].text
                contact_lastname = contact_values[1].text
                contact_id = element.find_element_by_name("selected[]").get_attribute("value")
                contact_address = contact_values[3].text
                contact_all_emails = contact_values[4].text
                contact_all_phones = contact_values[5].text
                self.contact_cache.append(Contact(firstname=contact_firstname, lastname=contact_lastname, id=contact_id,
                                                  address=contact_address, all_emails_from_homepage=contact_all_emails,
                                                  all_phones_from_homepage=contact_all_phones))
        return list(self.contact_cache)

    def get_contact_in_group_list(self, group):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            wd.find_element_by_xpath("//select[@name='group']").click()
            wd.find_element_by_xpath("(//select[@name='group']/option[@value='%s'])" % group.id).click()
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                contact_values = element.find_elements_by_css_selector("td")
                contact_firstname = contact_values[2].text
                contact_lastname = contact_values[1].text
                contact_id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=contact_firstname,
                                                  lastname=contact_lastname, id=contact_id))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home=home, mobile=mobile, work=work,
                       phone2=phone2, address=address, email=email, email2=email2, email3=email3)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_details_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        id = re.search('(id=)(.*)',  wd.current_url).group(2)
        return Contact(id=id, home=home, mobile=mobile, work=work, phone2=phone2)

    def add_group_to_contract(self, contact, id):
        wd = self.app.wd
        self.open_edit_by_id(id)
        self.fill_form(contact)
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def add_group_by_id(self, contract, group):
        wd = self.app.wd
        self.open_contact_page()
        # select contact
        wd.find_element_by_xpath("//input[@id='%s']" % contract.id).click()
        # select group
        wd.find_element_by_xpath("//select[@name='to_group']").click()
        wd.find_element_by_xpath("(//select[@name='to_group']/option[@value='%s'])" % group.id).click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Add to']").click()
        self.contact_cache = None

    def del_group_by_id(self, contract, group):
        wd = self.app.wd
        self.open_contact_page()
        # select group
        wd.find_element_by_xpath("//select[@name='group']").click()
        wd.find_element_by_xpath("(//select[@name='group']/option[@value='%s'])" % group.id).click()
        # select contact
        wd.find_element_by_xpath("//input[@id='%s']" % contract.id).click()
        # submit deletion
        wd.find_element_by_xpath("//input[@name='remove']").click()
        self.contact_cache = None
