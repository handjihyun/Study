# -------------------------------------------------------
# 과제3 : 네이버 증시 정보 크롤링
# 시가 총액 10위까지의 기업 정보를 크롤링
# -------------------------------------------------------
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_market_sum.naver'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

while True:

    print(f'{"-"*38}\n{"[ 네이버 코스피 상위 10대 기업 목록 ]"}\n{"-"*38}')
    for i in range(10):
        print(f'[{i+1:2}] {soup.find_all("a", class_ ="tltle")[i].text}')

    company = int(input("주가를 검색할 기업의 번호를 입력하세요(-1: 종료): "))

    if company == -1: break
    else:
        path = 'https://finance.naver.com'
        new = requests.get(path + soup.find_all('a', class_ ='tltle')[company-1].attrs['href'])
        n_soup = BeautifulSoup(new.text, 'html.parser')

        print(path + soup.find_all('a', class_ ='tltle')[company-1].attrs['href'])
        print(f"종목명: {n_soup.select('h2 > a')[0].text}")
        print(f"종목코드: {n_soup.select('div.description > span.code')[0].text}")
        print("현재가", n_soup.select_one('p.no_today').text.strip().split('\n')[0])
        print(f"전일가: {n_soup.select('td > em > span.blind')[0].text}")
        print(f"시가: {n_soup.select('td > em > span.blind')[4].text}")
        print(f"고가: {n_soup.select('td > em > span.blind')[1].text}")
        print(f"저가: {n_soup.select('td > em > span.blind')[5].text}")