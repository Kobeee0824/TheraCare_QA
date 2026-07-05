from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    URL = "https://theracareweb.online/landing.php"

    GET_STARTED = (By.CSS_SELECTOR, "#get-started-btn")
    USERNAME = (By.CSS_SELECTOR, "#username")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "button.swal2-confirm.bg-blue-600.hover\\:bg-blue-700.text-white.px-4.py-2.rounded.mr-6"
    )

    OUR_SERVICES = (
        By.XPATH,
        "//h2[@class='text-2xl font-bold mb-4']"
    )

    def open_page(self):
        self.open(self.URL)

    def click_get_started(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.GET_STARTED)
        ).click()

    def enter_username(self, username):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.USERNAME)
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.PASSWORD)
        ).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()


    # PINAG-ISA MO YUNG MGA NASA TAAS AT NILAGAY SA ISANG FUNCTION PARA ISANG TAWAGAN NALANG PAG GINAMIT SA IBANG FILE
    def login(self, username, password):
        self.click_get_started()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_services_heading(self):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.OUR_SERVICES)
        ).text