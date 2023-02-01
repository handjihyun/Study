import pandas as pd

# 시리즈(Series) 데이터 =============================================
# pandas.Series(데이터)
# Attributes :  index, values, ndim, shape, ...
# ==================================================================
# Series 객체 속성 출력 함수
# printSeries
def printSeries(srObj, srObjName):
    print(f"{srObjName} =====>\n{srObj}")
    print('-----------------------')
    print(srObj.index)
    print(srObj.values)
    print(srObj.ndim)
    print(srObj.shape)
    print(srObj.dtype)

# __name__ : magic value, 시스템에 값을 설정
# 해당 파이썬 파일이 실행 중 여부 확인
# 실행 중 ==> __main__
# import될 경우 ==> 파일명

print(f"'__name__ : {__name__}")
if __name__ == '__name__':
    

    # 1) data => list data
    sr = pd.Series([10, 20, 30])
    print(sr)

    # 시리즈 객체의 속성 확인 => 변수명, 속성명
    printSeries(sr, 'sr')

    # 2) data => Dictionary data
    sr2 = pd.Series({'name':'Hong', 'age':12, 'loc':'Daegu'})

    printSeries(sr2, 'sr2')

    # 3) data => Tuple data
    sr3 = pd.Series((11, 22))

    printSeries(sr3, 'sr3')