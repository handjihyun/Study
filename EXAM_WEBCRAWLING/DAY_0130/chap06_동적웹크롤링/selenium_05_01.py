# --------------------------------------------
# Selenium 사용 (5)
# - 동적 웹페이지 크롤링 예제
# --------------------------------------------
# 커피빈 코리아 홈페이지 자동 실행
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('C:/workspace/chromedriver.exe')
driver.get('https://www.coffeebeankorea.com/store/store.asp')

driver.execute_script('storePop2(1)')

html = driver.page_source   # 해당 웹페이지의 소스가 저장됨
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())

# ----------------------------------------------------------------
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('C:/workspace/chromedriver.exe')
driver.get('https://www.coffeebeankorea.com/store/store.asp')

driver.execute_script('storePop2(1)')

# 현재의 html 소스를 저장
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

store_names = soup.select('div.store_txt > p.name > span')
store_names_list = []
for name in store_names:
    store_names_list.append(name.get_text())

print('매장 개수: ', len(store_names_list))
print(store_names_list)

store_addresses = soup.select('p.address > span')
store_addresses_list = []

for addr in store_addresses:
    print(addr.get_text())
    store_addresses_list.append(addr)