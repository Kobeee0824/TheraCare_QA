from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class JournalPage(BasePage):

    JOURNAL_BUTTON = (
        By.CSS_SELECTOR,
        "body > div:nth-child(1) > div:nth-child(2) > main:nth-child(2) > section:nth-child(2) > div:nth-child(2) > article:nth-child(1) > a:nth-child(4) > button:nth-child(1)"
    )

    JOURNAL_HEADING = (
        By.XPATH,
        "//h1[@class='text-3xl font-bold text-blue-900']"     
    )

    def click_journal(self):
        self.wait.until(
            EC.element_to_be_clickable(self.JOURNAL_BUTTON)
        ).click()

    def get_journal_heading(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.JOURNAL_HEADING)
        ).text