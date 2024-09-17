import allure
from locators.auth_page_locators import Locators_auth
from pages.base_page import BasePage
from data import Data

class AuthPage(BasePage):

    @allure.step('Переход на страницу авторизации')
    def navigate_auth_url(self):
        self.navigate_url_method(Data.URL)

    @allure.step('Заполнение поля "Username"')
    def set_username(self, username):
        self.send_keys_method(Locators_auth.USERNAME_FIELD, username)

    @allure.step('Заполнение поля "Password"')
    def set_password(self, password):
        self.send_keys_method(Locators_auth.PASSWORD_FIELD, password)

    @allure.step('Клик по кнопке "Login"')
    def click_login_button(self):
        self.click_method(Locators_auth.LOGIN_BUTTON)

    @allure.step('Ожидания перехода на страницу со списком товаров')
    def wait_go_to_product_url(self):
        self.wait_url_to_be_visible_method(Data.PRODUCT_LIST_URL)
