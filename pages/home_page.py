from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        logout_button = self.driver.find_element(By.CSS_SELECTOR, "a[href='/logout']")
        logout_button.click()

    def is_login_successfull(self):
        flash_message = self.driver.find_element(By.CLASS_NAME, "flash success").text
        print("flash message is: ", flash_message)
        assert flash_message == " You logged into a secure area! "
