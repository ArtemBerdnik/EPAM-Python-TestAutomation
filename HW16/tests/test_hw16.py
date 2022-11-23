from HW16.pageobjects.MainPage import MainPage


def test_login(browser):
    # 1. Open main page
    main_page = MainPage(browser).open_page()

    # 2. Click login button and assert there are inputs for login field and password
    main_page.click_login_button()
    main_page.assert_login_field_is_present()
    main_page.assert_password_field_is_present()

    # 3. Login with valid credential and assert that welcome message is displayed for user as long as logout button
    main_page.login()
    main_page.assert_logout_button_is_present()
    main_page.assert_welcome_message_is_displayed()


def test_adding_products_to_cart(browser, get_main_page_after_login):
    # 1. Open 'Monitors' page and find the most expensive monitor there
    monitors_page = get_main_page_after_login.navigate_to_monitors_page()
    most_expensive_monitor = monitors_page.find_the_most_expensive_monitor()

    # 2. Navigate to details page of a most expensive monitor and assert that correct name and price are displayed
    most_expensive_monitor_page = monitors_page.open_specific_monitor_page(most_expensive_monitor['web_element'])
    most_expensive_monitor_page.assert_correct_page_is_opened(most_expensive_monitor['monitor_name'],
                                                              most_expensive_monitor['monitor_price'])

    # 3. Add the monitor to a cart
    most_expensive_monitor_page.add_monitor_to_cart()

    # 4. Navigate to cart page and assert that monitor information is correct in there
    cart_page = get_main_page_after_login.navigate_to_card_page()
    cart_page.assert_product_is_displayed_in_cart(most_expensive_monitor['monitor_name'],
                                                  most_expensive_monitor['monitor_price'])
