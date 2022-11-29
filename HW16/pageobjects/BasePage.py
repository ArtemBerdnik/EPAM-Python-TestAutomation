from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from HW16.utils.PropertiesHandler import get_properties


class BasePage:

    def __init__(self, driver: WebDriver, url=f"{get_properties('url')}"):
        self.driver = driver
        self.url = url

    def find_element(self, locator: tuple, timeout=10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def find_elements(self, locator: tuple, timeout=10) -> List[WebElement]:
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def assert_element_is_present(self, how_to_locate: By, locator: str):
        if self.find_element((how_to_locate, locator)):
            assert True
        else:
            assert False, f"There is no element on the page located by {how_to_locate}:{locator}"

    def open_page(self, url: str):
        return self.driver.get(url)
