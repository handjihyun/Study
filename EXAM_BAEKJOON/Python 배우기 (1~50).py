# Q1. Hello World!를 출력하시오.
print("Hello World!")

# Q2. 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
a, b = map(int, input().split())
print(a + b)

# Q3. 두 정수 A와 B를 입력받은 다음, AXB를 출력하는 프로그램을 작성하시오.
a, b = map(int, input().split())
print(a * b)

# Q4. 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
a, b = map(int, input().split())
print(a - b)

# Q5. 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.
a, b = map(int, input().split())
print(a / b)

# Q6. 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를
# 출력하는 프로그램을 작성하시오. 
a, b = map(int, input().split())
print(a + b, a - b, a * b, a // b, a % b, sep='\n')

# Q7. 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를
# 출력하는 프로그램을 작성하시오.
a, b, c = map(int, input().split())
print((a + b) % c, ((a%c)+(b%c))%c, (a*b)%c, ((a%c)*(b%c))%c, sep='\n')

# Q8. 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
a = int(input())
b = int(input())
print(a + b)

# Q9. (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
#     (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에
#     들어갈 값을 구하는 프로그램을 작성하시오.
a = int(input())
b = input()

for i in range(len(b)-1, -1, -1):
    print(a*int(b[i]), end='\n')
print(a*int(b))

# Q10. 두 숫자 R1과 R2가 있을 때, 두 수의 평균 S는 (R1+R2)/2와 같다.
#       R1과 S는 기억하고 있다! 상근이를 도와 R2가 몇 인지 구하는 프로그램을 작성하시오.
R1, S = map(int, input().split())
print(2*S - R1)

# Q11. 정화는 N×M 크기의 초콜릿을 하나 가지고 있다.
#      초콜릿의 크기가 주어졌을 때,
#      이를 1×1 크기의 초콜릿으로 쪼개기 위한 최소 쪼개기 횟수를 구하는 프로그램을 작성하시오.
N, M = map(int, input().split())
print(N*M-1)

# Q12. 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
#      각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#      각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.
case = int(input())

i, nums = 0, []
while i < case:
    a, b = map(int, input().split())
    nums.append((a,b))
    i += 1

i = 0
while i < case:
    print(f"Case #{i+1}: {sum(nums[i])}")
    i += 1

# Q13. 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다.
#      x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.
case = int(input())

i, nums = 0, []
while i < case:
    a, b = map(int, input().split())
    nums.append((a,b))
    i += 1

i = 0
while i < case:
    print(f"Case #{i+1}: {nums[i][0]} + {nums[i][1]} = {sum(nums[i])}")
    i += 1

# Q14. 서울의 오늘 날짜를 출력하는 프로그램을 작성하시오.
#      서울의 오늘 날짜를 "YYYY-MM-DD" 형식으로 출력한다.
from datetime import date
print(date.today().isoformat())

# Q15. 자신이 백준 온라인 저지(BOJ)에서 맞은 문제의 수와 아이디를 그대로 출력하는 프로그램을 작성하시오.
#      첫 줄에 자신이 맞은 문제의 수, 둘째 줄에 아이디를 출력한다.


# Q16. 첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다.
# 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다.
# 첫째 줄에 종료되는 시각의 시와 분을 공백을 사이에 두고 출력한다.
# (단, 시는 0부터 23까지의 정수, 분은 0부터 59까지의 정수이다. 디지털 시계는 23시 59분에서 1분이 지나면 0시 0분이 된다.)
a, b = map(int, input().split())
c = int(input())

if b+c >= 60:
    n = int((b+c)/60)
    if a+n >= 24:
        print(a+n-24, b+c-60*n)
    else: print(a+n, b+c-60*n)
else:
    print(a, b+c)

# Q17. 첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23), 분 B (0 ≤ B ≤ 59)와 초 C (0 ≤ C ≤ 59)가 정수로
#      빈칸을 사이에 두고 순서대로 주어진다. 두 번째 줄에는 요리하는 데 필요한 시간 D (0 ≤ D ≤ 500,000)가 초 단위로 주어진다.
#      첫째 줄에 종료되는 시각의 시, 분, 초을 공백을 사이에 두고 출력한다.
#      (단, 시는 0부터 23까지의 정수이며, 분, 초는 0부터 59까지의 정수이다. 디지털 시계는 23시 59분 59초에서 1초가 지나면 0시 0분 0초가 된다.)
a, b, c = map(int, input().split())
d = int(input())

if c+d >= 60:
    n = int((c+d)/60)
    if b+n >= 60:
        n2 = int((b+n)/60)
        if a+n2 >= 24:
            print((a+n2)%24, b+n-60*n2, c+d-60*n)
        else: print(a+n2, b+n-60*n2, c+d-60*n)
    else: print(a, b+n, c+d-60*n)
else:
    print(a, b, c+d)

# Q18. 첫째 줄에 앨범에 수록된 곡의 개수 A와 평균값 I가 주어진다. (1 ≤ A, I ≤ 100)
#      첫째 줄에 적어도 몇 곡이 저작권이 있는 멜로디인지 출력한다.
a, b = map(int, input().split())
print(a*(b-1)+1)

# Q19. @는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자이다.
#      첫째 줄에 테스트 케이스의 개수 T가 주어진다. 다음 줄에는 화성 수학식이 한 줄에 하나씩 주어진다.
#      입력으로 주어지는 수는 정수이거나 소수 첫째 자리까지 주어지며,
#      0 이상 100 이하이다. 연산자는 최대 3개 주어진다.
#      각 테스트 케이스에 대해서, 화성 수학식의 결과를 계산한 다음에, 소수점 둘째 자리까지 출력한다.
n = int(input())

case = []
for i in range(n):
    case.append((input().split()))

l_total = []
for i in case:
    total = float(i[0])
    for j in i:
        if j == "@":
            total = total * 3
        elif j == '%':
            total += 5
        elif j == '#':
            total -= 7
    l_total.append(total)

for _ in l_total:
    print(f"{_:.2f}")

# Q20. 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
#      즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
s = int(input())

str = []
for i in range(s):
    str.append(input().split())

for _ in str:
    num = int(_[0])
    total = ''
    for k in _[1]:
        total += k*num
    print(total)

# Q21. 첫째 줄에 양의 정수 A가 주어진다. 둘째 줄에 연산자 + 또는 *가 주어진다.
# 셋째 줄에 양의 정수 B가 주어진다. A와 B는 모두 10의 제곱 형태이고, 길이는 최대 100자리이다.
nums = []

for i in range(3):
    nums.append(input())
    
for i in range(3):
    a, b = int(nums[0]), int(nums[-1])

if nums[1] == '*':
    print(a * b)
else:
    print(a + b)

# Q22.시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C,
#     60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
score = int(input())

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# Q.23 세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.
num = list(map(int, input().split()))
print(sorted(num)[1])

# Q.11653 소인수분해
N = int(input())
m = 2

while N != 1:
    if N % m == 0:
        print(m)
        N //= m
    else:
        m += 1
        
# Q.1789 수들의 합
S = int(input())

n = 1
while n * (n+1) / 2 <= S:
    n += 1
print(n-1)

# Q.2753 윤년
year = int(input())

if (year % 4 == 0) & (year % 100 != 0):
    print(1)
elif (year % 400 == 0):
    print(1)
else:
    print(0)

# Q.10039 평균 점수
score = []
for i in range(5):
    score.append(int(input()))

for i in range(len(score)):
    if score[i] < 40:
        score[i] = 40

print(int(sum(score)/len(score)))

total = 0
for i in range(5):
    score = int(input())

    if score < 40:
        score = 40
    
    total += score
print(total // 5)

# Q.1934 최소공배수
# 유클리드 호제법 : 두 수의 곱에서 두 수의 최대공약수를 나누면 최소공배수를 구할 수 있음
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    aa, bb = a, b

    while bb != 0:
        aa = aa % bb
        aa, bb = bb, aa

    print(a * b // aa)

# Q.2480 주사위 세개
a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif (a == b) | (a == c):
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    print(max(a, b, c) * 100)

# Q.4101 크냐?
while True:
    a, b = map(int, input().split())
    if a == b == 0: break

    if a > b:
        print('Yes')
    else:
        print('No')

# Q.10156 과자
k, n, m = map(int, input().split())

if k * n > m:
    print(k * n - m)
else:
    print(0)

# Q.3009 네 번째 점
l_a = []
l_b = []

for i in range(3):
    a, b = map(int, input().split())
    l_a.append(a)
    l_b.append(b)

for i in range(3):
    if l_a.count(l_a[i]) == 1:
        a = l_a[i]
    if l_b.count(l_b[i]) == 1:
        b = l_b[i]
print(a, b)

# Q.2476 주사위 게임
n = int(input())
max_dice = 0

for i in range(n):
    a, b, c = map(int, input().split())

    if a == b == c:
        dice = 10000 + a * 1000
    elif (a == b) | (a == c):
        dice = 1000 + a * 100
    elif b == c:
        dice = 1000 + b * 100
    else:
        dice = max(a, b, c) * 100

    if max_dice < dice:
        max_dice = dice
print(max_dice)

# Q.2754 학점계산
score = input()

if score[0] == 'A':
    if score == 'A+':
        print(4.3)
    elif score == 'A0':
        print(4.0)
    else:
        print(3.7)
elif score[0] == 'B':
    if score == 'B+':
        print(3.3)
    elif score == 'B0':
        print(3.0)
    else:
        print(2.7)
elif score[0] == 'C':
    if score == 'C+':
        print(2.3)
    elif score == 'C0':
        print(2.0)
    else:
        print(1.7)
elif score[0] == 'D':
    if score == 'D+':
        print(1.3)
    elif score == 'D0':
        print(1.0)
    else:
        print(0.7)
else:
    print(0.0)

# Q.2884 알람 시계
a, b = map(int, input().split())

if b - 45 < 0:
    if a == 0:
        print(23, 60-(45-b))
    else:
        print(a-1, 60-(45-b))
else:
    print(a, b-45)

#Q.7567 그릇
dish = input()

height = 10
for i in range(1, len(dish)):
    if dish[i-1] != dish[i]:
        height += 10
    else:
        height += 5
print(height)

# Q.5063 TGN
n = int(input())

for i in range(n):
    r, e, c = map(int, input().split())

    if r < e-c:
        print('advertise')
    elif r == e-c:
        print('does not matter')
    else:
        print('do not advertise')

# Q.10102 개표
n = int(input())
vote = input()

a, b = 0, 0
for i in vote:
    if i == 'A':
        a += 1
    else:
        b += 1

if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')

# Q.10886 0 = not cute / 1 = cute
n = int(input())

total = 0
for i in range(n):
    ans = int(input())

    if ans == 1:
        total += 1
    
if total >= (n//2+1):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")

# Q.10988 펠린드롬인지 확인하기
word = input()

if word == ''.join(reversed(word)):
    print(1)
else:
    print(0)

# Q.5086 배수와 약수
while True:
    a, b = map(int, input().split())
    if a == 0: break

    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')

# Q.5717 상근이의 친구들
while True:
    a, b = map(int, input().split())

    if a == 0: break

    print(a+b)

# Q.9610 사분면
n = int(input())
q1, q2, q3, q4, axis = [0] * 5

for i in range(n):
    a, b = map(int, input().split())
    if (a == 0) | (b == 0):
        axis += 1
    elif (a > 0) & (b > 0):
        q1 += 1
    elif (a < 0) & (b > 0):
        q2 += 1
    elif (a < 0) & (b < 0):
        q3 += 1
    else:
        q4 += 1
print(f'Q1: {q1}\nQ2: {q2}\nQ3: {q3}\nQ4: {q4}\nAXIS: {axis}')

# Q.8958 OX퀴즈
n = int(input())

for i in range(n):
    test = input()

    score, num = 0, 1

    for i in range(len(test)):
        if test[i] == 'O':
            score += num
            num += 1
        else:
            num = 1
    print(score)

# Q.9506 약수들의 합
while True:
    num = int(input())

    if num == -1: break

    num_l = []

    for i in range(1, num):
        if num % i == 0:
            num_l.append(i)
    
    if sum(num_l) == num:
        print(num, '=', ' + '.join(map(str, num_l)))
    else:
        print(num, 'is NOT perfect.')