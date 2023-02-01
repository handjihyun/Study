# ---------------------------------------------------------------------
# 1. 계산기 프로그램을 클래스기반으로 만들어 주십시오. (정수, 실수)
class calc:
    def __init__(self, *num):
        self.num = num

    def add(self):
        return sum(self.num)

    def sub(self):
        self.num1 = self.num[0]
        for i in range(1, len(self.num)):
            self.num1 -= self.num[i]
        return self.num1
    
    def mul(self):
        self.num1 = self.num[0]
        for i in range(1, len(self.num)):
            self.num1 *= self.num[i]
        return self.num1

    def divi(self):
        self.num1 = self.num[0]
        for i in range(1, len(self.num)):
            if self.num[i] != 0:
                self.num1 = self.num1 / self.num[i]
            else: 
                self.num1 = None
                break
        return self.num1


myCalc = calc(5, 0, -1)
print(myCalc.add())
print(myCalc.sub())
print(myCalc.mul())
print(myCalc.divi())

# ---------------------------------------------------------------------
# 2. 함수 구현
#   1) 구구단 2 ~ 9단 출력 반복문 1개
dan = 2
num = 0

while dan < 10:
    if num == 0:
        print(f"  --{dan}단--  ", end = '  ' if dan != 9 else '\n')
        num += 1 if dan == 9 else 0
        if dan == 9:
            dan = 2
        else:
            dan += 1
    elif dan == 9:
        print(f"{dan} * {num} = {dan*num:02}", end='\n')
        num += 1
        dan = 2
    elif dan < 9:
        print(f"{dan} * {num} = {dan*num:02}", end='   ')
        dan += 1
    if num > 9: break

for n in range(0, 81):
    num, dan = (n//9)+1, (n%9)+2
    if num != 10 and dan != 10:
        print(f'{dan:^3}*{num:^3} = {dan*num:^3}', end="\n" if dan == 9 else "   " ) 

#   2) 리스트 컨프리헨션
[print(f"--{dan}단--", end = '\t') for dan in range(2, 10)]
[print(f"{i}*{j}={i*j:02}", end = '\t') if i != 9 else print(f"{i}*{j}={i*j:02}", end = '\n') for j in range(1, 10) for i in range(2, 10)]

#   3) 별자리, 띠
jumin = '221010-3345678'

def Info(jumin):
    year, month, day, gender = jumin[0:2], jumin[2:4], jumin[4:6], jumin[7]
    zodiac = ['원숭이', '닭', '개', '돼지', '쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양']
    star = {120:'물병자리', 219:'물고기자리', 321:'양자리', 420:'황소자리', 521:'쌍둥이자리', 622:'게자리', 723:'사자자리', 823:'처녀자리', 924:'천칭자리', 1023:'전갈자리', 1123:'궁수자리', 1225:'염소자리'}
    l_star = list(star.keys())
    
    if (gender == '1') | (gender == '2'):
        year = '19' + year
        i = int(year) % 12
        j_zodiac = zodiac[i]
    else:
        year = '20' + year
        i = int(year) % 12
        j_zodiac = zodiac[i]

    if l_star[0] <= int(month+day) < l_star[1]:
        j_star = star[l_star[0]]
    elif l_star[1] <= int(month+day) < l_star[2]:
        j_star = star[l_star[1]]
    elif l_star[2] <= int(month+day) < l_star[3]:
        j_star = star[l_star[2]]
    elif l_star[3] <= int(month+day) < l_star[4]:
        j_star = star[l_star[3]]
    elif l_star[4] <= int(month+day) < l_star[5]:
        j_star = star[l_star[4]]
    elif l_star[5] <= int(month+day) < l_star[6]:
        j_star = star[l_star[5]]
    elif l_star[6] <= int(month+day) < l_star[7]:
        j_star = star[l_star[6]]
    elif l_star[7] <= int(month+day) < l_star[8]:
        j_star = star[l_star[7]]
    elif l_star[8] <= int(month+day) < l_star[9]:
        j_star = star[l_star[8]]
    elif l_star[9] <= int(month+day) < l_star[10]:
        j_star = star[l_star[9]]
    elif l_star[10] <= int(month+day) < l_star[11]:
        j_star = star[l_star[10]]
    else:
        j_star = star[l_star[11]]

    print(f"{j_zodiac}띠 {j_star}")

Info(jumin)