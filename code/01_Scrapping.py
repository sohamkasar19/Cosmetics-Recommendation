from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selectorlib import Extractor
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import json
import time
import pandas as pd
import re

def search_item_url(tickers):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    df = pd.DataFrame(columns=['Label','Name', 'URL'])
    for ticker in tickers:
        page = 1
        while True:
            try:
                url = 'https://www.sephora.com/shop/' + ticker + '?pageSize=100&currentPage=' + str(page)
                driver.get(url)
                body = driver.find_element_by_css_selector('body')
                containers = driver.find_elements_by_class_name('css-1qe8tjm')
                if not containers:
                    break
                i=0
                for items in containers:
#                     print(items.text.split('\n')[1])
                    name = items.text.split('\n')[1]
                    link = items.find_element_by_class_name('css-klx76');
                    url = link.get_attribute('href')
                    dic = {'Label': ticker, 'Name': name, 'URL': url}
                    df = df.append(dic, ignore_index = True)
                    i+=1
#                     print(i)
                    if i % 3 == 0 :
                        body.send_keys(Keys.PAGE_DOWN)
                    driver.implicitly_wait(4)
                    print(link.get_attribute('href'))

                print("Page "+ str(page) +" ---DONE---")
                page += 1
            except:
                print('in except')
                break
    
    return (df)

tickers = ['moisturizing-cream-oils-mists', 'cleanser', 'facial-treatments', 'face-mask',
           'eye-treatment-dark-circle-treatment', 'sunscreen-sun-protection']
# tickers = ['cleanser']
df = search_item_url(tickers)