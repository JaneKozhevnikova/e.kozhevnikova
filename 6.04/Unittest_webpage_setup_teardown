import unittest
from selenium import webdriver
from unittest import TestCase

# driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX)
#driver.get("https://ya.ru")
from selenium.common.exceptions import NoSuchElementException
from selenium_test_web_page import driver
#from page import MainPage


class TestString(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test(self):
        self.driver.get("http://ya.ru")
        self.driver.implicitly_wait(60)

        inputElement = driver.find_element_by_name("text")
        inputElement.send_keys("Apps for Android")
        inputElement.submit()
        print(driver.title)
        self.assertIn("Apps for Android", driver.title)

    def test1(self):
        
        self.driver.get("http://translate.ya.ru")
        self.driver.implicitly_wait(60)

        driver.find_element_by_id("cmdAuto").click()
        inputElement = driver.find_element_by_id("srcText")
        inputElement.send_keys("Yandex")
        try:
            driver.find_elements_by_id("cmdSubmit")
            #check = True
        except NoSuchElementException:
           #check = False
            self.fail("Button doesn't found")
        #self.assertTrue(check, 'The Element not exists')

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
