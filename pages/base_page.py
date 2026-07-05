# ganito siya since lahat ng pages is gagamitin siya (fixed)
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) #assign value sa wait

    def open(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title
    
