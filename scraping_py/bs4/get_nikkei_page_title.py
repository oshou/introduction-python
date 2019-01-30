from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import time

time_flag = True

while True:
    if datetime.now().minute != 59:
        time.sleep(58)
        continue

    f = open('nikkei_heikin.csv', 'a')
    writer = csv.writer(f.lineterminator='\n')

    while datetime.now().second != 59:
        time.sleep(1)
    time.sleep(1)

    csv_list = []
    time_ = datetime.now().strftime("%Y/%m%d %H:%M:%S")
    csv_list.append(time_)

    url = "http://www.nikkei.com/markets/kabu/"

    html = urlopen(url)

    soup = BeautifulSoup(html, "html.parser")

    span = soup.find_all("span")

    nikkei_heikin = ""
    for tag in span:
        try:
            string_ = tag.get("class").pop(0)
            if string_ in "mkc-stock-prices":
                nikkei_heikin = tag.string
                break
        except:
            pass

    print time_, nikkei_heikin
    csv_list.append(nikkei_heikin)

url = "http://www.nikkei.com"

html = urlopen(url)

soup = BeautifulSoup(html, 'html.parser')

title_tag = soup.title
title = title_tag.string

print(title_tag)
print(title)
