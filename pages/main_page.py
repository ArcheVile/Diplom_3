from .base_page import BasePage
from locators.main_locators import MainLocators

class MainPage(BasePage):
    def open(self):
        super().open("/")

    def go_to_profile(self):
        self.click_element(MainLocators.PROFILE_BUTTON)

    def go_to_constructor(self):
        self.click_element(MainLocators.CONSTRUCTOR_BUTTON)

    def go_to_feed(self):
        self.click_element(MainLocators.FEED_BUTTON)

    def open_ingredient_modal(self):
        self.click_element(MainLocators.INGREDIENT)

    def is_ingredient_modal_visible(self):
        return self.find_element(MainLocators.INGREDIENT_MODAL).is_displayed()

    def close_ingredient_modal(self):
        self.click_element(MainLocators.CLOSE_MODAL_BUTTON)

    def is_ingredient_modal_closed(self):
        return MainLocators.INGREDIENT_MODAL not in self.driver.page_source

    def add_ingredient_to_order(self):
        self.click_element(MainLocators.INGREDIENT)

    def get_ingredient_counter(self):
        try:
            return int(self.get_element_text(MainLocators.INGREDIENT_COUNTER))
        except:
            return 0

    def click_order_button(self):
        self.click_element(MainLocators.ORDER_BUTTON)

    def order_success_visible(self):
        return self.find_element(MainLocators.ORDER_SUCCESS).is_displayed()

    def is_constructor_page(self):
        return "constructor" in self.get_current_url()

    def is_feed_page(self):
        return "feed" in self.get_current_url()
