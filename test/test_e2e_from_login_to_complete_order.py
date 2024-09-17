import allure
from conftest import driver
from pages.auth_page import AuthPage
from pages.product_list_page import ProductListPage
from pages.cart_page import CartPage
from pages.order_page import OrderPage
from pages.second_order_page import SecondOrderPage
from pages.finish_order_page import FinishOrderPage
from constants import Constants


class TestRestorePassword:
    @allure.title('Проверка e2e cценария от авторизации до успешного завершения заказа"')
    @allure.description('Авторизация, добавление товара в корзину, проверка, что он там присутствует, оформление заказа и проверка что покупка завершена')
    def test_click_restore_password_button(self, driver):
        auth_page = AuthPage(driver)
        auth_page.set_username(Constants.TEST_USERNAME)
        auth_page.set_password(Constants.TEST_PASSWORD)
        auth_page.click_login_button()
        auth_page.wait_go_to_product_url()
        prod_list_page = ProductListPage(driver)
        prod_list_page.click_any_product_button()
        prod_list_page.wait_go_to_specific_product_url()
        prod_list_page.click_add_to_cart_button()
        prod_list_page.click_cart_button()
        prod_list_page.wait_go_to_cart_url()
        cart_page = CartPage(driver)
        cart_page.wait_product_to_be_visible()
        assert cart_page.product_is_displayed() is True
        cart_page.click_checkout_button()
        cart_page.wait_go_to_order_url()
        order_page = OrderPage(driver)
        order_page.set_first_name(Constants.FIRST_NAME)
        order_page.set_second_name(Constants.LAST_NAME)
        order_page.set_postal_code(Constants.POSTAL_CODE)
        order_page.click_continue_button()
        order_page.wait_go_to_2_order_url()
        second_order_page= SecondOrderPage(driver)
        second_order_page.click_finish_button()
        finish_order_page = FinishOrderPage(driver)
        finish_order_page.wait_order_success_to_be_visible()
        assert finish_order_page.Order_success_is_displayed() is True


