import time
import requests

url_html = "https://docs.pyq.jp/_static/assets/scraping/ensyu1.html"
url_csv = "https://docs.pyq.jp/_static/assets/scraping/ensyu1.csv"

response = requests.get(url_html)
response.encoding = response.apparent_encoding
print("HTMLの取得と表示 ----")
ensyu_html = response.text

time.sleep(1)

response = requests.get(url_csv)
response.encoding = response.apparent_encoding
print("CSVの取得と表示 ----")
ensyu_csv = response.text

with open('ensyu1.html', mode='w', encoding='utf-8') as fp:
    fp.write(ensyu_html)

with open('ensyu1.csv', mode='w', encoding='utf-8') as fp:
    fp.write(ensyu_csv)

print('保存完了')
