# --------------------------------------------
# Selenium 사용 (3)
# - 텍스트 입력(구글) : send_keys()
# - 구글 검색어 입력 예제
# --------------------------------------------
from selenium import webdriver

driver = webdriver.Chrome('C:/workspace/chromedriver.exe')
driver.get('https://www.google.com')

driver.implicitly_wait(3)

search_box = driver.find_element_by_name('q')
search_box.send_keys('data')
search_box.submit()     # 검색어 전달