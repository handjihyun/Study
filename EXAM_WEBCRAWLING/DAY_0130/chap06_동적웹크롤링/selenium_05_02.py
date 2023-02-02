# --------------------------------------------
# Selenium 사용 (5)
# - 동적 웹페이지 크롤링 예제
# - # 커피빈 코리아 홈페이지
# --------------------------------------------
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time

def coffeebean_store(store_list):
    coffeebean_url = 'https://www.coffeebeankorea.com/store/store.asp'
    driver = webdriver.Chrome('C:/workspace/chromedriver.exe')

    for i in range(1, 380):
        driver.get(coffeebean_url)
        time.sleep(1)   # 웹페이지를 연결한 동안 1초 대기

        driver.execute_script('storePop2(%d)' %i)
        time.sleep(1)

        try:
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            store_name = soup.select_one('div.store_txt > h2').text
            store_info = soup.select('div.store_txt > table.store_table > tbody > tr > td')
            store_address_list = list(store_info[2])
            store_addr = store_address_list[0]
            store_phone = store_info[3].text
            print('{} {} {}'.format(store_name, store_addr, store_phone))
            store_list.append([store_name, store_addr, store_phone])
        except:
            continue

def main():
    store_info = []
    coffeebean_store(store_info)

    # 데이터프레임으로 변경
    coffeebean_table = pd.DataFrame(store_info, columns = ('매장이름', '주소', '전화번호'))
    print(coffeebean_table.head())

    # 데이터프레임을 csv파일로 저장
    coffeebean_table.to_csv('coffeebean_branches.csv', encoding='utf-8', mode='w', index=True)

main()