from selenium import webdriver
import pandas as pd

browser = webdriver.PhantomJS()
url = "https://qiita.com"
browser.get(url)
df = pd.DataFrame({'title': [], 'date': [], 'like': []})

while True:
    if len(browser.find_element_by_class_name('要素')) > 0:
        posts = browser.find_element_by_class_name('要素')
        for post in posts:
            title = post.find_element_by_css_selector('要素').text
            date = post.find_element_by_css_selector('要素').text
            like = post.find_element_by_css_selector('要素').text
            series = pd.Series([title, date, like], [
                               'title', 'date', 'bookmarks'])
            print(series)
            df = df.append(series, ignore_index=True)

        link = browser.find_element_by_link_text('要素')
        link.click()
        browser.implicitly_wait(10)
    else:
        break

df['like'] = pd.to_numeric(df['like'].str.replace('users', ''))
df = df.sort_values(['like'], ascending=False).reset_index(drop=True)
df.to_csv('hoge.csv')
print('完了')
