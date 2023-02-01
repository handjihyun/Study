# --------------------------------------------------------------------------------------
# 1. 알파벳 빈도수 계산 및 그래프 출력 (딕셔너리 활용)
# - 제공된 loremipsum.txt 파일을 읽어서, 각 알파벳 소문자, 대문자의 빈도수를 따로 계산하
#   고 그 결과를 그래프로 출력하시오. (다른 파일도 읽어서 분석이 가능해야 됨)
# - 숫자, 공백, 마침표 등 다른 문자들은 계산하지 않음
# - isalpha(), isdigit(), isspace()등 활용
# - str.islower(): 문자열이 소문자이면 True
# - str.isupper(): 문자열이 대문자이면 True
# - 빈도수가 0인 알파벳은 출력하지 않음
# - 알파벳 소문자, 대문자 빈도수를 각각 계산해서 아래의 그래프 출력
# - 출력은 빈도수가 제일 높은 문자부터 화면 출력함 (내림차순 정렬)
# --------------------------------------------------------------------------------------

def check():
    d = input("Input file name: ").strip()
    file = "WORK/" + d
    f = open(file, "r", encoding='utf-8')
    sentence = f.read().rstrip()

    upper = {}
    lower = {}

    for s in sentence:
        if s.isalpha():
            if (s.isupper()) and (s not in upper.keys()):
                upper[s] = 1
            elif (s.isupper()) and (s in upper.keys()):
                upper[s] += 1
            elif (s.islower()) and (s not in lower.keys()):
                lower[s] = 1
            elif (s.islower()) and (s in lower.keys()):
                lower[s] += 1
        else:
            pass

    f.close()

    upper = dict(sorted(upper.items(), key=lambda x: x[1], reverse=True))
#        생성자 dict()                 -> 정렬 기준   value
    print(f"대문자:\n{upper}")

    lower = dict(sorted(lower.items(), key=lambda x: x[1], reverse=True))
    print(f"소문자:\n{lower}")

    import numpy as np
    import matplotlib.pyplot as plt

    import matplotlib
    matplotlib.rcParams['font.family'] ='Malgun Gothic'
    matplotlib.rcParams['axes.unicode_minus'] =False

    plt.figure(figsize=(11,6))
    plt.suptitle(f"알파벳 카운트 : {d.strip('.txt')}")

    plt.subplot(1,2,1)
    plt.bar(upper.keys(), upper.values())
    plt.title("대문자 개수")
    plt.xlabel("Alphabet")
    plt.ylabel("Count")

    plt.subplot(1,2,2)
    plt.bar(lower.keys(), lower.values())
    plt.title("소문자 개수")
    plt.xlabel("Alphabet")
    plt.ylabel("Count")

    plt.savefig(f"{d.strip('.txt')}_count.png")
    plt.show()
    
    print(f"{d.strip('.txt')}_count.png is saved.")

check()