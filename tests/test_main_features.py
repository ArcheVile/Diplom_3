import allure
from pages.main_page import MainPage

@allure.feature("Основной функционал")
class TestMainFeatures:

    @allure.title("Переход по кнопке Конструктор")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_feed()
        main_page.go_to_constructor()
        assert main_page.is_constructor_page()

    @allure.title("Переход по кнопке Лента заказов")
    def test_go_to_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_feed()
        assert main_page.is_feed_page()

    @allure.title("Открытие всплывающего окна ингредиента")
    def test_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.open_ingredient_modal()
        assert main_page.is_ingredient_modal_visible()
        main_page.close_ingredient_modal()
        assert main_page.is_ingredient_modal_closed()

    @allure.title("Добавление ингредиента увеличивает счётчик")
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        initial = main_page.get_ingredient_counter()
        main_page.add_ingredient_to_order()
        assert main_page.get_ingredient_counter() == initial + 1

    @allure.title("Оформление заказа авторизованным пользователем")
    def test_order_authenticated_user(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.open()
        main_page.add_ingredient_to_order()
        main_page.click_order_button()
        assert main_page.order_success_visible()
