from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(executable_path='G:/Projects/SeleniumTasks/webdrivers/chromedriver.exe',
                                  chrome_options=chrome_options)

    def get_element(self, xpath: str):
        """Метод получения вэб элемента по xpath

        Args:
            xpath: xpath

        Returns:
            element: вэб-элемент
        """
        try:
            element = WebDriverWait(driver=self.driver, timeout=20).until(
                expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            element = self.driver.find_element(By.XPATH, xpath)
        return element

    def click(self, xpath):

        element = self.get_element(xpath=xpath)
        element.click()

    def fill_input(self, xpath, value):
        """Метод заполняет поле

        Args:
            xpath: xpath
            value: значение которым заполняется

        Returns:

        """
        element = self.get_element(xpath=xpath)
        element.send_keys(value)

    def clear_input(self, xpath):

        element = self.get_element(xpath=xpath)
        element.clear()

    def hover(self, xpath):

        #element = self.driver.find_element_by_link_text(xpath=xpath)
        #hov = ActionChains(self.driver).move_to_element(element)
        #hov.perform()

        hover = selfdriver.get_element(xpath=xpath)  # Наведение мыши
        hover = ActionChains(driver).move_to_element(hover).perform()
        hover.perform()
        driver.get_element("//*[@id=\"result\"]/div[1]/div/div[1]/a/div[2]/div[1]/div[2]/div[1]").click()