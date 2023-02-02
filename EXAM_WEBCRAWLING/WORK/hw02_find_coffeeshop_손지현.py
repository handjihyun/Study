import pandas as pd
df = pd.read_csv("D:\EXAM_WEBCRAWLING\hollys_branches.csv")
# print(df)

while True:
    city = input("검색할 매장의 도시를 입력하세요: ")
    if city == 'quit':
        print("종료 합니다.")
        break
    else:
        print(f'{"-"*25}\n검색된 매장 수: {len(df.loc[df["위치(시,구)"].str.contains(city)])}\n{"-"*25}')
        for i in range(len(df.loc[df["위치(시,구)"].str.contains(city)])):
            print(f'[{i+1:3d}]: {list(df.loc[df["위치(시,구)"].str.contains(city)].iloc[i][2:])}')
