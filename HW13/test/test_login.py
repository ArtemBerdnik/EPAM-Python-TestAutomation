from HW13.pages.LoginPage import LoginPage


def test_login(browser):
    LoginPage(browser)\
        .open_page()\
        .login()\
        .assert_page_url()
