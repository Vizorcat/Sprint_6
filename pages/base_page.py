from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    def get_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text

    def scroll_to_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)

    def switch_to_new_tab(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])

    def get_current_url(self):
        return self.driver.current_url