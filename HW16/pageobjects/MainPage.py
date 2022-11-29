import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from HW16.pageobjects.BasePage import BasePage
from selenium.webdriver.remote.webdriver import WebDriver

from HW16.pageobjects.CartPage import CartPage
from HW16.pageobjects.MonitorsPage import MonitorsPage
from HW16.utils.PropertiesHandler import get_properties

LOGGER = logging.getLogger()


class MainPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    ############################## Actions ##################################

    def open_page(self, url=f"{get_properties('url')}"):
        super().open_page(url)
        return self

    def click_login_button(self):
        """Clicking Login button on the main page"""
        LOGGER.info("Clicking 'Login' button")
        login_button = self.find_element((By.ID, Locators.LOGIN_BUTTON))
        login_button.click()
        LOGGER.info("Waiting until login form is loaded")
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, Locators.USERNAME_INPUT_FIELD)),
                                            message=f"Could not login within 5 seconds")
        return self

    def login(self):
        """log in with valid credentials"""
        username_input = self.find_element((By.ID, Locators.USERNAME_INPUT_FIELD))
        password_input = self.find_element((By.ID, Locators.PASSWORD_INPUT_FIELD))
        LOGGER.info(f"Specifying username as {get_properties('username')} and password as ***")
        username_input.send_keys(get_properties('username'))
        password_input.send_keys(get_properties('password'))
        login_button_in_popup = self.find_element((By.CSS_SELECTOR, Locators.LOGIN_BUTTON_IN_LOGIN_POPUP))
        LOGGER.info("Clicking 'Login' button in log in popup")
        login_button_in_popup.click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, Locators.LOGOUT_BUTTON)),
                                            message=f"Could not login within 5 seconds")
        return self

    def navigate_to_monitors_page(self) -> MonitorsPage:
        """Opening Monitors page"""
        LOGGER.info("Open 'Monitors' page")
        all_products_on_page = self.find_elements((By.XPATH, Locators.ALL_PRODUCTS_ON_PAGE))
        monitors_button = self.find_element((By.XPATH, Locators.MONITORS_BUTTON))
        monitors_button.click()

        LOGGER.info("Waiting until monitors page is completely loaded")
        WebDriverWait(self.driver, 5).until(lambda wd: len(wd.find_elements(
            By.XPATH, Locators.ALL_PRODUCTS_ON_PAGE)) != len(all_products_on_page),
                                            message=f"Monitors page was not loaded within 5 seconds")
        return MonitorsPage(self.driver)

    def navigate_to_card_page(self) -> CartPage:
        """Opening Cart page"""
        LOGGER.info("Open 'Cart' page")
        cart_page = self.find_element((By.ID, Locators.CART_BUTTON))
        cart_page.click()
        return CartPage(self.driver)

    ############################## Asserts ##################################

    def assert_login_field_is_present(self):
        """Asserting that there is login input field in login popup"""
        LOGGER.info(f"Asserting Login field is present")
        self.assert_element_is_present(By.ID, Locators.USERNAME_INPUT_FIELD)
        return self

    def assert_password_field_is_present(self):
        """Asserting that there is password input field in login popup"""
        LOGGER.info(f"Asserting Password field is present")
        self.assert_element_is_present(By.ID, Locators.PASSWORD_INPUT_FIELD)
        return self

    def assert_logout_button_is_present(self):
        """Asserting that there is logout button on the page"""
        LOGGER.info(f"Asserting Logout button is present")
        self.assert_element_is_present(By.ID, Locators.LOGOUT_BUTTON)
        return self

    def assert_welcome_message_is_displayed(self):
        """Asserting there is a welcome message on the page"""
        LOGGER.info(f"Asserting welcome message text")
        message = self.find_element((By.ID, Locators.WELCOME_MESSAGE_TEST))
        assert message.text == f"Welcome {get_properties('username')}", f"Incorrect message {message.text}"


class Locators:
    LOGIN_BUTTON = "login2"
    LOGIN_POPUP = "logInModalLabel"
    USERNAME_INPUT_FIELD = "loginusername"
    PASSWORD_INPUT_FIELD = "loginpassword"
    LOGIN_BUTTON_IN_LOGIN_POPUP = "div[id='logInModal'] button[class='btn btn-primary']"
    LOGOUT_BUTTON = "logout2"
    WELCOME_MESSAGE_TEST = "nameofuser"
    MONITORS_BUTTON = "//a[text()='Monitors']"
    ALL_PRODUCTS_ON_PAGE = "//div[@id='tbodyid']//div[@class='col-lg-4 col-md-6 mb-4']"
    CART_BUTTON = "cartur"
