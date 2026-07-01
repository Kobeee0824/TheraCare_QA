from selenium.webdriver.common.by import By

class LoginPage:
    URL = "https://theracareweb.online/landing.php"

    GET_STARTED = (By.ID,"get-started-btn")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By. CSS_SELECTOR, "button[class='swal2-confirm bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded mr-6']")
    MESSAGE = (By. CSS_SELECTOR, ".text-2xl.font-bold.mb-4")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(*self.GET_STARTED).click()
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()

    def get_message(self):
        return self.driver.find_element(*self.MESSAGE).text