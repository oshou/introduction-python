# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

res = requests.get('http://gigazine.net/')
content = res.content

soup = BeautifulSoup(content, 'html.parser')
title_tag = soup.title
title = title_tag.string

print(title_tag)
print(title)
