#  __author__ = 'Alexey Buchkin'
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.helper import Helper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.helper = Helper(self)

    def destroy(self):
        self.wd.quit()
