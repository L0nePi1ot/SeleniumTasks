from pages.yandex_func import MainYandexPage


def test_yandex():
    page = MainYandexPage()

    page.driver.get('https://yandex.ru')
    page.click(xpath=page.INPUT_SEARCH)
    page.fill_input(xpath=page.INPUT_SEARCH, value='Привет')
    page.click(xpath=page.BUTTON_SEARCH)

    print()
