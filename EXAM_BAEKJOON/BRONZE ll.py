# 1009번. 분산처리
import sys
n = int(sys.stdin.readline())

result = []
for i in range(n):
    a, b = [int(x) for x in sys.stdin.readline().split()]
    result.append(a**b%10)

for i in result:
    print(i)

# -----------------------------------------------------------
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    
    new_b = b % 4       # 모든 제곱은 4번의 순환을 가진다.
    if new_b == 0:
        new_b == 4
    
    number = a ** new_b
    if number % 10 == 0:
        print(10)
    else:
        print(number % 10)

# 1075번. 나누기
n = []
for i in range(2):
    n.append(int(input()))

result = []
while True:
    if n[0][-2:] % n[1] == 0:
        print(n[0])
        print(str(n[0])[-2:])
        break
    else:
        n[0] += 1

# 1076번. 저항
color = {'black':'0', 'brown':'1', 'red':'2', 'orange':'3', 'yellow':'4', 'green':'5', 'blue':'6' ,'violet':'7', 'grey':'8', 'white':'9'}

l = []
for i in range(3):
    l.append(input())

print(int(color[l[0]] + color[l[1]]) * (10 ** int(color[l[2]])))
