from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        logout_button = self.driver.find_element(By.CSS_SELECTOR, "a[href='/logout']")
        logout_button.click()

    def is_login_successfull(self):
        flash_message_text = self.driver.find_element(By.CSS_SELECTOR, "div[data-alert].flash.success").text
        expected_message = "You logged into a secure area"
        message_without_line_breaks = flash_message_text.replace("\n", " ")
        flash_message_cleaned = message_without_line_breaks.split("!")[0].strip()
        expected_message_cleaned = expected_message.strip()

        assert flash_message_cleaned == expected_message_cleaned
