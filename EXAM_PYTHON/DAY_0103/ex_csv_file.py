# -------------------------------------------------------------------------
# CSV FILE ==> DataFrame 객체로 저장
# - pandas.read_csv(경로 파일명)
# -------------------------------------------------------------------------
import pandas as pd

FILE = "datafiles/dataFiles/banklist.csv"

# DF 객체 생성 ------------------------------------------------------------
bankDF = pd.read_csv(FILE)
print(f'bankDF ===> \n{bankDF}')

# DF 데이터 확인용 메서드 --------------------------------------------------
# [1] 전체 요약 정보 제공 메서드 => info() 메서드
bankDF.info()

# [2] 앞부분 5줄(기본값) 실제데이터 보기 => head(n) 메서드
#     끝부분 5줄(기본값) 실제데이터 보기 => tail(n) 메서드
print(bankDF.head(5), bankDF.tail(3), sep="\n\n")

# [3] 데이터의 기술통계를 적용한 결과 제공 => 데이터 분포 확인 ==> describe() 메서드
#   수치 데이터 가능 (기본값)
#   모든 데이터 가능 (include = True)
print(bankDF.describe())
print(bankDF.describe(include="all"))

# 데이터 가지고 놀아보기 ===================================================
print((f'bankDF.columns => {bankDF.columns}'))

# (1) 4개 columns => 'Bank Name', 'City', 'Closing Date', 'Updated Date'
df_new = bankDF[['Bank Name', 'City', 'Closing Date', 'Updated Date']]
print(df_new.info())
print(df_new.head(3))

# (2) 컬럼 중에서 인덱스로 설정 => set_index([])
df_new.set_index(["Bank Name", "City"], inplace=True)
print(df_new.index, df_new.columns, sep='\n', end='\n\n')
print(df_new.head(3))

# (3) Updated Date 기준으로 가장 최근날짜부터 보여주세요.
# 가장 최근 날짜 => 내림차순 ( ascending = False )
# object str --------> datetime

# import datetime
# df_new['Updated Date'] = pd.to_datetime(df_new['Updated Date'], format="%d-%b-%y")

df_new.sort_values(by = ["Updated Date"], key=lambda col: pd.to_datetime(col), ascending=False, inplace=True)
print(df_new["Updated Date"].values)