from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://x.com/i/flow/login")

time.sleep(5)

username = driver.find_element(By.XPATH, "//input[@name='text']")
username.send_keys("hnhp113")
button1 = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
button1.click()

time.sleep(2)

password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys("phatho0317")
button2 = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
button2.click()

time.sleep(5)