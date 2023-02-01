# ------------------------------------------------------
# DataFrame & Series 다루기 => 삭제
# ------------------------------------------------------
# 모듈 로딩 ---------------------------------------------
import pandas as pd

# DF 객체 생성 ------------------------------------------
df1 = pd.DataFrame({'name':["마징가", "베트맨", "원더우먼"],'kor':[87, 91, 69], 'eng':[99, 73, 89], 'sci':[71, 95, 62]})

# DF 데이터 확인하기
print(f"df1 ===================> \n{df1}")
print(f"df1.index => \n{df1.index}")
print(f"df1.columns => \n{df1.columns}")

# 행(row, 가로 데이터) 삭제 => drop() 메서드 =============
# '베트맨'이 있는 가로 라인 데이터 삭제
# - inplace = False : 원본 데이터 적용 여부
#             결과 DataFrame 반환
# - inpalce = True  : 원본 데이터 적용
#             None 반환
retDF = df1.drop(1)
print(f"retDF ===================> \n{retDF}")
print(f"df1 ===================> \n{df1}")

# retDF에서 2번 인덱스 행(row) 삭제 및 원본 적용
ret = retDF.drop(2, inplace=True)
print(f"ret ===================> \n{ret}")  # 복사본에 적용X --> None 반환
print(f"retDF ===================> \n{retDF}")

# 열(column, 세로 데이터) 삭제 => drop(axis=1) 메서드 =====
# 행 방향 지정 => axis = 1 또는 axis = 'columns'
# sci 컬럼 삭제
colDF = df1.drop('sci', axis=1)
print(f"colDF ===================> \n{colDF}")
print(f"df1 ===================> \n{df1}")


# ------------------------------------------------------
# DataFrame & Series 다루기 => 추가
# ------------------------------------------------------
# 행(row, 가로) 데이터 추가 ------------------------------
# 변수명.loc['행 이름/인덱스] = "값"
# 데이터 => 이름, 국어, 영어, 과학

df1.loc[10] = ["홍길동", 99, 87, 91]
print(f"df1 ===================> \n{df1}")
print(f"df1.index \n{df1.index}")

# 열(col, 가로) 데이터 추가 ------------------------------
# 변수명["열 이름 / 인덱스"] = 값
df1["math"] = [45,56,89,24]
print(f"df1 ===================> \n{df1}")
print(f"df1.columns \n{df1.columns}")

df1["math2"] = [100]
print(f"df1 ===================> \n{df1}")
print(f"df1.columns \n{df1.columns}")