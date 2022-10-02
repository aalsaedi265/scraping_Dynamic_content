import time #to use seelp if you want to slow down the progreession a point
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pandas as pd #imprts data into a data frame, making exporting a lot easier

url = "https://www.youtube.com/c/CyberpunkGame/videos"
#need path no in direcoty
driver= webdriver.Chrome(r"C:\Users\16075\Documents\work\automationScrap\chromedriver.exe")
# r"C:\Users\16075\Documents\work\automationScrap\chromedriver.exe"
driver.get(url)

communityTab = driver.find_element(By.XPATH,'//*[@id="tabsContent"]/tp-yt-paper-tab[4]/div')
communityTab.click()

time.sleep(1)

homePage= driver.find_element(By.XPATH,'//*[@id="tabsContent"]/tp-yt-paper-tab[1]/div')
homePage.click()

time.sleep(1)

fullScreen = driver.find_element(By.XPATH,'//*[@id="c4-player"]/div[26]/div[2]/div[2]/button[7]')
fullScreen.click()

time.sleep(21)
driver.quit()