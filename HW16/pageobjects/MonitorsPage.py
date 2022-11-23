import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from HW16.pageobjects.BasePage import BasePage
from selenium.webdriver.remote.webdriver import WebDriver

from HW16.pageobjects.SpecificProductPage import SpecificProductPage

LOGGER = logging.getLogger()


class MonitorsPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    ############################## Actions ##################################

    def open_specific_monitor_page(self, monitor: WebElement) -> SpecificProductPage:
        """Navigating to a specific monitor page"""
        LOGGER.info("Opening a specific monitor page")
        monitor.click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Locators.MONITOR_NAME)),
                                            message=f"Monitor page was not loaded within 5 seconds")
        return SpecificProductPage(self.driver, self.driver.current_url)

    def find_the_most_expensive_monitor(self) -> dict:
        """Method will identify the most expensive monitor on the page and return tuple consisted of
            1. WebElement
            2. Monitor title
            3. Monitor price
        """
        LOGGER.info("Searching for the most expensive monitor")
        all_monitors = self.find_elements((By.XPATH, Locators.ALL_MONITORS))
        most_expensive = max(all_monitors, key=lambda x: x.find_element(By.XPATH, f'.{Locators.PRODUCT_PRICE}').text[1:])
        most_expensive_name = most_expensive.find_element(By.XPATH, f'.{Locators.PRODUCT_NAME}').text
        most_expensive_price = most_expensive.find_element(By.XPATH, f'.{Locators.PRODUCT_PRICE}').text[1:]

        LOGGER.info(f"Most expensive monitor found. Name: {most_expensive_name}. Price: {most_expensive_price}")
        return {"web_element": most_expensive,
                "monitor_name": most_expensive_name,
                "monitor_price": most_expensive_price}


class Locators:
    TABLE_WITH_MONITORS = "#tbodyid"
    ALL_MONITORS = "//div[@id='tbodyid']//div[@class='col-lg-4 col-md-6 mb-4']"
    PRODUCT_PRICE = "//h5"
    PRODUCT_NAME = "//a[@class='hrefch']"
    MONITOR_NAME = "//h2[@class='name']"
