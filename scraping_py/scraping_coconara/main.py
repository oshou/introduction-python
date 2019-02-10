# -*- coding: utf-8 -*-
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import pandas
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
browser = webdriver.Chrome(
    executable_path="/root/.pyenv/versions/3.6.6rc1/lib/python3.6/site-packages/chromedriver_binary/chromedriver", options=options)
# browser = webdriver.Chrome(
#    executable_path='/usr/local/bin/chromedriver', options=options)

browser.get("https://coconala.com/categories/11")

page = 1

titles = browser.find_element_by_tag_name('title').text
print(titles)

# while True:
#    if len(browser.find_elements_by_css_selector("a.next")) > 0:
#        print("##################### page: {} ########################".format(page))
#        print("Starting to get posts...")
#
#        time.sleep(5)
#        posts = browser.find_element_by_css_selector(".listContentBox")
#        print(len(posts))
#
#        for post in posts:
#            try:
#                title = post.find_element_by_css_selector(
#                    "a.js-service-view-tracker").text
#            except:
#                print("Error:Advertisement appeared.Skipping...")
#    else:
#        print("no pager exist anymore")
#        break
#
#print("Finished Scraping. Writing CSV...")
# df.to_csv("output.csv")
print("DONE")
