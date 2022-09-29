import time #to use seelp if you want to slow down the progreession a point
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd #imprts data into a data frame, making exporting a lot easier

url = "https://www.youtube.com/c/CyberpunkGame/videos"

driver= webdriver.Chrome()
# r"C:\Users\16075\Documents\work\ScapeDynamic\chromedriver.exe"
driver.get(url)


# style-scope ytd-grid-video-renderer
# #above line is classname of div which hold inside all the following paths below
# name =//*[@id="video-title"]

#key difference, here use find elementS while in the iteration use find ELEMENT
videos = driver.find_elements(By.CLASS_NAME, "style-scope ytd-grid-video-renderer" )

video_list = []#make list of dictonares each about a video

for video in videos:
    #both ways of wrting find element works wanted to demonstate it
    title=video.find_element(By.XPATH, './/*[@id="video-title"]').text
    views = video.find_element('xpath', './/*[@id="metadata-line"]/span[1]').text 
    age = video.find_element('xpath','//*[@id="metadata-line"]/span[2]').text 
    # print(title, views, age)
    vid_item={
        'title': title,
        'views': views,
        'posted': age,
    }
    
    video_list.append(vid_item)
    
dataFrame = pd.DataFrame(video_list)
print(dataFrame)
# print(video_list)
driver.quit()