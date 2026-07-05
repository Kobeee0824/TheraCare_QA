from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LearningMaterials(LoginPage):

    LEARNING_MATERIALS = (By.XPATH, "//span[normalize-space()='Learning Materials']")
    LEARNING_MATERIALS_TITLE = (By. XPATH, "//h2[@class='text-2xl font-bold text-cyan-600']")

    def click_learning_materials(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LEARNING_MATERIALS)
        ).click()
    
    def get_learning_materials_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LEARNING_MATERIALS_TITLE)
        ).text
    
    