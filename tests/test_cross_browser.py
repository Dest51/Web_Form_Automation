import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage

# Run test:
# python -m unittest tests/test_cross_browser.py

class CrossBrowserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chrome_driver = webdriver.Chrome()
        cls.firefox_driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.chrome_driver.quit()
        cls.firefox_driver.quit()

    def test_login_and_logout_chrome(self):
        self.login_and_logout(self.chrome_driver)

    def test_login_and_logout_firefox(self):
        self.login_and_logout(self.firefox_driver)

    def login_and_logout(self, driver):
        login_page = LoginPage(driver)
        home_page = HomePage(driver)

        # Open the login page
        login_page.open()

        # Perform the login
        login_page.login("tomsmith", "SuperSecretPassword!")

        # Verify successful login
        home_page.is_login_successfull()

        # Perform the logout
        home_page.logout()

if __name__ == "__main__":
    unittest.main()
