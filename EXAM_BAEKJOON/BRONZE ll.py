# 1009번. 분산처리
# import sys
# n = int(sys.stdin.readline())

# result = []
# for i in range(n):
#     a, b = [int(x) for x in sys.stdin.readline().split()]
#     result.append(a**b%10)

# for i in result:
#     print(i)

# -----------------------------------------------------------
n = int(input())

result = []
for i in range(n):
    a, b = map(int, input().split())
    
    new_b = b % 4
    if new_b == 0: new_b = 4

    number = a ** new_b
    if number % 10 == 0:
        result.append(10)
    else:
        result.append(number % 10)

for i in result:
    print(i)

# 1075번. 나누기
n = []
for i in range(2):
    n.append(input())

a = int(n[0][:-2] + '00')

while True:
    if a % int(n[1]) == 0:
        break
    a += 1
print(str(a)[-2:])

# 1076번. 저항
color = {'black':'0', 'brown':'1', 'red':'2', 'orange':'3', 'yellow':'4', 'green':'5', 'blue':'6' ,'violet':'7', 'grey':'8', 'white':'9'}

l = []
for i in range(3):
    l.append(input())

print(int(color[l[0]] + color[l[1]]) * (10 ** int(color[l[2]])))

# 1100번. 하얀 칸
total = 0

for i in range(8):
    horse = list(input())
    
    if i % 2 == 0:
        

# 1152번. 단어의 개수
str = input().split()
print(len(str))