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

time.sleep(2)

password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys("phatho0317")
pw = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
pw.click()

time.sleep(5)
search = driver.find_element(By.XPATH, "//input[@data-testid='SearchBox_Search_Input']")
idol = "M-TP"
search.send_keys(idol)
search.send_keys(Keys.ENTER)

time.sleep(2)
people = driver.find_element(By.XPATH,"//span[contains(text(),'People')]")
people.click()

time.sleep(2)
name_idol = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[1]/div/div/button/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]")
name_idol.click()

#
userID=[]
timePost=[]
tweetText=[] #= Post status
like=[]
reply=[]
resport=[]
view=[]
tweetIMG=[]

userID = driver.find_element(By.XPATH,"//div[data-testid='User-Name']").text
timePost = driver.find_element(By.XPATH,"//time").get_attribute("datetime")
tweetText = driver.find_element(By.XPATH,"//div[data-testid='tweetText']")
like = driver.find_element(By.XPATH,"//div[data-testid='like']")
reply = driver.find_element(By.XPATH,"//div[data-testid='reply']")
resport = driver.find_element(By.XPATH,"//div[data-testid='retweet']")
view = By.CLASS_NAME #TIM CACH LAY

