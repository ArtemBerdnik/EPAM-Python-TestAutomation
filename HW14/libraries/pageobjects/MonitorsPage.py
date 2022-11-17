from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from HW14.libraries.variables import ALL_MONITORS, PRODUCT_PRICE, PRODUCT_NAME


class Monitors:
    ROBOT_LIBRARY_SCOPE = 'SUITE'

    @staticmethod
    def find_the_most_expensive_monitor() -> tuple:
        """Method will identify the most expensive monitor on the page and return tuple consisted of
            1. WebElement
            2. Monitor title
            3. Monitor price
        """
        seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
        all_monitors = seleniumlib.get_webelements(ALL_MONITORS)
        most_expensive = max(all_monitors, key=lambda x: x.find_element(By.XPATH, f'.{PRODUCT_PRICE}').text[1:])

        return (most_expensive, most_expensive.find_element(By.XPATH, f'.{PRODUCT_NAME}').text,
                most_expensive.find_element(By.XPATH, f'.{PRODUCT_PRICE}').text[1:])
