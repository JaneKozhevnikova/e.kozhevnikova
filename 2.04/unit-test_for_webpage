import unittest
from selenium import webdriver
from unittest import TestCase

# driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX)
#driver.get("https://ya.ru")
from selenium.common.exceptions import NoSuchElementException


class TestString(unittest.TestCase):
    def test(self):
        driver = webdriver.Firefox()
        driver.get("http://ya.ru")
        inputElement = driver.find_element_by_name("text")
        inputElement.send_keys("Apps for Android")
        inputElement.submit()
        driver.implicitly_wait(60)
        print(driver.title)
        driver.close()
        self.assertIn("Apps for Android", driver.title)

    def test1(self):
        driver = webdriver.Firefox()
        driver.get("https://translate.yandex.ru")
        inputElement = driver.find_element_by_id("cmdAuto").click()
        driver.implicitly_wait(60)
        inputElement = driver.find_element_by_id("srcText")
        inputElement.send_keys("Yandex")
        try:
            driver.find_elements_by_id("cmdSubmit")
        except NoSuchElementException:
            return False
        return True
        driver.close()


if __name__ == '__main__':
    unittest.main()
