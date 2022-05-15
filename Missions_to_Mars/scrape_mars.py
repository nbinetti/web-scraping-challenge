#!/usr/bin/env python
# coding: utf-8

# In[3]:


#dependencies
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


# In[4]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# # NASA Mars News

# In[5]:


#URL of page
url = 'https://redplanetscience.com/'
browser.visit(url)
time.sleep(1)


# In[6]:


#Scrape page into Soup
html = browser.html
soup = bs(html, "html.parser")


# In[7]:


news_title = soup.find_all('div', class_='content_title')[0].text
news_p = soup.find_all('div', class_='article_teaser_body')[0].text
# print(f"news_title: {news_title}")
# print(f"news_p: {news_p}")


# JPL Mars Space Images - Featured Image

# In[8]:


jpl_url = 'https://spaceimages-mars.com/'
browser.visit(jpl_url)
time.sleep(3)


# In[9]:


html=browser.html
soup=bs(html, 'html.parser')
image_url = soup.find("a", class_ = "showimg fancybox-thumbs")["href"]
featured_image_url = jpl_url + image_url
# featured_image_url


# Mars Facts

# In[10]:


facts_url = "https://galaxyfacts-mars.com"
browser.visit(facts_url)


# In[11]:


tables = pd.read_html(facts_url)
# print(tables)
df = tables[1]
df.columns = ["Description", "Value"]
df.set_index("Description", inplace=True)
# df

              


# Mars Hemispheres

# In[12]:


hemispheres_url = "https://marshemispheres.com/"
browser.visit(hemispheres_url)


# In[13]:


time.sleep(4)
hemisphere_html = browser.html
soup = bs(hemisphere_html, 'html.parser')


# In[14]:


items = soup.find_all("div", class_="item")
hemisphere_urls = []

for i in range(4):
    #create empty dictionary
    hemispheres = {}
    browser.find_by_css('a.product-item h3')[i].click()
    element = browser.links.find_by_text('Sample').first
    img_url = element['href']
    title = browser.find_by_css("h2.title").text
    hemispheres["img_url"] = img_url
    hemispheres["title"] = title
    hemisphere_urls.append(hemispheres)
    browser.back()


# In[15]:


# hemisphere_urls


# In[16]:


browser.quit()


# In[ ]:




