# ----------------------------------------------------------
# 데이터 분석 => 기초 통계함수들, 고유값, 결측치
# ----------------------------------------------------------
import pandas as pd

FILE = r"datafiles\dataFiles\auto-mpg.csv"

# 데이터 정보 확인 함수 --------------------------------------
def printDataInfo(df):
    df.info()
    print(df.head(), df.tail(), sep='\n', end='\n\n')
    print(df.describe(), end='\n')
    print(f"Index => {df.index}\nColumns => {df.columns}", end='\n\n')

# (1) FILE => DataFrame 읽기
df = pd.read_csv(FILE, header=None)

# (2) 데이터 확인
printDataInfo(df)

# (3) 컬럼명 추가
# mpg
# cylinders
# displacement
# horsepower
# weight
# acceleration
# model year
# origin
# car name
df.columns = ["mpg", "cylinders", "displacement", "horsepower", "weight", "accel", "model_year", "origin","car_name"]
print(df.head())

# (4) 실제 데이터와 타입 맞지 않는 데이터 처리
# horsepower => 데이터 값 중에 '?'
# (4-1) 해당 컬럼에 데이터 종류 확인 => 고유값 unique()
horseUnique = df.horsepower.unique()
print("horseUnique : ", horseUnique)

# (4-2) 해당 컬럼의 데이터 종류별 갯수 확인 => value_count()
horseValueCounts = df.horsepower.value_counts()
print("horseValueCounts : ", horseValueCounts, type(horseValueCounts))
print(horseValueCounts["?"])

# print(df.horsepower.dtype)
# df.astype({"horsepower":"float"})