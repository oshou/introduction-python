from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import csv

hiragana_list = [
    "あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", "さ", "し", "す", "せ", "そ",
    "た", "ち", "つ", "て", "と", "な", "に", "ぬ", "ね", "の", "は", "ひ", "ふ", "へ", "ほ",
    "ま", "み", "む", "め", "も", "や", "ゆ", "よ", "ら", "り", "る", "れ", "ろ", "わ", "を", "ん"
]

#driver = webdriver.Chrome(
    #executable_path='C:\Program Files\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(
    executable_path='/usr/bin/chromedriver')
driver.get('https://anime.dmkt-sp.jp/animestore/c_all_pc?initialCollectionKey=1')
results = {}
for hiragana in hiragana_list:
    if hiragana != "あ":
        continue_link = driver.find_element_by_link_text(hiragana)
        continue_link.click()

    html01 = driver.page_source
    while True:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        sleep(1)
        html02 = driver.page_source
        if html01 != html02:
            html01 = html02
        else:
            break

    # Parse
    soup = BeautifulSoup(html01, 'html.parser')
    titleAndFavoriteCounts = soup.find_all(class_='textContainerIn')

    # {title: favorite count}
    for titleAndFavoriteCount in titleAndFavoriteCounts:
        title = titleAndFavoriteCount.find(
            class_='ui-clamp webkit2LineClamp').get_text()
        favoriteCount = int(titleAndFavoriteCount.find(
            class_='favoriteCount').get_text())
        results[title] = favoriteCount

driver.close()
driver.quit()

sorted_results = {}
for k, v in sorted(results.items(), key=lambda x: x[1], reverse=True):
    sorted_results[k] = v

field_names = ['anime_title', 'favorite_count']

# output csv
with open("anime_ranking.csv", "w") as f:
    writer = csv.writer(f, delimiter=';')
