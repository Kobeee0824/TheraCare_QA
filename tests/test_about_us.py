from pages.login_page import LoginPage
from pages.about_us_page import AboutUs

def test_about_us(driver):
    login = LoginPage(driver)
    about_us = AboutUs(driver)

    login.open_page()
    login.login("2023-004", "Test@1234")

    about_us.click_about_us()
    assert about_us.get_about_us_title() == "About TheraCare"