from .base_page import BasePage
from locators.profile_locators import ProfileLocators

class ProfilePage(BasePage):
    def open(self):
        super().open("/account/profile")

    def logout(self):
        self.click_element(ProfileLocators.LOGOUT_BUTTON)

    def go_to_order_history(self):
        self.click_element(ProfileLocators.ORDER_HISTORY)

    def is_profile_page(self):
        return self.find_element(ProfileLocators.PROFILE_HEADER)

    def is_order_history_page(self):
        return "/account/orders" in self.get_current_url()
