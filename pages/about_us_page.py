from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class AboutUs(LoginPage):
    ABOUT_US = (By.XPATH, "//span[normalize-space()='About Us']")
    ABOUT_US_TITLE = (By.XPATH, "//h3[@class='text-xl font-bold mb-4']")

    def click_about_us(self):
        self.wait.until(
            EC.element_to_be_clickable(self.ABOUT_US)
        ).click()

    def get_about_us_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ABOUT_US_TITLE)
        ).text
    
    