#!/usr/bin/env python
# coding: utf-8

import re
import os
import sys
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import uuid

import googletrans
from googletrans import Translator

def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.

# Specifying incognito mode as you launch your browser[OPTIONAL]
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
browser = webdriver.Chrome(executable_path= str(os.getcwd()) + '/chromedriver.exe', options=option)

# df = pd.read_excel('russialist.xlsx')
# provinces = df['Names']

df = pd.read_html('https://en.wikipedia.org/wiki/List_of_cities_in_Brazil_by_population')
df = df[2]
print(type(df))
# for col in df.columns: 
#     print(col) 
# df = df['City']
# print(type(df))
# print(provinces)
provinces = df['City'].tolist()
# print(provinces)
translator = Translator()
provinces = provinces[200:]
provinces = [translator.translate(element).text for element in provinces]
# print(provinces)




queries = ['Universities ', 'Colleges', 'Higher Education']
data = pd.read_excel(r'Gmaps_Result_in_Brazil.xlsx')
# data = pd.DataFrame(columns = ['Provinces', 'Links']) 
# print(data)

# print(data)
# print(type(data))
for province in provinces:
    print('-----'+str(province)+'-----')
    for query in queries:
        links = []
        error = []
        try:
            # Go to desired website
            browser.get("https://www.google.com/maps/search/" + str(query) + ' in ' + str(province) + "/")
            time.sleep(5)
            next_button = browser.find_elements_by_xpath('//*[@id="n7lv7yjyC35__section-pagination-button-next"]/span')
            #Iterate over all results until next button is unclickable
            while(1):
                soup = BeautifulSoup(browser.page_source, 'html.parser')
                insti_soup = soup.find_all('div', attrs={'class': 'section-result-content'})
                for i in range(0, len(insti_soup)):
                    try:
                        links.append((re.search('href="(.+?)"', str(insti_soup[i].find('a', {'class' : 'section-result-action'})))).group(1))
                    except:
                        # print('Error in', i )
                        error.append(insti_soup[i])

                next_button[0].click()
                time.sleep(5)
        except:
            # if(len(links)==0)
            #     continue
            # links = list(set(links))
            if len(links) == 0:
                continue
            for url in links: 
                print(url)
                data = data.append({'Provinces' : str(province), 'Links' : url}, ignore_index = True)
            # if(str(province) in data.keys()):
            #     data[str(province)] = list(set(links))
            # original_list = data[str(province)]
            # original_list = original_list.extend(links)
            # original_list = list(set(original_list))
            # data[str(province)] = original_list
            # df = pd.DataFrame(data = links, columns = ["Link"], index = None, )
            # print(df)
            # try:
            #     df.to_excel('Gmaps_Result_' + str(query) + ' in ' + str(province) + '.xlsx', index=False, header=False)
            #     with open('Error_' + str(query) + ' in ' + str(province) +  '.txt', 'w') as f:
            #         for item in error:
            #             try:
            #                 f.write("%s\n" % item)
            #             except:
            #                 f.write("Encoding Error")
            # except:
            #     df.to_excel('Gmaps_Result_' + str(query).replace('.','_') + ' in ' + my_random_string(10) + '.xlsx', index=False, header=False)
            #     with open('Error_' + str(query).replace('.','_') + ' in ' + my_random_string(10) +  '.txt', 'w') as f:
            #         for item in error:
            #             try:
            #                 f.write("%s\n" % item)
            #             except:
            #                 f.write("Encoding Error")

# data.drop_duplicates(keep=False,inplace=True) 
data.to_excel('Gmaps_Result_in_Brazil' + '.xlsx', index=False, header=True, startrow = 0)
# browser.close()
