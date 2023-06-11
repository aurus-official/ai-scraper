from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class Driver :
    def __init__(self, options, service):
        self.service = service
        self.options = options
        self.webdriver = None

    def add_option(self, argument):
        self.options.add_argument(argument)

    def set_webdriver(self):
        self.webdriver = webdriver.Chrome(options=self.options, service=self.service)

def driver():
    driver = Driver(Options(), Service())
    userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.100.0" 
    driver.add_option(f"user-agent={userAgent}")
    driver.add_option("--no-sandbox")
    driver.add_option('disable-notifications')
    driver.add_option("--headless")
    driver.set_webdriver()

    return driver
