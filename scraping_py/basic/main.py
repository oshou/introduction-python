# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# レスポンス取得、Parse(構造化&要素分解)
res = requests.get('http://gigazine.net/')
html = res.content
soup = BeautifulSoup(html, 'html.parser')

#title_tag = soup.title
#title = title_tag.string
#title = soup.title.string
title = soup.title

print(title)
