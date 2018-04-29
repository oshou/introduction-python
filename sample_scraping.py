import re

with open("target.html") as f:
    html = f.read()

for row in re.findall(r"<a.*?</a>", html, re.DOTALL):
    url = re.search(r"<a href=""(.*?)"">",row).group(1)
    print(url)
