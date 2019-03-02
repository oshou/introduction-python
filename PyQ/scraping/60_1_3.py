import time
import requests

url_html = "https://docs.pyq.jp/_static/assets/scraping/test1.html"
url_csv = "https://docs.pyq.jp/_static/assets/scraping/test2.csv"

response = requests.get(url_html)
response.encoding = response.apparent_encoding
print("HTMLの取得と表示 ----")
print(response.text)

time.sleep(1)

response = requests.get(url_csv)
response.encoding = response.apparent_encoding
print("CSVの取得と表示 ----")
print(response.text)
