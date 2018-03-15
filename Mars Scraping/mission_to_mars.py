
# coding: utf-8

# In[125]:


from bs4 import BeautifulSoup
import requests
from splinter import Browser
import re
import pandas as pd


# In[6]:


url = 'https://mars.nasa.gov/news/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[7]:


print(soup.prettify())


# In[8]:


title_results = soup.find_all('div', class_='content_title')


# In[9]:


mars_titles = []
for result in title_results:
    mars_titles.append(result.text.strip())


# In[10]:


mars_titles


# In[11]:


para_results = soup.find_all('div', class_='rollover_description_inner')


# In[12]:


mars_p = []
for result in para_results:
    mars_p.append(result.text.strip())


# In[13]:


mars_p


# In[36]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[15]:


url = 'https://www.jpl.nasa.gov/spaceimages/index.php?category=Mars'


# In[92]:


browser.visit(url)
for x in range(1):
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image = soup.find_all('article', class_='carousel_item')
    #browser.click_link_by_partial_text('FULL IMAGE')

for i in image:
    image_url = i['style']
    print(i["style"])


# In[93]:


full_image = image_url.split("'")

first_url = url.split("space")

featured_image_url = first_url[0][:-1] + full_image[1]


# In[94]:


featured_image_url


# In[121]:


twitter_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(twitter_url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
tweet_text = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
mars_weather = tweet_text.text.strip()


# In[122]:


mars_weather


# In[156]:


fact_url = 'https://space-facts.com/mars/'
fact_tables = pd.read_html(fact_url)
fact_tables


# In[158]:


fact_df = fact_tables[0]
fact_df.columns = ['Description','Values']
fact_df.set_index('Description', inplace=True)
fact_df


# In[159]:


fact_html = fact_df.to_html()
fact_html


# In[215]:


hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
hemi_titles = ['Cerberus Hemisphere','Schiaparelli Hemisphere','Syrtis Major Hemisphere','Valles Marineris Hemisphere']
hemi_img_links = []
for i in range(4):
    browser.visit(hemi_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hemi_text = soup.find('a', class_='itemLink product-item')
    browser.click_link_by_partial_text(hemi_titles[i])
    hemi_image_links.append(browser.url)
    hemi_url_2 = browser.url
    browser.visit(hemi_url_2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hemi_img = soup.find_all('a', href=True)
    img_links = []
    for img in hemi_img:
        img_links.append(img['href'])
    hemi_img_links.append(img_links[42])


# In[216]:


hemi_img_links


# In[217]:


hemisphere_image_urls = [
    {'title':hemi_titles[0],'img_url':hemi_img_links[0]},
    {'title':hemi_titles[1],'img_url':hemi_img_links[1]},
    {'title':hemi_titles[2],'img_url':hemi_img_links[2]},
    {'title':hemi_titles[3],'img_url':hemi_img_links[3]}
]


# In[218]:


hemisphere_image_urls

