from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class OrderPage(BasePage):
    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    LASTNAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    METRO_DROPDOWN_OPTION = (By.CLASS_NAME, 'select-search__option')
    PHONE_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.CLASS_NAME, 'Button_Middle__1CSJM')

    SUCCESS_MODAL = (By.CLASS_NAME, 'Order_Header__BZXOb')

    def fill_order_form(self, name, lastname, address, phone, metro_station=None):
        self.find_element(self.NAME_INPUT).send_keys(name)
        self.find_element(self.LASTNAME_INPUT).send_keys(lastname)
        self.find_element(self.ADDRESS_INPUT).send_keys(address)

        if metro_station:
            metro_input = self.find_element(self.METRO_INPUT)
            metro_input.send_keys(metro_station)
            metro_input.send_keys(Keys.ARROW_DOWN)
            metro_input.send_keys(Keys.ENTER)

        self.find_element(self.PHONE_INPUT).send_keys(phone)

    def click_next_button(self):
        self.click_element(self.NEXT_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MODAL)