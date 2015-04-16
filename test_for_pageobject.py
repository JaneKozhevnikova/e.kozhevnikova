import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import page

class TestString(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://ya.ru")
        self.driver.implicitly_wait(60)
        self.main_page = page.MainPage(self.driver)

    def test(self):
        assert self.main_page.is_title_matches(),"Yandex title doesn't match"
        self.main_page.search_text_element = "Apps for Android"
        self.main_page.click_go_button()
        result = page.SearchResultsPage(self.driver)
        assert result.is_results_found(), "No result found"

    def test1(self):
        try:
            self.main_page.click_go_button()
            
        except NoSuchElementException:
            self.fail("Button doesn't found")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()


