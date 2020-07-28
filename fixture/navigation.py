#  __author__ = 'Alexey Buchkin'


class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        # open home page
        wd.get("http://localhost/addressbook/")
