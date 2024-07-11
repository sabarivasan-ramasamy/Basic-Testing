from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

path = "C:\\Program Files (x86)\\chromedriver.exe"


driver = webdriver.Chrome()
driver.implicitly_wait(60)

driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'langSelect-EN'))).click()
    print("Language selected successfully.")
    cookie = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'bigCookie')))
    count = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'cookies')))
    max = [WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'productPrice' + str(i)))) for i in range(1, -1, -1)]
    actions =ActionChains(driver)
    for _ in range(50000):
        actions.click(cookie).perform()
        time.sleep(0.1)
except Exception as e:
    print('Element not found:', e)









time.sleep(60)