# ---------------------------------------------------------------------
# 웹 페이지 가져오기
# ---------------------------------------------------------------------
from urllib.request import urlopen

html = urlopen('http://www.daangn.com/hot_articles')
print(type(html))

print(html.read())

# ---------------------------------------------------------------------
# BeautifulSoup Library
# ---------------------------------------------------------------------
from urllib.request import urlopen
from bs4 import BeautifulSoup

# html 불러오기
html = urlopen('http://www.pythonscraping.com/pages/page1.html')

# html을 객체로 저장 -> 태그에 접근 가능(beautifulsoup 사용하는 이유)
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs)
print(type(bs)) # class type

print(bs.h1)
print(bs.title)

# ---------------------------------------------------------------------
# 존재하지 않는 태그 예외 처리
# ---------------------------------------------------------------------
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url, tag):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsobj = BeautifulSoup(html.read(), 'html.parser')
        value = bsobj.body.find(tag)
    except AttributeError as e:
        return None
    return value

tag = 'h2'
value = getTitle('http://www.pythonscraping.com/pages/page1.html', tag)
if value == None:
    print(f'{tag} could not be found')
else:
    print(value)