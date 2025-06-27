import allure
from .base_page import BasePage
from locators.feed_locators import FeedLocators

class FeedPage(BasePage):

    @allure.step("Открываем страницу ленты заказов")
    def open(self):
        super().open("/feed")

    @allure.step("Открываем детали заказа")
    def open_order_details(self):
        self.click_element(FeedLocators.ORDER_CARD)

    @allure.step("Проверяем, что модальное окно заказа отображается")
    def is_order_modal_visible(self):
        return self.find_element(FeedLocators.ORDER_MODAL).is_displayed()

    @allure.step("Закрываем модальное окно заказа")
    def close_order_modal(self):
        self.click_element(FeedLocators.CLOSE_MODAL_BUTTON)

    @allure.step("Проверяем, что модальное окно заказа закрыто")
    def is_order_modal_closed(self):
        return FeedLocators.ORDER_MODAL not in self.driver.page_source

    @allure.step("Получаем общее количество выполненных заказов")
    def get_total_orders_count(self):
        return int(self.get_element_text(FeedLocators.TOTAL_ORDERS))

    @allure.step("Получаем количество заказов, выполненных сегодня")
    def get_today_orders_count(self):
        return int(self.get_element_text(FeedLocators.TODAY_ORDERS))

    @allure.step("Проверяем, что последний заказ отображается в ленте")
    def latest_order_visible(self):
        return self.find_element(FeedLocators.ORDER_CARD).is_displayed()
