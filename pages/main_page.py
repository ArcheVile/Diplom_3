import allure
from .base_page import BasePage
from locators.main_locators import MainLocators

class MainPage(BasePage):

    @allure.step("Открываем главную страницу")
    def open(self):
        super().open("/")

    @allure.step("Переход в профиль")
    def go_to_profile(self):
        self.click_element(MainLocators.PROFILE_BUTTON)

    @allure.step("Переход в конструктор")
    def go_to_constructor(self):
        self.click_element(MainLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Переход в ленту заказов")
    def go_to_feed(self):
        self.click_element(MainLocators.FEED_BUTTON)

    @allure.step("Открытие модального окна ингредиента")
    def open_ingredient_modal(self):
        self.click_element(MainLocators.INGREDIENT)

    @allure.step("Проверка, что модальное окно ингредиента отображается")
    def is_ingredient_modal_visible(self):
        return self.find_element(MainLocators.INGREDIENT_MODAL).is_displayed()

    @allure.step("Закрытие модального окна ингредиента")
    def close_ingredient_modal(self):
        self.click_element(MainLocators.CLOSE_MODAL_BUTTON)

    @allure.step("Проверка, что модальное окно ингредиента закрыто")
    def is_ingredient_modal_closed(self):
        return MainLocators.INGREDIENT_MODAL not in self.driver.page_source

    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient_to_order(self):
        self.click_element(MainLocators.INGREDIENT)

    @allure.step("Получение счётчика ингредиента")
    def get_ingredient_counter(self):
        try:
            return int(self.get_element_text(MainLocators.INGREDIENT_COUNTER))
        except:
            return 0

    @allure.step("Нажатие на кнопку заказа")
    def click_order_button(self):
        self.click_element(MainLocators.ORDER_BUTTON)

    @allure.step("Проверка, что заказ успешно создан")
    def order_success_visible(self):
        return self.find_element(MainLocators.ORDER_SUCCESS).is_displayed()

    @allure.step("Проверка, что мы находимся на странице конструктора")
    def is_constructor_page(self):
        return "constructor" in self.get_current_url()

    @allure.step("Проверка, что мы находимся на странице ленты заказов")
    def is_feed_page(self):
        return "feed" in self.get_current_url()
