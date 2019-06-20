from pages.google_page import MainGooglePage


def test_google():
    page = MainGooglePage()

    page.driver.get('https://www.google.com/')
    page.click(xpath=page.INPUT_SEARCH)
    page.fill_input(xpath=page.INPUT_SEARCH, value='Привет')
    page.click(xpath=page.BUTTON_SEARCH)

    print()