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


def get_item_details(df):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    df2 = pd.DataFrame(columns=['brand', 'price', 'rank', 'skin_type', 'ingredients'])
    df = pd.concat([df, df2], axis = 1)
    for i in range(len(df)):
        url = df.URL[i]
        print(url)
        try:
            driver.get(url)
        except:
            print('driver timeout')
            continue
        try:
            brand = driver.find_element(By.XPATH, '//a[contains(@data-at, "brand_name")]')
            df['brand'][i]  = brand.text
        except:
            df['brand'][i] = 'NA'
            
        try:
            price_div = driver.find_element_by_class_name('css-1oz9qb')
            price = price_div.find_element(By.XPATH, "//*[@class='css-1oz9qb']")
            df['price'][i]  = price.text
        except:
            df['price'][i] = 'NA'
        try:
            rank_ele = driver.find_element(By.XPATH, '//span[contains(@data-comp, "StarRating")]')
            rank = rank_ele.get_attribute('aria-label')
            df['rank'][i] = rank
        except:
            df['rank'][i] = 'NA';
        
        try:
            skin_type_div = driver.find_element(By.XPATH, '//div[.//b[contains(., "What it is")]]')
            skin_type_idx = [i for i, item in enumerate(skin_type_div.text.split('\n')) if item.startswith('Skin Type')]
            skin_type = skin_type_div.text.split('\n')[skin_type_idx[0]]
            df['skin_type'][i] = skin_type
        except:
            df['skin_type'][i] = 'NA'
            print('Best for not found in first try')
#             try:
#                 skin_type_ele = driver.find_element(By.XPATH, "//*[contains(text(), 'Best for')]")
#                 print(skin_type_ele.text)
#             except:
#                 print('Best for not found in second try')
        try:
            ingredients_div = driver.find_element(By.XPATH,'//div[contains(@aria-labelledby, "ingredients_heading")]/div')
            ingredients_idx = [i for i, item in enumerate(ingredients_div.get_attribute("innerText").split('\n')) if re.search('water', item, re.IGNORECASE)]
            ingredients = ingredients_div.get_attribute("innerText").split('\n')[ingredients_idx[0]]
            df['ingredients'][i] = ingredients
        except:
            df['ingredients'][i] = 'NA'
            print('Ingredients div not found')

    return df


df2 = get_item_details(df)
df2.to_csv('cosmetic.csv', encoding = 'utf-8-sig', index = False)
