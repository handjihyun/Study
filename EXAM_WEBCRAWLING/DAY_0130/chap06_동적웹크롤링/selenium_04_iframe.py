# --------------------------------------------
# Selenium 사용 (4)
# - 프레임 이동
# --------------------------------------------
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('C:/workspace/chromedriver.exe')
driver.get('https://blog.naver.com/swf1004/221631056531')

driver.switch_to.frame('mainFrame')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

whole_border = soup.find('div', {'id' : 'whole-border'})
results = whole_border.find_all('div', class_ = 'se-module')

result1 = []
for result in results:
    print(result.text.replace('\n', ''))
    result1.append(result.text)

driver.quit()