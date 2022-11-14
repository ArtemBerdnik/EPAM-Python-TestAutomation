from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from HW13.pages.BasePage import BasePage
from HW13.pages.InventoryPage import InventoryPage
from HW13.utils.PropertiesHandler import get_properties


class Locators:
    USERNAME_INPUT_FILED = By.ID, "user-name"
    PASSWORD_INPUT_FIELD = By.XPATH, "//input[@name='password']"
    SUBMIT_BUTTON = By.ID, "login-button"


class LoginPage(BasePage):

    def __init__(self, driver, url=f"{get_properties('url')}"):
        super().__init__(driver, url)

    def open_page(self, url=f"{get_properties('url')}"):
        super().open_page(url)
        return self

    def login(self) -> InventoryPage:
        self.find_element(Locators.USERNAME_INPUT_FILED).send_keys(get_properties('username'))
        self.find_element(Locators.PASSWORD_INPUT_FIELD).send_keys(get_properties('password'))
        self.find_element(Locators.SUBMIT_BUTTON).click()
        WebDriverWait(self.driver, 5).until(EC.url_to_be(f"{get_properties('url') + '/inventory.html'}"),
                                                  message=f"Could not login within 5 seconds")
        return InventoryPage(self.driver)
