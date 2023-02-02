# --------------------------------------------
# Selenium 사용 (1)
# --------------------------------------------
from selenium import webdriver

driver = webdriver.Chrome('C:/workspace/chromedriver.exe')

driver.get('https://www.google.com')

print(driver.current_url)
print(driver.title)
print(driver.page_source)   # HTML 소스 가져오기

driver.implicitly_wait(time_to_wait=5)
driver.close()  # 하나의 탭만 종료
driver.quit()   # webdriver 전체 종료