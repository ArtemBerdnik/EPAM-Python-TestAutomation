from HW13.pages.BasePage import BasePage
from HW13.utils.PropertiesHandler import get_properties


class InventoryPage(BasePage):

    def __init__(self, driver, url=f"{get_properties('url') + '/inventory.html'}"):
        super().__init__(driver, url)

    def assert_page_url(self):
        assert self.driver.current_url == f"{get_properties('url') + '/inventory.html'}"
