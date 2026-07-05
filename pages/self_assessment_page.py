from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class SelfAssessment(LoginPage):
    SELF_ASSESSMENT_BUTTON = (By. CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(2) > main:nth-child(2) > section:nth-child(2) > div:nth-child(2) > article:nth-child(4) > a:nth-child(4) > button:nth-child(1)")
    SELF_ASSESSMENT_TITLE = (By. CSS_SELECTOR, ".text-3xl.font-bold")

    def click_self_assessment_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SELF_ASSESSMENT_BUTTON)
        ).click()
    
    def self_assessment_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SELF_ASSESSMENT_TITLE)
        ).text
    
    