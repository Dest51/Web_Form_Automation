from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

    def is_login_unsuccessfull_username(self):
        flash_message_text = self.driver.find_element(By.CSS_SELECTOR, "div[data-alert].flash.error").text
        expected_message = "Your username is invalid"
        message_without_line_breaks = flash_message_text.replace("\n", " ")
        flash_message_cleaned = message_without_line_breaks.split("!")[0].strip()
        expected_message_cleaned = expected_message.strip()
        print("cleaned flash message is:", flash_message_cleaned)
        print("expected cleaned flash message is:", expected_message_cleaned)

        assert flash_message_cleaned == expected_message_cleaned    
    
    def is_login_unsuccessfull_password(self):
        flash_message_text = self.driver.find_element(By.CSS_SELECTOR, "div[data-alert].flash.error").text
        expected_message = "Your password is invalid"
        message_without_line_breaks = flash_message_text.replace("\n", " ")
        flash_message_cleaned = message_without_line_breaks.split("!")[0].strip()
        expected_message_cleaned = expected_message.strip()
        print("cleaned flash message is:", flash_message_cleaned)
        print("expected cleaned flash message is:", expected_message_cleaned)

        assert flash_message_cleaned == expected_message_cleaned   