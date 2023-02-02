# ------------------------------------------------------------
# 6장. 데이터 저장
# ------------------------------------------------------------

# ------------------------------------------------------------
# 미디어 파일
# - urlretrieve() 함수
#   : url로 표시된 네트워크 객체를 로컬 파일로 복사
#   : filename => 복사할 파일 위치 및 이름 지정
# ------------------------------------------------------------
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
home_image = bs.find('img', {'class':'pagelayer-img'})
image_location = home_image['src']  # <img> 태그의 'src' 속성값

print(image_location)
urlretrieve(image_location, 'img/logo.jpg')

# ------------------------------------------------------------
# src 속성이 있는 태그에 연결된 내부 파일 출력
# ------------------------------------------------------------
downloadList = bs.find_all(src=True)    # src 속성이 있는 태그를 찾음

for down_url in downloadList:
    print(down_url['src'])

# ------------------------------------------------------------
# 내부 파일 저장 (1)
# ------------------------------------------------------------
import os

downloadDirectory = 'downloaded'
baseUrl = 'https://pythonscraping.com'

def getAbsoluteUrl(baseUrl, source):
    if source.startswith('http://www.'):
        url = 'http://{}'.format(source[11:])
    elif source.startswith("http://"):
        url = source
    elif source.startswith('www.'):
        url = 'http://{}'.format(source[4:])
    else:
        url = '{}'.format(source)
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace('www.', '')
    path = path.replace(baseUrl, '')
    path = downloadDirectory + path
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

# ------------------------------------------------------------
# 내부 파일 저장 (2)
# ------------------------------------------------------------
html = urlopen('https://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
downloadList = bs.find_all('img', src=True)

for download in downloadList:
    fileUrl = getAbsoluteUrl(baseUrl, download['src'])
    if fileUrl is not None:
        print(fileUrl)
        urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))

# ------------------------------------------------------------
# 데이터를 CSV파일로 저장
# ------------------------------------------------------------
# python에 기본 내장된 라이브러리 사용
import csv

csvFile = open('test.csv', 'w', encoding='UTF-8')

try:
    writer = csv.writer(csvFile)
    writer.writerow(('number', 'number+2', '(number+2)^2'))

    for i in range(10):
        writer.writerow((i, i+2, pow(i+2, 2)))

except Exception as e:
    print(e)
finally:
    csvFile.close()

# ------------------------------------------------------------
# 데이터를 CSV로 저장 예제 (1)
#  - 위키피디아에서 텍스트 에디터 비교 테이블 가져와 저장
# ------------------------------------------------------------
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html, 'html.parser')

table = bs.find_all('table', class_ = 'wikitable')[0]
rows = table.find_all('tr')

csvFile = open('editors.csv', 'wt', encoding='utf-8')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.find_all(['td', 'th']):
            csvRow.append(cell.get_text())

        writer.writerow(csvRow)
finally:
    csvFile.close()

# --> Version과 Date 항목의 저장 위치가 원본과 다름( colspan = 2 )

# ------------------------------------------------------------
# 웹페이지 테이블 크롤링하기
# ------------------------------------------------------------
# ------------------------------------------------------------
# 데이터를 CSV로 저장 예제 (1) *개선*
#  - colspan = 2로 설정된 부분 처리
# ------------------------------------------------------------
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parse
import pandas as pd

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html, 'html.parser')

table = bs.find_all('table', class_ = 'wikitable')[0]
rows = table.find_all('tr')

table_data = parse.make2d(table)    # 2차원 배열

# 데이터 프레임으로 저장
df = pd.DataFrame(table_data[2: ], columns=table_data[1])
print(df)

# csv 파일로 저장
csvFile = open('editor1.csv', 'w', encoding='utf-8')
writer = csv.writer(csvFile)

for row in table_data:
    writer.writerow(row)

csvFile.close()

# ------------------------------------------------------------
# 파이썬과 통합 : 예제 (1)
# - Kevin Bacon에 연결된 모든 링크 가져오기
# ------------------------------------------------------------
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import re

conn = pymysql.connect(host='localhost', user='root', passwd='0131', db='scraping', charset='utf8')

cur = conn.cursor()
random.seed(None)

# title, content 필드에 데이터 추가 함수
def store(title, content):
    cur.execute('INSERT INTO pages (title, content) VALUES ("%s", "%s")', (title, content))
    cur.connection.commit()

def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org' + articleUrl)
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('h1').get_text()
    content = bs.find('div', {'id':'mw-content-text'}).find('p').get_text()
    store(title, content)   # 데이터베이스에 저장
    return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()