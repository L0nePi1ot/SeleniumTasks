from pages.google_page import MainGooglePage


def test_google():
    page = MainGooglePage()

    page.driver.get('https://www.google.com/')
    page.click(xpath=page.INPUT_SEARCH)  # 1
    page.fill_input(xpath=page.INPUT_SEARCH, value='Boeing')  # 2
    time.sleep(3)
    page.click(xpath=page.BUTTON_SEARCH)  # 3
    page.clear_input(xpath=page.INPUT_SEARCH)  # 4
    page.fill_input(xpath=page.INPUT_SEARCH, value='Sukhoi')  # 5
    page.click(xpath=page.SEC_BUTTON)
    page.click(xpath=page.PIC_BUTTON)

    print()