from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.chrome.service import Service
from pymongo import MongoClient

#kết nối
client = MongoClient("mongodb://localhost:27017/")
client.drop_database('demo')
db = client['demo']  # chon csdl Facebookdata1
collection = db['tweets']

# Đường dẫn đến file thực thi geckodriver
gecko_path = r"D:/DoAnNhom10d/Nhom-10d/pythonProject/geckodriver.exe"
ser = Service(gecko_path) # Khởi tạo đối tượng dịch vụ với geckodriver

# Tạo tùy chọn
options = webdriver.firefox.options.Options()
options.binary_location ="C:/Program Files/Mozilla Firefox/firefox.exe"
# Thiết lập firefox chỉ hiện thị giao diện
options.headless = False

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

#Tìm thẻ body để có thể cuộn trang
data_set = set()

# def scrape_comments(article):
#     comments = []
#
#     # Nhấp vào bài viết để mở phần chi tiết, bao gồm cả các bình luận
#     try:
#         article.click()
#         time.sleep(2)  # Đợi trang tải để có các bình luận
#     except Exception as e:
#         print(f"Lỗi khi nhấp vào bài viết: {e}")
#         return comments  # Nếu không nhấp được thì trả về danh sách rỗng
#
#     # Tìm các bình luận sau khi nhấp vào bài viết
#     comment_elements = article.find_elements(By.XPATH, ".//div[@data-testid='reply']")
#     for comment in comment_elements[:10]:  # Giới hạn 10 bình luận đầu
#         try:
#             comment_text = comment.find_element(By.XPATH, ".//div[@data-testid='tweetText']").text
#             comments.append(comment_text)
#         except Exception as e:
#             print(f"Lỗi khi lấy bình luận: {e}")
#             comments.append("")  # Nếu không có nội dung, thêm bình luận trống
#
#     # Đóng lại bài viết sau khi lấy bình luận
#     try:
#         driver.find_element(By.XPATH, "//div[@aria-label='Close']").click()
#         time.sleep(1)  # Đợi một chút để đảm bảo bài viết đóng hoàn toàn
#     except Exception as e:
#         print(f"Lỗi khi đóng bài viết: {e}")
#
#     return comments





def scrape_tweets(driver):
    #Luu du luu kiem tra bai viet trung lap:
    global document
    userIDs = []
    timePosts = []
    tweetTexts = []  # = Post status
    likes = []
    replys = []
    reposts = []
    views = []
    tweetIMG=[]

    articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
    while True:
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
                images = article.find_elements(By.XPATH, ".//img[@alt='Image']")
                tweetIMGs = [img.get_attribute('src') for img in images]

            except:
                tweetIMGs = ''
            # comments = scrape_comments(article)
                # Tạo document dữ liệu để lưu trữ trong MongoDB
            document = {
                "userID": userID,
                "timePost": timePost,
                "tweetText": tweetText,
                "like": like,
                "reply": reply,
                "repost": repost,
                "views": views_count,
                "tweetIMG": tweetIMGs

            }

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
                # tweet_comments.append(comments)
                collection.insert_one(document)


        #Cuộn chậm
        driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(5)
        #Lấy thêm tweets mới sau khi cuộn
        articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
        if len(set(tweetTexts)) >= 50:
            break
        print(len(set(tweetTexts)))
    print("Dữ liệu đã được lưu vào MongoDB.")

    # df = pd.DataFrame(zip(userIDs, timePosts, tweetTexts, likes, replys, reposts, views, tweetIMG),
    #                    columns=['userIDs', 'timePosts', 'tweetTexts', 'likes', 'replys', 'reposts', 'views', 'tweetIMG'])
    # df['tweetIMG'] = df['tweetIMG'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
    # # # df['tweet_comments'] = df['tweet_comments'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
    #
    # filename = 'ab.xlsx'
    # df.to_excel(filename, index=False)
    # print("File excel saved")
# scrape_comment()
scrape_tweets(driver)
driver.quit()
def convert_numeric_fields(collection):
    for document in collection.find():
        update_needed = False
        update_fields = {}

        for field, value in document.items():
            # Kiểm tra nếu giá trị là chuỗi và có thể chuyển đổi thành số
            if isinstance(value, str) and value.isdigit():
                update_fields[field] = int(value)  # Chuyển sang kiểu số nguyên
                update_needed = True
            elif isinstance(value, str):
                try:
                    # Cố gắng chuyển thành số thực nếu có thể
                    num_value = float(value)
                    update_fields[field] = num_value
                    update_needed = True
                except ValueError:
                    continue  # Không phải kiểu số, bỏ qua

        # Nếu có bất kỳ trường nào cần cập nhật, thực hiện cập nhật
        if update_needed:
            collection.update_one({'_id': document['_id']}, {'$set': update_fields})

# Kết nối lại với cơ sở dữ liệu MongoDB và gọi hàm chuyển đổi
convert_numeric_fields(collection)

print("Đã chuyển đổi tất cả các trường từ chuỗi thành số thành công.")
print('Tổng số tệp:', collection.count_documents({}))