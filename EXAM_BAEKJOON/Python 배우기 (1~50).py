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
for i in range(len(b)):
    print(a*int(b[i]), end='\n')