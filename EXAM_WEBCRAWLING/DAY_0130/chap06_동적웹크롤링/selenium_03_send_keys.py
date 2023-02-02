# --------------------------------------------
# Selenium 사용 (3)
# - 텍스트 입력 : send_keys()
# --------------------------------------------
from selenium import webdriver

driver = webdriver.Chrome('C:/workspace/chromedriver.exe')
driver.get('https://nid.naver.com/nidlogin.login')

driver.implicitly_wait(3)

# id, 비밀번호 전달
# <input>의 이름이 id를 검색
driver.find_element_by_id('id').send_keys('bileair')
driver.find_element_by_id('pw').send_keys('zzeon4697@')

driver.find_element_by_xpath("//*[@id='log.login']").click()