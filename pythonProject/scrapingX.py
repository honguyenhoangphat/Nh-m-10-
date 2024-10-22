from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


driver = webdriver.Chrome()
driver.get("https://x.com/i/flow/login")

time.sleep(5)

#Đăng nhập
username = driver.find_element(By.XPATH, "//input[@name='text']")
username.send_keys("hnhp113")
name = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
name.click()

time.sleep(2)

password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys("phatho0317")
pw = driver.find_element(By.XPATH, "//span[contains(text(),'Log in')]")
pw.click()

time.sleep(5)

#Tìm trang cá nhân bạn muốn quét dữ liệu
search = driver.find_element(By.XPATH, "//input[@data-testid='SearchBox_Search_Input']")
idol = "M-TP"
search.send_keys(idol)
search.send_keys(Keys.ENTER)
time.sleep(5)

#Qua tab people để tìm, vì ở trang chính có khi k co
people = driver.find_element(By.XPATH, "//span[contains(text(),'People')]")
people.click()
time.sleep(7)

#Nhấp vao người bạn muốn tìm
name_idol = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/section/div/div/div[1]/div/div/button/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]")
name_idol.click()
time.sleep(2)

#Tạo list để lưu dữ liệu

#Tìm thẻ body để có thể cuộn trang
body = driver.find_element(By.TAG_NAME, "body")
data_set = set()

def scrape_tweets(driver):
    #Luu du luu kiem tra bai viet trung lap:
    userIDs = []
    timePosts = []
    tweetTexts = []  # = Post status
    likes = []
    replys = []
    resports = []

    #view=[]
#tweetIMG=[]
    articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
    while True:
        for article in articles:
            try:
                userID = article.find_element(By.XPATH,".//div[@data-testid='User-Name']").text
            except:
                userID = ''
            try:
                timePost = driver.find_element(By.XPATH,".//time").get_attribute("datetime")
            except:
                timePost = ''
            try:
                tweetText = driver.find_element(By.XPATH,".//div[@data-testid='tweetText']").text
            except:
                tweetText = ''
            try:
                like = driver.find_element(By.XPATH, ".//button[@data-testid='like']").text
            except:
                like = ''
            try:
                reply = driver.find_element(By.XPATH, ".//button[@data-testid='reply']").text
            except:
                reply = ''

            try:
                resport = driver.find_element(By.XPATH, ".//button[@data-testid='retweet']").text
            except:
                resport = ''

            #Kiểm tra xem tweet có trùng lặp không
            if tweetText not in tweetTexts:
                data_set.add(tweetText)
                userIDs.append(userID)
                timePosts.append(timePost)
                tweetTexts.append(tweetText)
                likes.append(like)
                replys.append(reply)
                resports.append(resport)
        #Cuộn chậm
        driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(3)
        #Lấy thêm tweets mới sau khi cuộn
        articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
        if len(set(tweetTexts)) >= 5:
            break
            print(len(set(tweetTexts)))


    df = pd.DataFrame(zip(userIDs,timePosts,tweetTexts,likes,replys,resports),
                      columns=['userIDs','timePosts','tweetTexts','likes','replys','resports'])
    filename = 'X.xlsx'
    df.to_excel(filename)
    print("File excel saved")
scrape_tweets(driver)
driver.quit()