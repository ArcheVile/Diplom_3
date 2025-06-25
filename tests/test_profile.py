import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage

@allure.feature("Личный кабинет")
class TestProfile:

    @allure.title("Переход в личный кабинет")
    def test_go_to_profile(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_profile()
        profile_page = ProfilePage(driver)
        assert profile_page.is_profile_page()

    @allure.title("Переход в раздел истории заказов")
    def test_go_to_order_history(self, driver, login_user):
        profile_page = ProfilePage(driver)
        profile_page.open()
        profile_page.go_to_order_history()
        assert profile_page.is_order_history_page()

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, login_user):
        profile_page = ProfilePage(driver)
        profile_page.open()
        profile_page.logout()
        login_page = LoginPage(driver)
        assert login_page.is_login_page()
