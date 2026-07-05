from pages.landing_page import LandingPage

def test_open_landing_page(driver):

    landing = LandingPage(driver)

    landing.open_page()

    assert landing.get_heading_text() == "TheraCare"
    