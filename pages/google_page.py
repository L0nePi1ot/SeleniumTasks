from pages.base_page import BasePage


class MainGooglePage(BasePage):

    INPUT_SEARCH = '//input[@class="input__control input__input"]'
    BUTTON_SEARCH = '//span[text()="Найти"]/ancestor::button'
