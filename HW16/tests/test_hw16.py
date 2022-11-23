from HW16.pageobjects.MainPage import MainPage


def test_login(browser):
    MainPage(browser)\
        .open_page()\
        .click_login_button()\
        .assert_login_field_is_present()\
        .assert_password_field_is_present()\
        .login()\
        .assert_logout_button_is_present()\
        .assert_welcome_message_is_displayed()


def test_adding_products_to_cart(browser, get_main_page_after_login):
    monitors_page = get_main_page_after_login.navigate_to_monitors_page()
    most_expensive_monitor = monitors_page.find_the_most_expensive_monitor()

    most_expensive_monitor_page = monitors_page.open_specific_monitor_page(most_expensive_monitor['web_element'])
    most_expensive_monitor_page\
        .assert_correct_page_is_opened(most_expensive_monitor['monitor_name'], most_expensive_monitor['monitor_price'])\
        .add_monitor_to_cart()

    cart_page = get_main_page_after_login.navigate_to_card_page()
    cart_page.assert_product_is_displayed_in_cart(most_expensive_monitor['monitor_name'], most_expensive_monitor['monitor_price'])
