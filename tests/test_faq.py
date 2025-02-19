import pytest
import allure
from pages.faq_page import FAQPage

@allure.suite("FAQ Tests")
class TestFAQ:
    @pytest.mark.parametrize("question_index", [0, 1, 2, 3, 4, 5, 6, 7])
    @allure.title("Проверка вопроса №{question_index} в разделе FAQ")
    @allure.description("Тест проверяет, что при нажатии на вопрос в разделе FAQ отображается ответ.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_faq_question(self, driver, question_index):
        with allure.step("Открытие страницы FAQ"):
            page = FAQPage(driver)

        page.scroll_to_faq_section()

        with allure.step(f"Нажатие на вопрос с индексом {question_index}"):
            page.click_question(question_index)

        with allure.step("Получение текста ответа"):
            answer_text = page.get_answer_text(question_index)
        with allure.step("Проверка, что ответ отображается"):
            assert answer_text != "", f"Ответ на вопрос с индексом {question_index} не отображается"