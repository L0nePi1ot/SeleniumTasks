from pages.yandex_page import MainYandexPage


def test_yandex():
    page = MainYandexPage()

    page.driver.get('https://yandex.ru')
    page.click(xpath=page.INPUT_SEARCH)                         # 1
    page.fill_input(xpath=page.INPUT_SEARCH, value='Cessna')    # 2
    page.click(xpath=page.BUTTON_SEARCH)                        # 3
    page.clear_input(xpath=page.CLEAR_SEARCH)                   # 4
    page.fill_input(xpath=page.CLEAR_SEARCH, value='Airbus')    # 5
    page.click(xpath=page.SEC_BUTTON)
    page.click(xpath=page.PIC_BUTTON)
    #page.click(xpath=page.PIC_PUSH)
    page.element_hover(xpath=page.PIC_PUSH)


    print()
