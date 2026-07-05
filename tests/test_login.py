from pages.login_page import LoginPage

def test_valid_login(driver):

    login = LoginPage(driver)

    login.open_page()

    login.login(
        "2023-004",
        "Test@1234"
    )

    assert login.get_services_heading() == "Our Services"