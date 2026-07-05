from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class AppointmentPage(LoginPage):
    APPOINTMENT = (By.XPATH, "//span[normalize-space()='Appointments']")
    APPOINTMENT_TITLE = (By.XPATH, "//h2[@class='text-2xl font-bold mb-4']")

    def click_appointment(self):
        self.wait.until(
            EC.element_to_be_clickable(self.APPOINTMENT)
        ).click()

    def get_appointment_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.APPOINTMENT_TITLE)
        ).text
    

    