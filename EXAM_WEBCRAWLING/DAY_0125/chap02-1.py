# ---------------------------------------------------------
# BeautifulSoup Library
# ---------------------------------------------------------

# ---------------------------------------------------------
# 1. 샘플 HTML 구성
# ---------------------------------------------------------
html_example = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library Examples!</span>
    <div id="link">
        <a class="external_link" href="www.google.com">google</a>
        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="external_link" href="www.naver.com">naver</a>
            
            <p id="second">class1's second paragraph</p>
            <a class="internal_link" href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>
</body>
</html>
'''

# ---------------------------------------------------------
# 2. BeautifulSoup 기초
#   - 태그를 사용하여 요소에 직접 접근하기
# ---------------------------------------------------------
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, 'html.parser')

# <title> 태그에 접근
print(soup.title)
print(soup.title.text)
print(soup.title.get_text())

# <title> 태그를 포함하고 있는 부모(<head> 태그 출력)
print(soup.title.parent)

# <body> 태그에 접근
print(soup.body)
print(soup.body.text)

# <h1> 태그 접근
print(soup.h1)
print(soup.h1.text)

# <a> 태그 접근
print(soup.a)
print(soup.a.text)          # 태그 내부의 텍스트 추출
print(soup.a['href'])       # href 속성의 url 추출
print(soup.a.get('href'))   # a['href']와 동일

# ---------------------------------------------------------
# 2. BeautifulSoup 기초
#   - find() 함수
#     : 해당 조건에 맞는 맨 처음 검색 결과 추출
# ---------------------------------------------------------
print(soup.find('div'))

# 여러 <div> 태그 중 특정 속성을 가지는 항목 추출
print(soup.find('div', {'id':'text_id2'}))

# 추출된 요소에서 텍스트만 추출
div_text = soup.find('div', {'id':'text_id2'})
print(div_text.text)

# ---------------------------------------------------------
# find() 함수 활용
# ---------------------------------------------------------
# <a> 태그 및 <a> 태그의 href 속성 추출
# href_link = soup.find('a', {'class':'internal_link'})
href_link = soup.find('a', class_ = 'internal_link')

print(href_link)                # class='internal_link'인 태그 전체 추출
print(href_link['href'])
print(href_link.get('href'))
print(href_link.text)           # <a> 태그 내부 text 추출

# <a> 태그 내부의 모든 속성(attr) 가져오기
print('href_link.attrs: ', href_link.attrs)

# <a> 태그 내부의 모든 속성(attr)의 값 가져오기
print('values():', href_link.attrs.values())

values = list(href_link.attrs.values())
print('values[0]: {0}, values[1]: {1}'.format(values[0], values[1]))

# class 속성
print('class 속성값: ', href_link['class'])

# class 속성 예제
tr='''
<table>
<tr class="passed a b c" id="row1 example"><td>t1</td></tr>
<tr class="failed" id="row2"><td>t2</td></tr>
</table>
'''

table = BeautifulSoup(tr, 'html.parser')
for row in table.find_all('tr'):
    print(row.attrs)

# href 속성의 값이 'www.google.com'인 항목 검색
href_value = soup.find(attrs={'href': 'www.google.com'})

print(href_value)
print(href_value['href'])
print(href_value.text)

# span 태그의 속성 가져오기
span_tag = soup.find('span')

print('span_tag:', span_tag)
print('attrs:', span_tag.attrs)
print('value:', span_tag.attrs['class'])
print('text:', span_tag.text)

# ---------------------------------------------------------
# find_all() 함수
# ---------------------------------------------------------
# 모든 div 태그 검색
div_tags = soup.find_all('div')

print('div_tags length: ', len(div_tags))

for div in div_tags:
    print('-----------------------------------------------------')
    print(div)

# 모든 <a> 태그 검색 및 속성 보기
links = soup.find_all('a')

for alink in links:
    print(alink)
    print('url:{0}, text:{1}'.format(alink['href'], alink.get_text()))
    print()

# ---------------------------------------------------------
# find_all() 함수
# - 특정 태그 중 여러 속성값을 한 번에 검색
# ---------------------------------------------------------
link_tag = soup.find_all('a', {'class' : ['external_link', 'internal_link']})
print(link_tag)

# <p> 태그의 id값이 'first', 'third'인 항목 검색
p_tags = soup.find_all('p', {'id':['first', 'third']})

for p in p_tags:
    print(p)

# ---------------------------------------------------------
# select_one() 함수
# ---------------------------------------------------------
# <head> 태그 검색
head = soup.select_one('head')
print(head)
print(head.text)
print(head.text.strip())

# 첫 번째 <h1> 태그 검색
h1 = soup.select_one('h1')
print(h1)

# <h1> 태그의 id 검색 : #id
footer = soup.select_one('h1#footer')
print(footer)

# 클래스 이름 검색 : 태그.클래스이름
class_link = soup.select_one('a.internal_link')
print(class_link)
print(class_link.text)
print(class_link['href'])

# 계층적 하위 태그 접근 1
link1 = soup.select_one('div#link > a.external_link')
print(link1)

# 계층적 하위 태그 접근 2
link2 = soup.select_one('div#class1 p#second')
print(link2)
print(link2.text)

# ---------------------------------------------------------
# select() 함수
# ---------------------------------------------------------
# 모든 <h1> 태그 검색
h1_all = soup.select('h1')
print(h1_all)

# 모든 url 링크 검색
url_links = soup.select('a')

for link in url_links:
    print(link['href'])

# <div id=“class1”> 내부의 모든 url 검색
div_urls = soup.select('div#class1 > a')

# <div>태그와 <a>태그는 자손관계이기 때문에 부등호가 없어도 됨
# div_urls = soup.select('div#class1 a')
print(div_urls)
print(div_urls[0]['href'])

# 여러 항목 검색하기
# <h1>태그의 id가 ”heading”과 “footer”를 모두 검색
h1 = soup.select('#heading, #footer')
print(h1)

# <a>태그의 class이름이 “external_link”와 ”internal_link” 모두 검색
url_links = soup.select('a.external_link, a.internal_link')
print(url_links)