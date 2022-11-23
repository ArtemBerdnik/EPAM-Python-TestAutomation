import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from HW16.pageobjects.MainPage import MainPage


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def get_main_page_after_login(browser):
    main_page = MainPage(browser).open_page()
    main_page.click_login_button()
    main_page.login()
    yield main_page


