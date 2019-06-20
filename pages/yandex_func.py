from pages.base_func import BasePage


class MainYandexPage(BasePage):

    INPUT_SEARCH = '//input[@class="input__control input__input"]'
    BUTTON_SEARCH = '//span[text()="Найти"]/ancestor::button'
