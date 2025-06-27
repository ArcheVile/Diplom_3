import allure
from .base_page import BasePage
from locators.profile_locators import ProfileLocators

class ProfilePage(BasePage):

    @allure.step("Открываем страницу профиля")
    def open(self):
        super().open("/account/profile")

    @allure.step("Выход из профиля")
    def logout(self):
        self.click_element(ProfileLocators.LOGOUT_BUTTON)

    @allure.step("Переход в историю заказов")
    def go_to_order_history(self):
        self.click_element(ProfileLocators.ORDER_HISTORY)

    @allure.step("Проверяем, что это страница профиля")
    def is_profile_page(self):
        return self.find_element(ProfileLocators.PROFILE_HEADER)

    @allure.step("Проверяем, что это страница истории заказов")
    def is_order_history_page(self):
        return "/account/orders" in self.get_current_url()
