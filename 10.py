from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://www.zhihu.com/question/20899988.html")
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)