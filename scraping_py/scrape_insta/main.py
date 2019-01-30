#!/usr/bin/python
# -*- coding: utf-8 -*-
# https://www.promptcloud.com/blog/how-to-scrape-instagram-data-using-python
import requests
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json


class InstagramInfoScraper:
    def get_user_info(self, url):
        html = urllib.request.urlopen(url, context=self.ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find_all('meta', attrs={'property': 'og:description'})
        text = data[0].get('content').split()
        print(text)

        user = '%s %s %s' % (text[-3], text[-2], text[-1])
        followers = text[0]
        followings = text[2]
        posts = text[4]

        info = {}
        info['user'] = user
        info['followers'] = followers
        info['followings'] = followings
        info['posts'] = posts
        self.info_arr.append(info)
        print('---------------------------------------------------------')

    def main(self):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE
        self.info_arr = []

        with open('users.txt') as f:
            self.content = f.readlines()
        self.content = [x.strip() for x in self.content]
        for url in self.content:
            self.get_user_info(url)
        with open('info.json', 'w')as outfile:
            json.dump(self.info_arr, outfile, indent=4)
        print("Json file containing required info is created .......")


if __name__ == '__main__':
    obj = InstagramInfoScraper()
    obj.main()
