from selenium import webdriver
from browsermobproxy import Server
import time
from pages.login_page import LoginPage
from pages.home_page import HomePage

#
# THIS IS NOT WORKING
#



# Start the BrowserMob Proxy server
server = Server("utils\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat")
server.start()
proxy = server.create_proxy()

# Configure Chrome WebDriver with the proxy
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--proxy-server={}".format(proxy.proxy))

# Create a Chrome WebDriver instance with the proxy settings
chrome_driver = webdriver.Chrome(options=chrome_options)

# Create page objects for both drivers
login_page = LoginPage(chrome_driver)
home_page = HomePage(chrome_driver)

# Set network conditions for the proxy
proxy.new_har("example.com", options={"captureHeaders": True, "captureContent": True})
proxy.set_latency("upstream", 0)
proxy.set_downstream_kbps(0)

# Navigate to the URL using the open method from LoginPage
login_page.open()

# Login using the login method from LoginPage
login_page.login("tomsmith", "SuperSecretPassword!")

# Wait for a while (simulate some activity on the page)
time.sleep(2)

# Turn off the Internet (simulating offline)
proxy.set_latency("upstream", 2000)  # Increased latency to simulate offline
proxy.set_downstream_kbps(0)  # Set throughput to zero to simulate offline

# Reload the page (with no Internet)
chrome_driver.refresh()

# Wait for a while (simulate some activity on the page without Internet)
time.sleep(2)

# Turn on the Internet (simulating online)
proxy.set_latency("upstream", 0)  # Reset latency to zero to simulate online
proxy.set_downstream_kbps(0)  # Set throughput to zero to simulate online

# Reload the page (with Internet)
chrome_driver.refresh()

# Wait for a while (simulate some activity on the page with Internet)
time.sleep(2)

# Perform actions using methods from HomePage
home_page.logout()

# Stop the BrowserMob Proxy server and quit both WebDriver instances when done
server.stop()
chrome_driver.quit()
