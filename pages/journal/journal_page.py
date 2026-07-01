from selenium.webdriver.common.by import By

class JournalPage:
    def __init__(self, driver):
        self.driver = driver

    #LOCATORS
    journal_btn = (By.XPATH, "//a[@href='journal.php']//button[@class='mt-auto bg-blue-900 text-white text-sm font-semibold py-2 px-4 rounded-md hover:bg-blue-800 transition'][normalize-space()='Get Started']")
    add_journal = (By.XPATH, "//button[@class='add-journal-btn']")
    add_title = (By.XPATH, "//input[@id='journal-title']")
    add_notes = (By.XPATH, "//textarea[@id='journal-body']")
    save_notes = (By.XPATH, "//button[@class='btn-save']")

    def add_journal_entry(self):
        self.driver.find_element(*self.journal_btn).click()

    def create_journal(self, title, content):
        self.driver.find_element(*self.add_journal).click()
        self.driver.find_element(*self.add_title).send_keys(title)
        self.driver.find_element(*self.add_notes).send_keys(content)
        self.driver.find_element(*self.save_notes).click()

