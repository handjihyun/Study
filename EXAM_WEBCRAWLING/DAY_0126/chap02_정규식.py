# ------------------------------------------------------------
# 데이터 크롤링과 정제
# - HTML 분석 및 정규식
# ------------------------------------------------------------

# ------------------------------------------------------------
# CSS 속성을 이용한 검색
# - 등장 인물 검색
# ------------------------------------------------------------
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, 'html.parser')

# 등장인물의 이름 : 녹색
nameList = soup.find_all('span', {'class':'green'})
for name in nameList:
    print(name.get_text())  # -> 줄 바꿈 문자 포함 (\n)

# ------------------------------------------------------------
# 특정 단어 찾기
# - find_all(text='검색어')
# ------------------------------------------------------------
princeList = soup.find_all(text = 'the prince')
print(princeList)
print('the prince count: ', len(princeList))

# ------------------------------------------------------------
# 트리 이동
# : 자식과 자손 (children)
# ------------------------------------------------------------
html = urlopen("https://www.pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html, 'html.parser')

table_tag = soup.find('table', {'id':'giftList'})
print('children 개수: ', len(table_tag))

for child in table_tag.children:
    print(child)
    print('-'*30)

# ------------------------------------------------------------
# 트리 이동
# : 자손 ( descendants )
# ------------------------------------------------------------
desc = soup.find('table', {'id':'giftList'}).descendants
print('descendants 개수: ', len(list(desc)))
print(desc)

for child in soup.find('table', {'id':'giftList'}):
    print(child)
    print('-'*30)

# ------------------------------------------------------------
# 트리 이동
# : 형제 다루기
# ------------------------------------------------------------
# 1) next_siblings
for sibling in soup.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)
    print('-'*30)

# 2) previous_siblings
for sibling in soup.find('tr', {'id':'gift2'}).previous_siblings:
    print(sibling)
    print('-'*30)

# 문자열 마지막에 whitespace('\n', '\r'등)가 있는 경우
sibling1 = soup.find('tr', {'id':'gift3'}).next_sibling
print(ord(sibling1))    # 문자의 Unicode 정수를 리턴
sibling1                # 공백 출력

# next_sibling.next_sibling 이용
sibling2 = soup.find('tr', {'id':'gift3'}).next_sibling.next_sibling
print(sibling2)

# ------------------------------------------------------------
# 정규 표현식 객체 사용
# : 정규식 객체를 생성 : compile(pattern)
# ------------------------------------------------------------
import re

# compile 사용 X
# - 매번 패턴 입력
m = re.match('[a-z]+', 'Python')
print(m)
print(re.search('apple', 'I like apple!'))

# compile 사용
# - 객체 p 생성 : 알파벳 소문자 패턴, 여러 번 사용
p = re.compile('[a-z]+')
m = p.match('python')
print(m)
print(p.search('I like apple 123'))

# ------------------------------------------------------------
# 정규표현식과 BeautifulSoup
# ------------------------------------------------------------
# - 제품 이미지 검색
# : <img src="  "> 태그의 속성 ['src'] 사용
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

img_tag = re.compile('/img/gifts/img.*.jpg')
images = soup.find_all('img', {'src':img_tag})

for image in images:
    print(image, end="-> ['scr'] 속성: ")
    print(image['src'])

# 대소문자 구분없이 특정 단어 검색
# '[T|t]{1}he prince'
# - T 또는 t가 1회
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')

princeList = bs.find_all(text='the prince')
print('the prince count: ', len(princeList))

prince_list = bs.find_all(text=re.compile('[T|t]{1}he prince'))
print('T|the prince count:', len(prince_list))