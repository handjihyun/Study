# ---------------------------------------------------
# 연산 실습
# ---------------------------------------------------
# 모듈 로딩 ------------------------------------------
import pandas as pd

FILE = "datafiles/dataFiles/stock price.xlsx"
# df = pd.read_excel(FILE)

# # 데이터 확인 => info(), head(), tail(), describe()
# df.info()
# print(df.head(), df.tail(), sep='\n', end='\n\n')
# print(df.describe(), end='\n\n')

# # [1] 주식ID, 이름, 가격만 사용하도록 데이터 추출
# n_df = df[["id", "stock_name", "price"]]
# print(n_df.head(), n_df.tail(), sep='\n', end='\n\n')

# # [2] 가격에 대한 * 100 결과를 추가
# n_df['n_price'] = n_df.price * 100
# # n_df['n_price'] = n_df.price.mul(100, fill_value=0)
# print(n_df.head(), end='\n\n')

# =====================================================
# id 컬럼을 인덱스 설정
# 데이터 파일을 읽어 올 때 설정 => 매개변수(파라미터) index_col
# print("="*50)
# print(df.index, n_df.index, sep='\n')

# 특정 컬럼 인덱스로 설정 => index_col 매개변수
# 로딩할 특정 컬럼 지정 => usecols=''
# stockDF = pd.read_excel(FILE, usecols="B, D")
stockDF = pd.read_excel(FILE, skiprows=3, header=None)
#                               -> 3번째 행이 첫번째로 나온다
#                                           -> header가 없으면 3번째 행이 인덱스로 설정된다
print(stockDF.index, stockDF.columns, sep='\n', end='\n\n')
print(stockDF)

# parse_dates 매개변수 => 컬럼 지정하면 해당 컬럼의 타입이 datetime64로 변경
# dayfirst 매개변수 : 일.월 순서로 설정
# inter_datetime_format 매개변수 : 날짜시간 포맷을 추정해서 파싱
# date_parser 매개변수 : 직접 날짜시간 포맷 설정 function
from datetime import datetime # 날짜 시간 관련 모듈

print("="*50)
FILE2 = "datafiles/dataFiles/banklist.csv"
_date_parser = lambda x : datetime.strptime(x, '%d-%b-%y')
# bankDF = pd.read_csv(FILE2, parse_dates=["Updated Date"], dayfirst=True, infer_datetime_format=True)
bankDF = pd.read_csv(FILE2, parse_dates=["Closing Date", "Updated Date"], date_parser=_date_parser)
bankDF.info()
print(bankDF.head())