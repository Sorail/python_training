#  __author__ = 'Alexey Buchkin'

from selenium.webdriver.support.ui import Select
from model.contact import Contact
from time import sleep


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_form(contact)
        wd.find_element_by_name("new_group").click()
        wd.find_element_by_xpath("//option[@value='[none]']").click()
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        sleep(5)

    def edit_first(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # select first contact for edit
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        self.fill_form(contact)
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

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

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            if "day" in field_name:
                wd.find_element_by_name(field_name).click()
                Select(wd.find_element_by_name(field_name)).select_by_visible_text("%s" % text)
                wd.find_element_by_xpath("(//option[@value='%s'])" % text).click()
            elif "month" in field_name:
                wd.find_element_by_name(field_name).click()
                Select(wd.find_element_by_name(field_name)).select_by_visible_text("%s" % text)
                wd.find_element_by_xpath("(//option[@value='%s'])" % text).click()
            elif "year" in field_name:
                wd.find_element_by_xpath("//input[@name='" + field_name + "']").click()
                wd.find_element_by_xpath("//input[@name='" + field_name + "']").clear()
                wd.find_element_by_xpath("//input[@name='" + field_name + "']").send_keys(text)
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

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contact_page()
        contacts = []
        for element in wd.find_elements_by_css_selector("tr[name='entry']"):
            contact_values = element.find_elements_by_css_selector("td")
            contact_firstname = contact_values[2]
            contact_lastname = contact_values[1]
            contact_id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=contact_firstname.text, lastname=contact_lastname.text, id=contact_id))
        return contacts
