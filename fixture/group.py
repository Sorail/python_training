#  __author__ = 'Alexey Buchkin'

from model.group import Group


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
        self.group_cache = None

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
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_tab()
        self.group_cache = None

    def select_first(self):
        self.select_by_index(0)

    def select_by_index(self, index):
        wd = self.app.wd
        # select group
        wd.find_elements_by_name("selected[]")[index].click()

    def edit_first(self, group):
        self.edit_by_index(group, 0)

    def edit_by_index(self, group, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_by_index(index)
        # submit edit
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_form(group)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.return_to_group_tab()
        self.group_cache = None

    def open_group_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0:
            return
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

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.groups_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                group_id = element.find_element_by_name("selected[]").get_attribute("value")
                self.groups_cache.append(Group(name=text, id=group_id))

        return list(self.groups_cache)
