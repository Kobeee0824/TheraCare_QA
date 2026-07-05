from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Logout(LoginPage):
    LOGOUT = (By.XPATH, "//a[@href='logout.php']")
    HOME_DESC = (By.XPATH, "//p[@class='text-lg text-blue-900 mb-8']")

    def click_logout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT)
        ).click()
    
    def get_home_desc(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.HOME_DESC)
        )
    
    