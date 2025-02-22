import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.suite("Order Flow Tests")
class TestOrder:
    @pytest.mark.parametrize("order_data", [
        {"name": "Иван", "lastname": "Иванов", "address": "Москва, ул. Ленина, 1", "metro_station": "Белорусская", "phone": "+79000000000"},
        {"name": "Мария", "lastname": "Петрова", "address": "Санкт-Петербург, ул. Пушкина, 2", "metro_station": "Сенная площадь", "phone": "+79111111111"}
    ])
    @allure.title("Проверка процесса заказа самоката через верхнюю кнопку")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_top_button(self, driver, order_data):
        main_page = MainPage(driver)

        with allure.step("Нажатие на верхнюю кнопку заказа"):
            main_page.click_top_order_button()

        order_page = OrderPage(driver)
        order_page.process_order(order_data)

    @pytest.mark.parametrize("order_data", [
        {"name": "Иван", "lastname": "Иванов", "address": "Москва, ул. Ленина, 1", "metro_station": "Белорусская", "phone": "+79000000000"},
        {"name": "Мария", "lastname": "Петрова", "address": "Санкт-Петербург, ул. Пушкина, 2", "metro_station": "Сенная площадь", "phone": "+79111111111"}
    ])
    @allure.title("Проверка процесса заказа самоката через нижнюю кнопку")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_bottom_button(self, driver, order_data):
        main_page = MainPage(driver)

        with allure.step("Нажатие на нижнюю кнопку заказа"):
            main_page.click_bottom_order_button()

        order_page = OrderPage(driver)
        order_page.process_order(order_data)