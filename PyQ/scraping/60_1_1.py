import requests

url = "https://docs.pyq.jp/_static/assets/scraping/test1.html"

response = requests.get(url)
response.encoding = response.apparent_encoding
print(response.text)
