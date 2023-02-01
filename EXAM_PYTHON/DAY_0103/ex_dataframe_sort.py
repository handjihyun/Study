# -------------------------------------------------------------------------------------------
# 정렬(Sort) 다루기
# - 인덱스 기준 정렬 => 오름차순(작은 숫자 >>> 큰 숫자), 내림차순(큰 숫자 >>> 작은 숫자)
# - 데이터 기준 정렬 => 오름차순(작은 숫자 >>> 큰 숫자), 내림차순(큰 숫자 >>> 작은 숫자)
# -------------------------------------------------------------------------------------------
#모듈 / 패키지 로딩 --------------------------------------------------------------------------
import pandas as pd

# DF 생성 ----------------------------------------------------------------------------------
df1 = pd.DataFrame({'name':["마징가", "베트맨", "원더우먼"],'kor':[87, 91, 69], 'eng':[99, 73, 89], 'sci':[71, 95, 62]})

print(df1, end="\n\n")

# [1] 인덱스 기준 정렬 => 내림차순 ------------------------------------------------------------
# 행 기준, 내림차순 - ascending = False
desDF = df1.sort_index(ascending=False)
print(desDF.index, desDF, sep="\n", end='\n\n')

# 열 기준, 내림차순
coldesDF = df1.sort_index(axis = 1, ascending=False)
print(coldesDF.index, coldesDF, sep="\n", end='\n\n')

coldesDF = df1.sort_index(axis = 1, ascending=True)
print(coldesDF.index, coldesDF, sep="\n", end='\n\n')

# [2] 데이터 즉 값 기준 정렬 => 내림차순 -------------------------------------------------------
# DataFrame.sort_values()
df2 = df1.sort_values(by=["name"], ascending=False)
print(df2, end='\n\n')

df2 = df1.sort_values(by=["kor", 'eng'], ascending=False)
print(df2, end='\n\n')

# 특정 컬럼에 값 넣기 -------------------------------------------------------------------------
print("-"*50)
print(df2['name'], df2.name, sep="\n")

df2["name"]  = ['B-Man', 'Mazinga', 'Woman']
print(df2['name'], df2.name, type(df2.name), sep="\n")

print(df2.name[1], type(df2.name[1]), df2.name[1].lower())
#                  --> str type