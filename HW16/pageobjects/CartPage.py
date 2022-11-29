import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from HW16.pageobjects.BasePage import BasePage
from HW16.utils.PropertiesHandler import get_properties
from selenium.webdriver.remote.webdriver import WebDriver

LOGGER = logging.getLogger()


class CartPage(BasePage):

    def __init__(self, driver: WebDriver, url=f"{get_properties('url')}/cart.html"):
        super().__init__(driver, url)
        WebDriverWait(self.driver, 5).until(lambda wd: len(wd.find_elements(
            By.ID, Locators.TABLE_WITH_PRODUCTS)) != 0,
                                            message=f"Cart page was not loaded within 5 seconds")

    def assert_product_is_displayed_in_cart(self, expected_name: str, expected_price: str):
        """Asserting that product in the cart has correct name and price"""
        LOGGER.info(f"Asserting that in the cart there is product with name {expected_name} and price {expected_price}")
        actual_name_in_card = self.find_element((By.XPATH, Locators.PRODUCT_NAME_IN_CART))
        actual_price_in_card = self.find_element((By.XPATH, Locators.PRODUCT_PRICE_IN_CART))
        assert actual_name_in_card.text == expected_name, f"Incorrect name in the card. Expected: {expected_name} Actual: {actual_name_in_card.text} "
        assert actual_price_in_card.text == expected_price, f"Incorrect price in the card. Expected: {expected_price} Actual: {actual_price_in_card.text}"


class Locators:
    TABLE_WITH_PRODUCTS = "tbodyid"
    PRODUCT_NAME_IN_CART = "//tbody[@id='tbodyid']//td[2]"
    PRODUCT_PRICE_IN_CART = "//tbody[@id='tbodyid']//td[3]"