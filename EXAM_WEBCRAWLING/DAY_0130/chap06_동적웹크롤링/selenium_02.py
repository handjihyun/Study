# --------------------------------------------
# Selenium 사용 (2)
# - element 접근 예제
# --------------------------------------------
from selenium import webdriver

driver = webdriver.Chrome('C:/workspace/chromedriver.exe')

driver.get('http://www.pythonscraping.com/pages/warandpeace.html')
driver.implicitly_wait(5)

# 하나의 클래스 이름 검색
name = driver.find_element_by_class_name('green')
print(name.text)

print('-' * 20)

# 해당 클래스 이름을 모두 검색
nameList = driver.find_elements_by_class_name('green')
for name in nameList:
    print(name.text)

driver.quit()