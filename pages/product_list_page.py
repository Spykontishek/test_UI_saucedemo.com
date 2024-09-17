import allure
from locators.product_list_page_locators import Locators_prod_list
from pages.base_page import BasePage
from data import Data

class ProductListPage(BasePage):
    @allure.step('Клик по кнопке товара')
    def click_any_product_button(self):
        self.click_method(Locators_prod_list.ANY_PRODUCT)

    @allure.step('Ожидания перехода на страницу этого товара')
    def wait_go_to_specific_product_url(self):
        self.wait_url_to_be_visible_method(Data.ANY_PRODUCT_URL)

    @allure.step('Клик по кнопке "Add to cart')
    def click_add_to_cart_button(self):
        self.click_method(Locators_prod_list.ADD_TO_CART_BUTTON)

    @allure.step('Клик по кнопке корзины')
    def click_cart_button(self):
        self.click_method(Locators_prod_list.CART_BUTTON)

    @allure.step('Ожидания перехода на страницу корзины')
    def wait_go_to_cart_url(self):
        self.wait_url_to_be_visible_method(Data.CART_URL)
