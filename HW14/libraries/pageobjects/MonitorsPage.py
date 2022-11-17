import time
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from HW14.libraries.variables import ALL_MONITORS, PRODUCT_PRICE, PRODUCT_NAME, TABLE_WITH_MONITORS


class Monitors:
    ROBOT_LIBRARY_SCOPE = 'SUITE'

    @staticmethod
    def wait_until_page_fully_loaded(timeout=5) -> None:
        """Waits until the table with monitors is loaded completely"""
        seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
        table = seleniumlib.get_webelement(TABLE_WITH_MONITORS)
        was_updated = True
        while was_updated and timeout > 0:
            if table.text is not None:
                was_updated = False
            time.sleep(1)
            timeout = timeout - 1
        if was_updated:
            raise Exception(f"Table with products was not populated within {timeout}")

    @staticmethod
    def find_the_most_expensive_monitor() -> dict:
        """Method will identify the most expensive monitor on the page and return tuple consisted of
            1. WebElement
            2. Monitor title
            3. Monitor price
        """
        seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
        all_monitors = seleniumlib.get_webelements(ALL_MONITORS)
        most_expensive = max(all_monitors, key=lambda x: x.find_element(By.XPATH, f'.{PRODUCT_PRICE}').text[1:])

        return {"web_element": most_expensive,
                "monitor_name": most_expensive.find_element(By.XPATH, f'.{PRODUCT_NAME}').text,
                "monitor_price": most_expensive.find_element(By.XPATH, f'.{PRODUCT_PRICE}').text[1:]}
