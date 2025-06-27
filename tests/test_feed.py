import allure
from pages.feed_page import FeedPage
from pages.main_page import MainPage

@allure.feature("Лента заказов")
class TestFeed:

    @allure.title("Открытие заказа из ленты заказов")
    def test_open_order_modal(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open()
        feed_page.open_order_details()
        assert feed_page.is_order_modal_visible()
        feed_page.close_order_modal()
        assert feed_page.is_order_modal_closed()

    @allure.title("Появление нового заказа в ленте заказов")
    def test_order_in_feed(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.open()
        main_page.add_ingredient_to_order()
        main_page.click_order_button()
        feed_page = FeedPage(driver)
        feed_page.open()
        assert feed_page.latest_order_visible()

    @allure.title("Увеличение счётчика 'Выполнено за всё время'")
    def test_total_orders_counter_increment(self, driver, login_user):
        feed_page = FeedPage(driver)
        feed_page.open()
        total_before = feed_page.get_total_orders_count()
        main_page = MainPage(driver)
        main_page.open()
        main_page.add_ingredient_to_order()
        main_page.click_order_button()
        feed_page.open()
        total_after = feed_page.get_total_orders_count()
        assert total_after > total_before

    @allure.title("Увеличение счётчика 'Выполнено за сегодня'")
    def test_today_orders_counter_increment(self, driver, login_user):
        feed_page = FeedPage(driver)
        feed_page.open()
        today_before = feed_page.get_today_orders_count()
        main_page = MainPage(driver)
        main_page.open()
        main_page.add_ingredient_to_order()
        main_page.click_order_button()
        feed_page.open()
        today_after = feed_page.get_today_orders_count()
        assert today_after > today_before
