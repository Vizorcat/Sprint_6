from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class MainPage(BasePage):
    TOP_ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')
    BOTTOM_ORDER_BUTTON = (By.CLASS_NAME, 'Button_Middle__1CSJM')

    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')

    @allure.step("Нажать на верхнюю кнопку заказа")
    def click_top_order_button(self):
        self.click_element(self.TOP_ORDER_BUTTON)

    @allure.step("Нажать на нижнюю кнопку заказа")
    def click_bottom_order_button(self):
        self.click_element(self.BOTTOM_ORDER_BUTTON)

    @allure.step("Кликнуть на логотип самоката")
    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)