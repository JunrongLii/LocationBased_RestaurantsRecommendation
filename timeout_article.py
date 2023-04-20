#detroit
import re
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import json




def parse_html(html):
    soup = BeautifulSoup(html,'lxml')
    dine_list = []
    resto = soup.find('header', class_='_header_1wadv_1')
    section1stTitle = resto.find('h1',class_='_h1_1wadv_5').text
    dict = {}
    article_list = []
    head_zone = soup.find('div',class_='_zoneItems_ncpe6_1')
    for article in head_zone.find_all('div', class_='_articleContent_1pzwm_26'):
        temp = {}
        temp['name'] = article.find('h3', class_='_h3_cuogz_1').text
        temp['url'] = 'https://www.timeout.com' + article.find('a')['href']
        article_list.append(temp)
    dict[section1stTitle] = article_list
    dine_list.append(dict)
    for resto in soup.find_all('div', class_='zone _zone_abr0c_1'):
        section = resto.find('h2',class_='_h2_1ikgb_1')
        section_title = section.find('span').text
        #print(title)
        dict={}
        article_list=[]
        for i in resto.find_all('div', class_='_zoneItems_1ktxs_1'):
            for article in i.find_all('div', class_='_articleContent_1pzwm_26'):
                temp = {}
                temp['name'] = article.find('h3',class_='_h3_cuogz_1').text
                temp['url'] = 'https://www.' + article.find('a')['href']
                article_list.append(temp)
        dict[section_title] = article_list
        dine_list.append(dict)
        for i in resto.find_all('div', class_=''):
            for article in i.find_all('div', class_='_articleContent_1pzwm_26'):
                temp = {}
                temp['name'] = article.find('h3',class_='_h3_cuogz_1').text
                temp['url'] = 'https://www.' + article.find('a')['href']
                article_list.append(temp)
        dict[section_title] = article_list
        dine_list.append(dict)

    return dine_list

CACHE_FILENAME = "Timeout_articles.json"

def open_cache():
    try:
        cache_file = open(CACHE_FILENAME, 'r')
        cache_contents = cache_file.read()
        cache_dict = json.loads(cache_contents)
        cache_file.close()
    except:
        cache_dict = {}
    return cache_dict

def save_cache(cache_dict):
    dumped_json_cache = json.dumps(cache_dict)
    fw = open(CACHE_FILENAME,"w")
    fw.write(dumped_json_cache)
    fw.close()


def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = 'https://www.timeout.com/newyork/food-drink'
    driver.get(url)
    sleep(0)
    page = driver.page_source
    data = parse_html(page)
    newdata = []
    for i in data:
        if i not in newdata:
            newdata.append(i)
    del newdata[2]
    save_cache(newdata)
    dict = open_cache()
    return dict





















