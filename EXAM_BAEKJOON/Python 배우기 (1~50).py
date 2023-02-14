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