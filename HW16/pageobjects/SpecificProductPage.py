import logging

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from HW16.pageobjects.BasePage import BasePage
from selenium.webdriver.remote.webdriver import WebDriver

LOGGER = logging.getLogger()


class SpecificProductPage(BasePage):
    def __init__(self, driver: WebDriver, url: str):
        super().__init__(driver, url)

    ############################## Actions ##################################

    def add_monitor_to_cart(self):
        """Adding a specific monitor to a cart"""
        LOGGER.info("Clicking 'Add to Cart' button")
        add_to_card_button = self.find_element((By.XPATH, Locators.ADD_TO_CARD_BUTTON))
        add_to_card_button.click()

        LOGGER.info("Waiting until alert is displayed")
        WebDriverWait(self.driver, 5).until(EC.alert_is_present(),
                                            message=f"Alert was not present within 5 seconds")
        LOGGER.info("Accepting alert")
        Alert(self.driver).accept()
        return self

    ############################## Asserts ##################################

    def assert_correct_page_is_opened(self, expected_name: str, expected_price: str):
        """Asserting product page has correct name and price"""
        LOGGER.info(f"Asserting monitor with name {expected_name} has price {expected_price}")
        product_name_on_page = self.find_element((By.CSS_SELECTOR, Locators.PRODUCT_NAME_ON_PRODUCT_PAGE))
        product_price_on_page = self.find_element((By.CSS_SELECTOR, Locators.PRODUCT_PRICE_ON_PRODUCT_PAGE))
        assert expected_name == product_name_on_page.text, f"Incorrect name. Expected: {expected_name}\n" \
                                                           f"Actual: {product_name_on_page.text}"
        assert f"${expected_price} *includes tax" == product_price_on_page.text, f"Incorrect price. " \
                                                                                 f"Expected: {expected_price}  *includes tax" \
                                                                                 f"Actual: product_price_on_page.text"
        return self


class Locators:
    PRODUCT_CONTENT = "//div[@class='product-content product-wrap clearfix product-deatil']"
    PRODUCT_NAME_ON_PRODUCT_PAGE = "h2[class='name']"
    PRODUCT_PRICE_ON_PRODUCT_PAGE = "h3[class='price-container']"
    ADD_TO_CARD_BUTTON = "//a[text()='Add to cart']"
