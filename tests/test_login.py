import unittest
import keyboard
from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.keys import Keys
import time



class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    # Title: Handling login/logout operations with correct data			
    def test_successful_login_and_logout(self):
        """
        Successful login and logout with all correct data and actions.
        """
        self.login_page.open()
        self.login_page.login("tomsmith", "SuperSecretPassword!")

        self.home_page.is_login_successfull()

        self.home_page.logout()
    
    # Title: Handling login operation with incorrect username			
    def test_login_incorrect_username(self):
        """
        Unsuccessful login with incorrect username but correct password.
        """
        self.login_page.open()
        self.login_page.login("timmsoms", "SuperSecretPassword!")
        self.login_page.is_login_unsuccessfull_username()

    # Title: Handling login operation with incorrect password			
    def test_login_incorrect_pass(self):
        """
        Unsuccessful login with correct username but incorrect password.
        """
        self.login_page.open()
        self.login_page.login("tomsmith", "qwerty12345")
        self.login_page.is_login_unsuccessfull_password()

    # Title: Handling login operation with incorrect username and incorrect password			
    def test_login_incorrect_all(self):
        """
        Unsuccessful login with incorrect username and incorrect password.
        """
        self.login_page.open()
        self.login_page.login("timmmmapple", "asdfghjkl")
        self.login_page.is_login_unsuccessfull_username()

    # Title: Handling login operation with script injection in username field and correct password			
    def test_login_incorrect_script_injection(self):
        """
        Unsuccessful login with script injection in username field and correct password.
        """
        self.login_page.open()
        self.login_page.login("<script>alert(12345678)</script>", "SuperSecretPassword!")
        self.login_page.is_login_unsuccessfull_username()

    # Title: Handling login operation with another one script injection in username field and correct password			
    def test_login_incorrect_script_injection2(self):
        """
        Unsuccessful login with another one script injection in username field and correct password.
        """
        self.login_page.open()
        self.login_page.login("<script>alert(“Hello, world!”)</alert>", "SuperSecretPassword!")
        self.login_page.is_login_unsuccessfull_username()

    # Title: Handling login operation with complex sequence of characters in username field and correct password			
    def test_login_incorrect_characters(self):
        """
        Unsuccessful login with complex sequence of characters in username field and correct password.
        """
        self.login_page.open()
        self.login_page.login("“♣☺♂” , “”‘~!@#$%^&*()?>,./\<][ /*<!–“”, “${code}”;–>", "SuperSecretPassword!")
        self.login_page.is_login_unsuccessfull_username()

    # Title: Handling login operation with text consisting of only spaces in username field and correct password			
    def test_login_incorrect_only_spaces(self):
        """
        Unsuccessful login with text consisting of only spaces in username field and correct password.
        """
        self.login_page.open()
        self.login_page.login("                                ", "SuperSecretPassword!")
        self.login_page.is_login_unsuccessfull_username()

    # Title: Handling login operation with correct username starting with several spaces in username field and correct password			
    def test_login_incorrect_start_with_spaces(self):
        """
        Unsuccessful login with correct username starting with several spaces in username field and correct password.
        """
        self.login_page.open()
        self.login_page.login("           tomsmith", "SuperSecretPassword!")
        self.login_page.is_login_unsuccessfull_username()

    # Title: Handling login operation with correct username followed by several spaces in username field and correct password			
    def test_login_incorrect_followed_by_spaces(self):
        """
        Unsuccessful login with correct username followed by several spaces in username field and correct password.
        """
        self.login_page.open()
        self.login_page.login("tomsmith              ", "SuperSecretPassword!")
        self.login_page.is_login_unsuccessfull_username()

    # Title: Handling login operation with correct username and password, but using DIFFERENT case letters in password			
    def test_login_incorrect_diff_case_letters(self):
        """
        Unsuccessful login with correct username and password, but using DIFFERENT case letters in password.
        """
        self.login_page.open()
        self.login_page.login("tomsmith", "SuPErsecretpasswORD!")
        self.login_page.is_login_unsuccessfull_password()

    # Title: Handling login operation using an incorrect password and login written in Cyrillic			
    def test_login_incorrect_cyrilyc(self):
        """
        Unsuccessful login using an incorrect password and login written in Cyrillic.
        """
        self.login_page.open()
        self.login_page.login("Артём", "КошкаБуся")
        self.login_page.is_login_unsuccessfull_username()

    # Title: Handling login operation with all blank fields			
    def test_login_incorrect_all_blank(self):
        """
        Unsuccessful login with all blank fields.
        """
        self.login_page.open()
        self.login_page.login("", "")
        self.login_page.is_login_unsuccessfull_username()

    # Title: Handling login operation with blank username field		
    def test_login_incorrect_blank_username(self):
        """
        Unsuccessful login with blank username field.
        """
        self.login_page.open()
        self.login_page.login("", "SuperSecretPassword!")
        self.login_page.is_login_unsuccessfull_username()

    # Title: Handling login operation with blank password field			
    def test_login_incorrect_blank_password(self):
        """
        Unsuccessful login with blank password field
        """
        self.login_page.open()
        self.login_page.login("tomsmith", "")	
        self.login_page.is_login_unsuccessfull_password()
        
    # Title: Proceeding login process with correct data and navigation process through form fields and buttons using keys on keyboard	
    def test_login_successfull_with_keys_navigation(self):
        """
        Successful login with navigation between fields and buttons using keyboard keys
        """
        self.login_page.open()
        keyboard.press_and_release("tab, tab")
        keyboard.write("tomsmith")
        keyboard.press_and_release("tab")
        keyboard.write("SuperSecretPassword!")
        keyboard.press_and_release("tab")
        keyboard.press_and_release("enter")
        time.sleep(0.1)
        self.home_page.is_login_successfull()

    # Title: Title: Checking for possibility to make line breaks in the fields				
    def test_login_unsuccessfull_with_line_breaks(self):
        """
        Unsuccessful login. Line breaks test
        """
        username_with_line_break = "tomsm\nith"
        self.login_page.open()
        keyboard.press_and_release("tab, tab")
        keyboard.write(username_with_line_break)
        keyboard.press_and_release("tab")
        keyboard.write("SuperSecretPassword!")
        keyboard.press_and_release("tab")
        keyboard.press_and_release("enter")
        self.login_page.is_login_unsuccessfull_username()

if __name__ == "__main__":
    unittest.main()
