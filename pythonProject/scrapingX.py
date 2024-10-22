from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://x.com/i/flow/login")

time.sleep(5)

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
search = driver.find_element(By.XPATH, "//input[@data-testid='SearchBox_Search_Input']")
idol = "M-TP"
search.send_keys(idol)
search.send_keys(Keys.ENTER)

time.sleep(5)
people = driver.find_element(By.XPATH, "//span[contains(text(),'People')]")
people.click()

time.sleep(7)
name_idol = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/section/div/div/div[1]/div/div/button/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]")
time.sleep(2)
people = driver.find_element(By.XPATH, "//span[contains(text(),'People')]")
people.click()

time.sleep(2)
name_idol = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[1]/div/div/button/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]")
name_idol.click()

#
userIDs=[]
timePosts=[]
tweetTexts=[] #= Post status
likes=[]
replys=[]
resports=[]
#view=[]
#tweetIMG=[]

#Tim xem co bao nhieu post
TWEETs = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
while True:
    userIDs = driver.find_element(By.XPATH, "//div[data-testid='User-Name']").text
    timePost = driver.find_element(By.XPATH,"//time").get_attribute("datetime")
    tweetText = driver.find_element(By.XPATH,"//div[data-testid='tweetText']")
    like = driver.find_element(By.XPATH,"//div[data-testid='like']")
    reply = driver.find_element(By.XPATH,"//div[data-testid='reply']")
    resport = driver.find_element(By.XPATH,"//div[data-testid='retweet']")

    for TWEET in TWEETs:

        userID = driver.find_element(By.XPATH,".//div[@data-testid='User-Name']").text
        userIDs.append(userID)

        timePost = driver.find_element(By.XPATH,".//time").get_attribute("datetime")
        timePosts.append(timePost)

        tweetText = driver.find_element(By.XPATH,".//div[@data-testid='tweetText']").text
        tweetTexts.append(tweetText)

        try:
            reply = driver.find_element(By.XPATH, ".//div[@data-testid='reply']").text
        except:
            reply = ''
        replys.append(reply)

        try:
            resport = driver.find_element(By.XPATH, ".//div[@data-testid='retweet']").text
        except:
            resport = ''
        resports.append(resport)

        try:
            like = driver.find_element(By.XPATH, ".//div[@data-testid='like']").text
        except:
            like = ''
        likes.append(like)


    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    sleep(3)
    TWEETs = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
    Stop = list(set(tweetTexts))
    if len(Stop) >5:
        break
print(len(userIDs),
      len(timePosts),
      len(tweetTexts),
      len(likes),
      len(replys),
      len(resports))

df = pd.DataFrame(zip(userIDs,timePosts,tweetTexts,likes,replys,resports),
                  columns=['userIDs','timePosts','tweetTexts','likes','replys','resports'])
df.head()
filename = 'X.xlsx'
df.to_excel(filename)
print("File excel saved")