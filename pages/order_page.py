import allure
from locators.order_page_locators import Locators_order
from pages.base_page import BasePage
from data import Data

class OrderPage(BasePage):

    @allure.step('Заполнение поля "First name"')
    def set_first_name(self, first_name):
        self.send_keys_method(Locators_order.FIRST_NAME_FIELD, first_name)

    @allure.step('Заполнение поля "Last name"')
    def set_second_name(self, last_name):
        self.send_keys_method(Locators_order.LAST_NAME_FIELD, last_name)

    @allure.step('Заполнение поля "Zip/Postal Code"')
    def set_postal_code(self, postal_code):
        self.send_keys_method(Locators_order.POSTAL_CODE_FIELD, postal_code)

    @allure.step('Клик по кнопке "Continue')
    def click_continue_button(self):
        self.click_method(Locators_order.CONTINUE_BUTTON)

    @allure.step('Ожидания перехода на 2-ую страницу заказа')
    def wait_go_to_2_order_url(self):
        self.wait_url_to_be_visible_method(Data.SECOND_ORDER_URL)