from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from getRandomProxy import *
import json
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def get_current_proxy():
    current_path = './chrome_proxy_extension/current_proxy.json'
    with open(current_path, 'r') as file:
        proxy_data = json.load(file)
    return proxy_data
print('_'*100,'FUNCIONAL','_'*10,'DESCARTAVEL')
for a in range(1000): 
    proxy_atual = get_random_proxy()
    chrome_options = Options()
    chrome_options.add_argument("--load-extension=./chrome_proxy_extension")
    service = Service(ChromeDriverManager(driver_version="131.0.6778.69").install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    time.sleep(3) 
    

    print(proxy_atual)
    driver.get("https://www.impulsecrm.online/auth")
    time.sleep(1)
    try:
        email_label = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="email"]'))
        )
        print('_'*100,' '*3,'(X)')
        with open("proxys_funcionais.txt", "a") as file:
            file.write(proxy_atual + "\n") 
    except:
        print('_'*100,' '*25,'(X)')
        with open("proxys_descartaveis.txt", "a") as file:
            file.write(proxy_atual + "\n")  



    finally:
        driver.quit()  
