# imports for webscraping
from bs4 import *
import requests
import time
import random
import selenium
from selenium.webdriver.common.by import By
import selenium.webdriver as webdriver
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.support.ui import WebDriverWait

URL1 = 'https://steamcommunity.com/market/search?q=&category_440_Collection%5B%5D=any&category_440_Type%5B%5D=tag_TF_KillStreakifierToolC&appid=440#p1_price_desc'
data1 = requests.get(URL1)
soup1 = BeautifulSoup(data1.content, 'html.parser')



pageCount = soup1.find('span',{"id":"searchResults_total"}).text

resultCount = pageCount
pageCount = int(pageCount)

if pageCount> (10*(pageCount//10)):
    pageCount = (pageCount//10)+1
else:
    pageCount = pageCount//10

# initialize arrays to be used for web scraping
name_data = []
prices = []
data = []

soups = []
names = []
name_data2 = []
price_data = []
price_data2 = []
driver = webdriver.Chrome(executable_path=r"C:\Users\Jon\AppData\Local\Programs\Python\Python36-32\Scripts\chromedriver_win32\chromedriver.exe")

# KillStreak Kit Names and Prices
URL = 'https://steamcommunity.com/market/search?q=&category_440_Collection%5B%5D=any&category_440_Type%5B%5D=tag_TF_KillStreakifierToolC&appid=440#p1_price_desc'
driver.get(URL)
time.sleep(2)
# go page by page and collect killstreak information from each one
for x in range(pageCount+1):
    data = driver.page_source
    soup = (BeautifulSoup(data, 'html.parser'))
    if x!=17:
        print('Page ' + str(x + 1) + " Parsed out of " + str(pageCount))

    price_data = soup.find_all('span', {"class": "normal_price"})
    name_data = soup.find_all('span',{"class":"market_listing_item_name"})

    for j in range(len(price_data)):
        if j % 2 == 1:
            prices.append(price_data[j].text)
    for z in range(len(name_data)):
        names.append(name_data[z].text)

    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.ID, 'searchResults_btn_next')))
    time.sleep(2)
    driver.find_element_by_xpath("//span[@id='searchResults_btn_next']").click()
driver.close() # close drivers once finished

# parse through each and print information to text file to be read later.
KitFile = open(os.getcwd()+"/MarketStuff/KitValues.txt","w")
KitFile.write("%-60s % -15s" % ('Killstreak Kit:', 'Prices:') + "\n")
print(len(names))
print(len(prices))
for i in range(len(names)):
    KitFile.write("%-60s % -15s" % (names[i], prices[i]) + "\n")
KitFile.close()




