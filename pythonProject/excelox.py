from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.chrome.service import Service
from pymongo import MongoClient



# Đường dẫn đến file thực thi geckodriver
#gecko_path = r"D:/Nhom10/Nhom-10d/pythonProject/geckodriver.exe"
gecko_path = r"D:/DoAnNhom10d/Nhom-10d/pythonProject/geckodriver.exe"

ser = Service(gecko_path) # Khởi tạo đối tượng dịch vụ với geckodriver

# Tạo tùy chọn
options = webdriver.firefox.options.Options()
options.binary_location ="C:/Program Files/Mozilla Firefox/firefox.exe"
# Thiết lập firefox chỉ hiện thị giao diện
options.headless = True

# Khởi tạo driver
driver = webdriver.Firefox(options=options, service=ser)
driver.get("https://x.com/i/flow/login")

time.sleep(5)

#Đăng nhập
username = driver.find_element(By.XPATH, "//input[@name='text']")
username.send_keys("hnhp113")
time.sleep(1)
name = driver.find_element(By.XPATH, "//span[contains(text(),'Tiếp theo')]")
name.click()

time.sleep(2)
#Xác thực thông tin
try:
    email = driver.find_element(By.XPATH, "//input[@name='text']")
    email.send_keys("hnhp113114115@gmail.com")
    tt = driver.find_element(By.XPATH, "//span[contains(text(),'Tiếp theo')]")
    tt.click()
except:
    pass
time.sleep(2)
#Mật khẩu
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys("phatho0317")
pw = driver.find_element(By.XPATH, "//span[contains(text(),'Đăng nhập')]")
pw.click()

time.sleep(10)

#Tìm trang cá nhân bạn muốn quét dữ liệu
search = driver.find_element(By.XPATH, "//input[@data-testid='SearchBox_Search_Input']")
idol = "Oxford University"
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

def scrape_tweets(driver, max_tweets = 6000):
    #Luu du luu kiem tra bai viet trung lap:
    global document
    data_set = set()
    count = 0

    userIDs = []
    timePosts = []
    tweetTexts = []  # = Post status
    likes = []
    replys = []
    reposts = []
    views = []
    tweetIMG=[]

    while count < max_tweets:
        articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
        for article in articles:
            try:
                userID = article.find_element(By.XPATH, ".//div[@data-testid='User-Name']").text
            except:
                userID = ''
            try:
                timePost = driver.find_element(By.XPATH, ".//time").get_attribute("datetime")
            except:
                timePost = ''
            try:
                tweetText = driver.find_element(By.XPATH, ".//div[@data-testid='tweetText']").text
            except:
                tweetText = ''
            try:
                # like = driver.find_element(By.XPATH, ".//button[@data-testid='like']").text
                like_count = driver.find_element(By.XPATH, ".//button[contains(@aria-label,'Likes')]")
                like = like_count.get_attribute('aria-label').split(' ')[0]
            except:
                like = ''
            try:
                # reply = driver.find_element(By.XPATH, ".//button[@data-testid='reply']").text
                reply_count = driver.find_element(By.XPATH, ".//button[contains(@aria-label,'Replies')]")
                reply = reply_count.get_attribute('aria-label').split(' ')[0]
            except:
                reply = ''

            try:
                # resport = driver.find_element(By.XPATH, ".//button[@data-testid='retweet']").text
                repost_count = driver.find_element(By.XPATH, ".//button[contains(@aria-label,'reposts')]")
                repost = repost_count.get_attribute('aria-label').split(' ')[0]
            except:
                repost = ''

            try:

                view = driver.find_element(By.XPATH, ".//a[contains(@aria-label,'views')]")
                views_count = view.get_attribute('aria-label').split(' ')[0]
            except:
                views_count = ''

            try:
                images = article.find_elements(By.XPATH, ".//img[contains(@src, 'https://pbs.twimg.com') and not (contains(@src, 'profile_images'))]")

                tweetIMGs = [img.get_attribute('src') for img in images]

            except:
                tweetIMGs = ''

            # Tạo document dữ liệu để lưu trữ trong MongoDB


            #Kiểm tra xem tweet có trùng lặp không
            if tweetText not in tweetTexts:
                data_set.add(tweetText)
                userIDs.append(userID)
                timePosts.append(timePost)
                tweetTexts.append(tweetText)
                likes.append(like)
                replys.append(reply)
                reposts.append(repost)
                views.append(views_count)
                tweetIMG.append(tweetIMGs)
                count += 1

                if count > max_tweets:
                    break


        #Cuộn chậm
        driver.execute_script("window.scrollBy(0,600);")
        time.sleep(3)
        #Lấy thêm tweets mới sau khi cuộn
        print(len(set(tweetTexts)))
    print(f"Dữ liệu đã được lưu vào MongoDB. Đã cào được {count} bài")
    #
    df = pd.DataFrame(zip(userIDs, timePosts, tweetTexts, likes, replys, reposts, views, tweetIMG),
                       columns=['userIDs', 'timePosts', 'tweetTexts', 'likes', 'replys', 'reposts', 'views', 'tweetIMG'])
    df['tweetIMG'] = df['tweetIMG'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)


    filename = 'testOxford.xlsx'
    df.to_excel(filename, index=False)
    print("File excel saved")
scrape_tweets(driver)
driver.quit()
