from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LandingPage(BasePage):

    URL = "https://theracareweb.online/landing.php"

    HEADING = (
        By.XPATH,
        "//div[@class='text-3xl font-bold mx-auto md:mx-0 text-blue-900']"
    )

    def open_page(self):
        self.open(self.URL)

        self.wait.until(
            EC.visibility_of_element_located(self.HEADING)
        )

    def get_heading_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.HEADING)
        ).text
    
    