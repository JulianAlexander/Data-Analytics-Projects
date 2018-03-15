from bs4 import BeautifulSoup
import requests
from splinter import Browser
import re
import pandas as pd
import pymongo
from pymongo import MongoClient
import time
from time import sleep

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    
    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    conn = "mongodb://localhost:27017"
    client = MongoClient('localhost', 27017)
    db = client.mars
    result = db.mars.delete_many({})

    print(soup.prettify())


    title_results = soup.find('div', class_='content_title')
    title = title_results.text.strip()

    para_results = soup.find('div', class_='rollover_description_inner')
    para = para_results.text.strip()

    url = 'https://www.jpl.nasa.gov/spaceimages/index.php?category=Mars'


    browser.visit(url)
    for x in range(1):
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        image = soup.find_all('article', class_='carousel_item')

    for i in image:
        image_url = i['style']
        print(i["style"])


    full_image = image_url.split("'")

    first_url = url.split("space")

    featured_image_url = first_url[0][:-1] + full_image[1]

    time.sleep(10)
    twitter_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(twitter_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    tweet_text = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
    mars_weather = tweet_text.text.strip()

    time.sleep(5)

    fact_url = 'https://space-facts.com/mars/'
    fact_tables = pd.read_html(fact_url)

    fact_df = fact_tables[0]
    fact_df.columns = ['Description','Values']
    fact_df.set_index('Description', inplace=True)

    fact_html = fact_df.to_html()
    
    time.sleep(10)

    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    hemi_titles = ['Cerberus Hemisphere','Schiaparelli Hemisphere','Syrtis Major Hemisphere','Valles Marineris Hemisphere']
    hemi_img_links = []
    for i in range(4):
        browser.visit(hemi_url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        hemi_text = soup.find('a', class_='itemLink product-item')
        browser.click_link_by_partial_text(hemi_titles[i])
        hemi_url_2 = browser.url
        browser.visit(hemi_url_2)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        hemi_img = soup.find_all('a', href=True)
        img_links = []
        for img in hemi_img:
            img_links.append(img['href'])
        hemi_img_links.append(img_links[41])


    hemisphere_image_urls = [
        {'title':hemi_titles[0],'img_url':hemi_img_links[0]},
        {'title':hemi_titles[1],'img_url':hemi_img_links[1]},
        {'title':hemi_titles[2],'img_url':hemi_img_links[2]},
        {'title':hemi_titles[3],'img_url':hemi_img_links[3]}
    ]

    mars_scrape = {
        "title":title,"paragraph":para,"featured_image":featured_image_url,"weather":mars_weather,"table":fact_html,"hemisphere":hemisphere_image_urls
    }

    return mars_scrape

    db.mars.insert_one(mars_scrape)