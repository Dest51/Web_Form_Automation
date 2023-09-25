import unittest
from selenium import webdriver
from tests.test_login import LoginTest

if __name__ == "__main__":
    # Create a test suite
    test_suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

    # Initialize the driver
    driver = webdriver.Chrome()

    # Run the test suite
    unittest.TextTestRunner(verbosity=2).run(test_suite)

    # Quit the driver
    driver.quit()
