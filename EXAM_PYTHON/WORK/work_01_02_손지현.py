import pandas as pd
import random as rd

# 1. Series 데이터를 생성 후 정보를 출력해주세요.
# (1)
# - 데이터 : 1 ~ 100 사이 임의의 숫자 30개 구성
data = pd.Series([rd.randrange(1, 101) for i in range(30)])
print(data)

# (2)
# - 데이터 : 1 ~ 100 사이 임의의 숫자 30개 구성
# - 조건 : 중복된 숫자 없음

data2 = []
while True:
    if len(data2) == 30: break
    num = rd.randint(1, 100)
    if num not in data2:
        data2.append(num)
print(pd.Series(data2))

data = set()
while True:
    if len(data) == 30: break
    num = rd.randrange(1, 101)
    if num not in data: data.add(num)
print(pd.Series(list(data)))

# (3)
# 데이터 : 0.0 ~ 1.0 사이 실수 데이터 10개로 구성
data3 = pd.Series([round(rd.random(), 2) for i in range(10)])
print(data3)