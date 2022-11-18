import time

from robot.libraries.BuiltIn import BuiltIn

from HW14.libraries.variables import TABLE_WITH_PRODUCTS


class CartPage:
    ROBOT_LIBRARY_SCOPE = 'SUITE'

    @staticmethod
    def wait_until_table_is_loaded(timeout=5) -> None:
        """Waits until the table with orders in loaded completely"""
        seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
        table = seleniumlib.get_webelement(TABLE_WITH_PRODUCTS)
        was_updated = True
        while was_updated and timeout > 0:
            if table.text is not None:
                was_updated = False
            time.sleep(1)
            timeout = timeout - 1
        if was_updated:
            raise Exception(f"Table with products was not populated within {timeout}")

