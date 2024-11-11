from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_for_testing_path = "/Users/agenciaimpulsemax/Downloads/chrome-mac-x64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"
options = Options()
options.binary_location = chrome_for_testing_path  # Define o caminho do Chrome for Testing

# Especifica a versão do ChromeDriver, se necessário
driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="130.0.6723.116").install()), options=options)

driver.get("https://www.google.com")

print(driver.title)

driver.quit()