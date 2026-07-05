from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MoodTrackPage(BasePage):

    MOODTRACK_BUTTON = (By. CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(2) > main:nth-child(2) > section:nth-child(2) > div:nth-child(2) > article:nth-child(2) > a:nth-child(4) > button:nth-child(1)")
    MOODTRACK_HEADING = (By. CSS_SELECTOR, ".text-3xl.font-bold.text-blue-900")

    def click_moodtrack(self):
        self.wait.until(
            EC.element_to_be_clickable(self.MOODTRACK_BUTTON)
        ).click()

    def get_moodtrack_heading(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.MOODTRACK_HEADING)
        ).text
        