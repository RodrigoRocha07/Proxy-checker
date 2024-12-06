from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--proxy-server=http://92.112.170.53:6022')
chrome_options.add_argument('--proxy-auth=AllanpX0101:AllanpX010')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.impulsecrm.online/auth")

