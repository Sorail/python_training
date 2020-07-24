#  __author__ = 'Alexey Buchkin'
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.navigation import NavigationHelper


class Helper:

    def __init__(self, app):
        self.app = app
        self.wd = app.wd
        self.navigation = NavigationHelper(self)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

