import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FAQPage(BasePage):
    QUESTION_LOCATORS = [
        (By.ID, 'accordion__heading-0'),
        (By.ID, 'accordion__heading-1'),
        (By.ID, 'accordion__heading-2'),
        (By.ID, 'accordion__heading-3'),
        (By.ID, 'accordion__heading-4'),
        (By.ID, 'accordion__heading-5'),
        (By.ID, 'accordion__heading-6'),
        (By.ID, 'accordion__heading-7')

    ]

    ANSWER_LOCATORS = [
        (By.ID, 'accordion__panel-0'),
        (By.ID, 'accordion__panel-1'),
        (By.ID, 'accordion__panel-2'),
        (By.ID, 'accordion__panel-3'),
        (By.ID, 'accordion__panel-4'),
        (By.ID, 'accordion__panel-5'),
        (By.ID, 'accordion__panel-6'),
        (By.ID, 'accordion__panel-7'),

    ]

    @allure.step("Прокрутка до раздела FAQ")
    def scroll_to_faq_section(self):
        self.scroll_to_element(self.QUESTION_LOCATORS[0])

    @allure.step("Нажатие на вопрос с индексом {index}")
    def click_question(self, index):
        self.click_element(self.QUESTION_LOCATORS[index])

    @allure.step("Получение текста ответа на вопрос с индексом {index}")
    def get_answer_text(self, index):
        return self.get_text(self.ANSWER_LOCATORS[index])