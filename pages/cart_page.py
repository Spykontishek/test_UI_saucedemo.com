import allure
from pages.base_page import BasePage
from locators.cart_page_locators import Locators_cart
from data import Data

class CartPage(BasePage):

    @allure.step('ожидание пока товар станет видимым')
    def wait_product_to_be_visible(self):
        self.wait_element_to_be_visible_method(Locators_cart.ANY_PRODUCT)

    @allure.step('проверка, что товар отображается')
    def product_is_displayed(self):
        return self.element_is_displayed_method(Locators_cart.ANY_PRODUCT)

    @allure.step('Клик по кнопке "Checkout"')
    def click_checkout_button(self):
        self.click_method(Locators_cart.CHECKOUT_BUTTON)

    @allure.step('Ожидания перехода на страницу заказа')
    def wait_go_to_order_url(self):
        self.wait_url_to_be_visible_method(Data.ORDER_URL)