from pages.base_page import BasePage


class MainYandexPage(BasePage):

    INPUT_SEARCH = '//input[@class="input__control input__input"]'
    BUTTON_SEARCH = '//span[text()="Найти"]/ancestor::button'
    CLEAR_SEARCH = '//input[@class="input__control"]'
    SEC_BUTTON = '//div[text()="Найти"]/ancestor::button'
    PIC_BUTTON = '//span[text()="Картинки"]'
    PIC_PUSH = '//span[text()="Видео"]' # тест