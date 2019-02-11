import requests
from bs4 import BeautifulSoup

url = "https://docs.pyq.jp/_static/assets/scraping/parse1.html"
response = requests.get(url)
response.encoding = response.apparent_encoding

bs = BeautifulSoup(response.text, "html.parser")

ul_tag = bs.find('ul')
for a_tag in ul_tag.find_all('a'):
    text = a_tag.text
    link_url = a_tag['href']
    print('{}: {}'.format(text, link_url))
