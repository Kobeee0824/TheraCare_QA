from pages.login_page import LoginPage
from pages.self_assessment_page import SelfAssessment

def test_moodtrack(driver):
    login = LoginPage(driver)
    selfassessment = SelfAssessment(driver)
    
    login.open_page()
    login.login("2023-004", "Test@1234")

    selfassessment.click_self_assessment_button()
    assert selfassessment.self_assessment_title() == "Self Assessment Test"


