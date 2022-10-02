import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
import pandas as pd 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


url = "https://www.youtube.com/results?search_query=god+of+war"
driver = webdriver.Chrome()#same directory no need for a path
driver.get(url)
num=0


SCROLL_PAUSE_TIME = 2
while num <=5:#give me the data of 5 pages
    
    down = driver.find_element(By.TAG_NAME,'html')
    down.send_keys(Keys.END)
    # Wait to load page content
    time.sleep(SCROLL_PAUSE_TIME)

    num+=1

    
video_links= driver.find_elements(By.XPATH,'//*[@id="video-title"]')
video_link_list=[]
for link in video_links:
    #https://selenium-python.readthedocs.io/api.html?highlight=get_attribute#selenium.webdriver.remote.webelement.WebElement.get_dom_attribute
    video_link_list.append(link.get_attribute('href') )
    #using a scrol down and next page command with click will allow the loop to contiune
    
video_title = driver.find_elements(By.XPATH,'//*[@id="video-title"]/yt-formatted-string')
titles_list=[]
for title in video_title:
    
    titles_list.append(title.text)

chanelsNames= driver.find_elements(By.XPATH,'//*[@id="text"]/a')
chanels_list=[]
for theName in chanelsNames:
    
    chanels_list.append(theName.text)
    
    
views= driver.find_elements(By.XPATH,'//*[@id="metadata-line"]/span[1]')
viewData_list=[]
for eyeBalls in views:

    viewData_list.append(eyeBalls.text)
    
ageOfPost= driver.find_elements(By.XPATH,'//*[@id="metadata-line"]/span[2]')
date_posted_list=[]
for posted in ageOfPost:

    date_posted_list.append(posted.text)


dataChart = {   'title': titles_list,
                'chanel': chanels_list,
                'views': viewData_list,
                'date': date_posted_list,
                'links': video_link_list}
df = pd.DataFrame.from_dict(dataChart, orient='index')
df = df.transpose()

#at the end nones appear because ther was no scholl down comand or click next botton 
print(df)
driver.quit()



#https://selenium-python.readthedocs.io/search.html?q=keys&check_keywords=yes&area=default
# driver.sendKeys(Keys.PAGE_DOWN);

# videoCards = driver.find_elements(By.CLASS_NAME,'scaffold-layout__list-container')
# videoCards = driver.find_elements(By.CLASS_NAME, "style-scope ytd-video-renderer")
# recomend_list=[]

# for video in videoCards:
#     print("===>> enter loop")
#     TITLE= video.find_element(By.XPATH,'//*[@id="video-title"]/yt-formatted-string').text
#     chanel= video.find_element(By.XPATH, '//*[@id="text"]').text
#     views= video.find_element('xpath','//*[@id="metadata-line"]/span[1]').text
#     postedTime = video.find_element('xpath','//*[@id="metadata-line"]/span[2]').text
    
#     video_card ={
#         'Title':TITLE,
#         'chanel':chanel,
#         'views': views,
#         'postedTime': postedTime
#     }
#     recomend_list.append(video_card)
    
    #above code to create any row and few columns for the data was not able to functions due to being stuck in one channel
    
    #below causes few rows and many columns throught mutople loops to harvest all the data
        
    

# if len(viewData_list) != len(chanels_list) or len(titles_list) != len(date_posted_list) or len(chanels_list) != len(titles_list) or len(video_link_list):
    
#     pass

    
#causes a  block of text, all there though
# dataFrame = pd.DataFrame = ((titles_list, chanels_list, viewData_list, date_posted_list, video_link_list))

#bring out many NAN
# dataFrame = pd.DataFrame([{'title': titles_list},
#                           {'chanel': chanels_list},
#                           {'views': viewData_list},
#                           {'date': date_posted_list},
#                           {'links': video_link_list}])


# SCROLL_PAUSE_TIME = 0.5

# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height