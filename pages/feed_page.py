from .base_page import BasePage
from locators.feed_locators import FeedLocators

class FeedPage(BasePage):
    def open(self):
        super().open("/feed")

    def open_order_details(self):
        self.click_element(FeedLocators.ORDER_CARD)

    def is_order_modal_visible(self):
        return self.find_element(FeedLocators.ORDER_MODAL).is_displayed()

    def close_order_modal(self):
        self.click_element(FeedLocators.CLOSE_MODAL_BUTTON)

    def is_order_modal_closed(self):
        return FeedLocators.ORDER_MODAL not in self.driver.page_source

    def get_total_orders_count(self):
        return int(self.get_element_text(FeedLocators.TOTAL_ORDERS))

    def get_today_orders_count(self):
        return int(self.get_element_text(FeedLocators.TODAY_ORDERS))

    def latest_order_visible(self):
        return self.find_element(FeedLocators.ORDER_CARD).is_displayed()
