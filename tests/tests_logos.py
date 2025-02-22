import allure
from pages.main_page import MainPage

@allure.suite("Logo Tests")
class TestLogos:
    @allure.title("Проверка перехода по логотипу Самоката")
    @allure.severity(allure.severity_level.NORMAL)
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)

        with allure.step("Нажатие на логотип Самоката"):
            main_page.click_scooter_logo()

        with allure.step("Проверка, что URL соответствует главной странице"):
            assert main_page.get_current_url() == "https://qa-scooter.praktikum-services.ru/", "Логотип Самоката не ведет на главную страницу"

    @allure.title("Проверка перехода по логотипу Яндекса")
    @allure.severity(allure.severity_level.NORMAL)
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)

        with allure.step("Нажатие на логотип Яндекса"):
            main_page.click_yandex_logo()

        with allure.step("Ожидание новой вкладки"):
            main_page.switch_to_new_tab()

        with allure.step("Проверка, что URL содержит dzen.ru"):
            assert "dzen.ru" in main_page.get_current_url(), "Логотип Яндекса не ведет на главную страницу Дзена"