from pages.login_page import LoginPage
from pages.logout import Logout

def test_logout(driver):
    login = LoginPage(driver)
    logout = Logout(driver)

    login.open_page()
    login.login("2023-004", "Test@1234")

    logout.click_logout()
    assert logout.get_home_desc()