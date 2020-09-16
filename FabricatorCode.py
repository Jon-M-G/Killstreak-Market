# imports for webscraping
from bs4 import *
import requests
import time
import random
import selenium
import selenium.webdriver as webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import selenium.webdriver as webdriver
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager


# establish driver for web scraping with selenium
driver = webdriver.Chrome(executable_path=r"C:\Users\Jon\AppData\Local\Programs\Python\Python36-32\Scripts\chromedriver_win32\chromedriver.exe")

URL1 = 'https://steamcommunity.com/market/search?q=Professional+Killstreak+Fabricator#p1_price_desc'
data1 = requests.get(URL1)
soup1 = BeautifulSoup(data1.content, 'html.parser')



pageCount = soup1.find('span',{"id":"searchResults_total"}).text

resultCount = pageCount
pageCount = int(pageCount)

if pageCount> (10*(pageCount//10)):
    pageCount = (pageCount//10)+1
else:
    pageCount = pageCount//10

# initialize arrays for web scraping
name_data = []
prices = []
data = []

soups = []
names = []
name_data2 = []
price_data = []
price_data2 = []


URL = 'https://steamcommunity.com/market/search?q=Professional+Killstreak+Fabricator#p1_price_desc'
driver.get(URL)

# KillStreak Fabricator Names and Price Code Block
# https://steamcommunity.com/market/search?q=professional+killstreak+fabricator#p1_price_desc

# go page to page collecting all the information and adding it to the arrays
time.sleep(2) # add delay to not be denied by steams anti-DDOS measures
for x in range(pageCount+1):

    data = driver.page_source
    soup = (BeautifulSoup(data, 'html.parser'))
    print('Page ' + str(x) + " Parsed out of " + str(pageCount))

    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.ID, 'searchResults_btn_next')))
    time.sleep(2)
    driver.find_element_by_xpath("//span[@id='searchResults_btn_next']").click()

    price_data = soup.find_all('span', {"class": "normal_price"})
    name_data = soup.find_all('span',{"class":"market_listing_item_name"})

    for j in range(len(price_data)):
        if j % 2 == 1:
            prices.append(price_data[j].text)
    for z in range(len(name_data)):
        names.append(name_data[z].text)

driver.close() # close drivers once finished



FabFile = open(os.getcwd()+"/MarketStuff/FabValues.txt","w")
FabFile.write("%-85s % -15s" % ('Killstreak Fabricator:', 'Prices:') + "\n")

print(len(names))
print(len(prices))
for i in range(len(names)): # print information to a text document for be read later.
    FabFile.write("%-85s % -15s" % (names[i], prices[i]) + "\n")
FabFile.close()




