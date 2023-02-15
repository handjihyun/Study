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