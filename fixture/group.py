#  __author__ = 'Alexey Buchkin'


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_tab()

    def fill_form(self, group):
        wd = self.app.wd
        self.change_field("group_name", group.name)
        self.change_field("group_header", group.header)
        self.change_field("group_footer", group.footer)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_tab()

    def select_first(self):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()

    def edit_first(self, group):
        wd = self.app.wd
        self.open_group_page()
        self.select_first()
        # submit edit
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_form(group)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.return_to_group_tab()

    def open_group_page(self):
        wd = self.app.wd
        # open group page
        wd.find_element_by_link_text("groups").click()

    def return_to_group_tab(self):
        wd = self.app.wd
        # return to group page
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))
