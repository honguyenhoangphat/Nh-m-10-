from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://x.com/i/flow/login")

time.sleep(5)

username = driver.find_element(By.XPATH, "//input[@name='text']")
username.send_keys("hnhp113")
name = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
name.click()

time.sleep(3)

password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys("phatho0317")
pw = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
pw.click()

time.sleep(8)
search = driver.find_element(By.XPATH, "//input[@data-testid='SearchBox_Search_Input']")
idol = "M-TP"
search.send_keys(idol)
search.send_keys(Keys.ENTER)

time.sleep(5)
people = driver.find_element(By.XPATH,"//span[contains(text(),'People')]")
people.click()

time.sleep(5)
name_idol = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[1]/div/div/button/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]")
name_idol.click()
body = driver.find_element(By.TAG_NAME, "body") # tim the body de cuộn trang

#Lap lai thao tac cuon
count = 0
last_height = driver.execute_script("return document.body.scrollHeight")
view_posts = set() #Tao tệp lưu các post, tránh trufng lập
while count < 10:
    #Cuon xuong cuoi trang
    for i in range(45):
        body.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.000001)
    view_elements = driver.find_elements(By.XPATH, "//a[contains(@aria-label,'views')]")
    for view_element in view_elements:
        try:
            #Lay link  de dam bao khong bi trung lap
            link = view_element.get_attribute("href")
            if link not in view_posts:
                view_posts.add(link)

                views = view_element.get_attribute('aria-label') #Tach sl view tu chuỗi aria

                if views:
                    views_count = views.split(' ')[0]
                    print("So luong view: ", views_count)
                    view_posts.add(view_element)
                    count += 1
                    if count == 5:
                        break
        except Exception as e:
            print(f"Error: {e}")
    if count == 10:
        break
    #Kiểm tra chiều cao sau khi cuộn
    new_height = driver.execute_script("return document.body.scrollHeight")
    #Neu height khong doi, kh con nội dung mới, dung chương trình
    if new_height == last_height:
        break

    last_height = new_height

time.sleep(10)
driver.quit()