# --------------------------------------------------------------------------
# Index / Index Label(Name)
# - Index : 판다스 시스템에 지정하는 RangeIndex 정수형 (0-base)
# - Index Label(Name) : 시리즈 객체 생성시 지정하는 인덱스
# --------------------------------------------------------------------------
import pandas as pd

# Series 객체 생성 ---------------------------------------------------------
# 데이터 :  1 ~ 20 사이의 3의 배수
# 인덱스 : 문자 'a' ~ 'f'
# --------------------------------------------------------------------------
data = list(range(3, 20, 3))
idx = ['a', 'b', 'c', 'd', 'e', 'f']
idx2 = [11, 22, 33, 44, 55, 66]

mySr = pd.Series(data, index=idx2, name="Jumsu", dtype="float32")
print(mySr)

# # 요소 1개 읽기 => 변수명[인덱스]
# print(mySr['a'], mySr[0])   # 정수형 인덱스가 사라지는 것은 아님
print(mySr[11], mySr[0])      # 정수형 인덱스를 지정했을 경우 기존의 정수형 인덱스는 사라짐

# for idx in mySr.index: print(mySr[idx])

# # 요소 여러개 읽기 => 변수명[[인덱스1, 인덱스2, ...]]
# print(mySr[['a', 'd', 'f']], mySr[[0, 3, 5]])
# print(mySr[mySr.index[0::2]])

# # 범위지정 요소 읽기 => 변수명[ start : end+1 ]
# # 인덱스가 문자열인 경우 [start index : end index]  # 마지막 인덱스엔 +1 하지 않음
# print(mySr['a':'d'], mySr[0:3])