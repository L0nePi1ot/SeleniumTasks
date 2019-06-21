from pages.base_page import BasePage


class MainGooglePage(BasePage):

    INPUT_SEARCH = '//input[@class="gLFyf gsfi"]'
    BUTTON_SEARCH = '//div[@class="FPdoLc VlcLAe"]/descendant::input[@class="gNO89b"]'
    SEC_BUTTON = '//div[text()="Найти"]/ancestor::button'
    PIC_BUTTON = '//span[text()="Картинки"]'
