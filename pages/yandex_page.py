from pages.base_page import BasePage


class MainYandexPage(BasePage):

    INPUT_SEARCH = '//input[@class="input__control input__input"]'
    BUTTON_SEARCH = '//span[text()="Найти"]/ancestor::button'
    CLEAR_SEARCH = '//input[@class="input__control"]'
    SEC_BUTTON = '//div[text()="Найти"]/ancestor::button'
    PIC_BUTTON = '//span[text()="Картинки"]'
    PIC_PUSH = '//*[@id="2f2529d63771e678d57d4888368eee0e"]/div'
