import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

coffee = {'매장이름' : [], '위치(시,구)' : [], '주소' : [], '전화번호' : []}

for i in range(1, 54):
    html = urlopen(f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store=')
    soup = BeautifulSoup(html, 'html.parser')

    for j in soup.select('tbody > tr'):
        data = j.text.split("\n")

        coffee['매장이름'].append(data[3])
        coffee['위치(시,구)'].append(data[2])
        coffee['주소'].append(data[5])
        coffee['전화번호'].append(data[-2])

hollys_table = pd.DataFrame(coffee, columns=('매장이름', '위치(시,구)', '주소', '전화번호'))

for i in range(len(hollys_table)):
    print(f"[{i+1:3d}]: 매장이름: {hollys_table.iloc[i][0]}, 지역: {hollys_table.iloc[i][1]}, 주소: {hollys_table.iloc[i][2]}, 전화번호: {hollys_table.iloc[i][3]}")

hollys_table.to_csv("hollys_branches.csv", index=False)