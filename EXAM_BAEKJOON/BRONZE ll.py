# 1009번. 분산처리
import sys
n = int(sys.stdin.readline())

result = []
for i in range(n):
    a, b = [int(x) for x in sys.stdin.readline().split()]
    result.append(a**b%10)

for i in result:
    print(i)