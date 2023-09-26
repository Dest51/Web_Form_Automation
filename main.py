import unittest
from selenium import webdriver
from tests.test_login import LoginTest

if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

    unittest.TextTestRunner(verbosity=2).run(test_suite)  
    
    #unittest.main()
