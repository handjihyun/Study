from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import re


# Wikipedia 페이지 가져오기
html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

# 항목 링크 찾기 
body_content = bs.find('div', {'id':'bodyContent'})
pattern = '^(/wiki/)((?!:).)*$'
for link in body_content.find_all('a', href = re.compile(pattern)):
    if 'href' in link.attrs:
        print(link.attrs['href'])
print('-'*100)

# 링크간 무작위 이동하기: 소스코드
# random.seed(datetime.datetime.now()): 시간에 따라 초기값 설정
random.seed(None)   # Python3.9 이상부터 None을 넣어도 위 기능이 됨

def getLinks(articleURL):
    html = urlopen('https://en.wikipedia.org' + articleURL)
    bs = BeautifulSoup(html, 'html.parser')
    bodyContent = bs.find('div', {'id':'bodyContent'})
    wikiURL = bodyContent.find_all('a', href = re.compile('^(/wiki/)((?!:).)*$'))
    return wikiURL

links = getLinks('/wiki/Kevin_Bacon')
print('links 길이: ', len(links))
i = 1
while(len(links)) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(f"[{i:3}] {newArticle}")
    links = getLinks(newArticle)
    i += 1

# 같은 페이지를 두 번 크롤링 하지 않기
# getLinks() 함수 수정: set 사용
pages = set()
count = 0

def getLinks(pageUrl):
    global pages, count
    html = urlopen('https://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href = re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 새로운 페이지 발견
                newPage = link.attrs['href']

                count += 1
                print('[{0}]: {1}'.format(count, newPage))
                pages.add(newPage)  # 세트에 추가
                getLinks(newPage)

getLinks('')

# 전체 사이트 데이터 수집 소스
pages = set()
count = 0

def getLinks(pageUrl):
    global pages
    global count
    html = urlopen('https://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id='mw-context-text').find('p ').text)
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError as e:
        print('this page is missing something! Continuing: ', e)

    for link in bs.find_all('a', href = re.compile('^(/wiki/)')):
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                    # 새로운 페이지 발견
                    newPage = link.attrs['href']
                    print('-'*40)
                    count += 1
                    print('[{0}]: {1}'.format(count, newPage))
                    pages.add(newPage)  # 세트에 추가
                    getLinks(newPage)

getLinks('')

# 인터넷 크롤링 : URL 구조
# - urllib.urlparse : HTTP요청, 파싱과 관련된 패키지
from urllib.parse import urlparse

urlString1 = 'https://shopping.naver.com/home/p/index.naver'

url = urlparse(urlString1)
print(url.scheme)
print(url.netloc)
print(url.path)

# --------------------------------------------------------------------
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(None)
def getInternalLinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    internalLinks = []

    for link in bs.find_all('a', href=re.compile('^(/|.*' + includeUrl + ')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if (link.attrs['href'].startswith('/')):
                    internalLinks.append(includeUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks
    
def getExternalLinks(bs, excludeUrl):
    externalLinks = []

    for link in bs.find_all('a', href=re.compile('^(http|www)((?!' + excludeUrl + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def getRandomExternalLink(startingPage):
    try:
        html = urlopen(startingPage)
        bs = BeautifulSoup(html, 'html.parser')
        externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)

        if len(externalLinks) == 0:
            print('No external links, looking around the site for one')
            domain = '{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
            internalLinks = getInternalLinks(bs, domain)
            return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks) - 1)])
        else:
            return externalLinks[random.randint(0, len(externalLinks) - 1)]
    except Exception as e:
        print('Exception 발생: ', e)

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print('Random external link is: {}'.format(externalLink))
    followExternalOnly(externalLink)

followExternalOnly('http://oreilly.com')