# Module Loading ------------------------------------------------------
import pandas as pd                 # data analysis package
# import DAY_0102.ex_pandas as mp     # My Module

# -----------------------------------------------------------------------------------------
# Series 객체의 요소 다루기 => Use index
# [사용법] 객체변수명 [ 인덱스 ]
# -----------------------------------------------------------------------------------------
data = list(range(5, 31, 5))
sr1 = pd.Series(data)

# 요소 1개 읽기 => 변수명[인덱스] -----------------------------------------------------------
print(f"sr1[0] => {sr1[0]}")
print(f"sr1[5] => {sr1[5]}, {type(sr1[5])}")

for idx in range(len(sr1)):
    print(f"sr1[{idx}] => {sr1[idx]} : {type(sr1[idx])}")

for idx in sr1.index:       # .index 속성 사용!★
    print(f'idx => {idx}')
    print(f"sr1[{idx}] => {sr1[idx]} : {type(sr1[idx])}")

# 요소 여러개 읽기 => 변수명[[인덱스1, 인덱스2]] ---------------------------------------------
# ==> 결과 데이터 시리즈(Series) 타입
print(f'sr1[[0,4]] => \n{sr1[[0, 4]]}\n{type(sr1[[0, 4]])}')    # series type
print(f'sr1[[4]] => \n{sr1[[4]]}\n{type(sr1[[4]])}')            # series type


# 요소 범위지정하여 읽기 => 변수명[ star : end+1 ]
print(f"sr1[0: ] => \n {sr1[0:]}\n{type(sr1[0:])}")
print(f"sr1[0: :2] => \n {sr1[0::2]}\n{type(sr1[0::2])}")       # 짝수번째 요소 추출