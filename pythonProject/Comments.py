from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


driver = webdriver.Chrome()
driver.get("https://x.com/sontungmtp777/status/1804486742147473860")

time.sleep(5)
comments = []

articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
while True:
    for article in articles:
        comment = driver.find_element(By.XPATH, ".//span")