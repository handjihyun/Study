# --------------------------------------------------------------------
# Q1085. 직사각형에서 탈출
# 한수는 지금 (x, y)에 있다.
# 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0),
# 오른쪽 위 꼭짓점은 (w, h)에 있다.
# 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.
# --------------------------------------------------------------------
x, y, w, h = map(int, input().split())

print(min(abs(w - x), abs(h - y), x, y))

# --------------------------------------------------------------------
# Q1247. 부호
# N개의 정수가 주어지면, 이 정수들의 합 S의 부호를 구하는 프로그램을 작성하시오.
# 총 3개의 테스트 셋이 주어진다. 각 테스트 셋의 첫째 줄에는 N(1 ≤ N ≤ 100,000)이 주어지고,
# 둘째 줄부터 N개의 줄에 걸쳐 각 정수가 주어진다.
# 주어지는 정수의 절댓값은 9223372036854775807보다 작거나 같다.
# --------------------------------------------------------------------
nums = []

for i in range(3):
    N = int(input())

    j = 0
    while j < N:
        nums.append(int(input()))
        j += 1

l_sum = [sum(nums[0:3]), sum(nums[3:13]), sum(nums[13:])]

for i in l_sum:
    if i == 0: print('0')
    elif i < 0 : print('-')
    else: print('+')

from sys import stdin

for i in range(3):
    N = int(stdin.readline())
    nums = [int(stdin.readline()) for i in range(N)]

    if sum(nums) == 0:
        print("0")
    elif sum(nums) > 0:
        print('+')
    else:
        print('-')

# --------------------------------------------------------------------
# Q.1267 핸드폰 요금
# 영식 요금제는 30초마다 10원씩 청구된다. 민식 요금제는 60초마다 15원씩 청구된다.
# 동호가 저번 달에 이용한 통화의 개수 N이 주어진다. N은 20보다 작거나 같은 자연수이다.
# 둘째 줄에 통화 시간 N개가 주어진다. 통화 시간은 10,000보다 작거나 같은 자연수이다.
# --------------------------------------------------------------------
N = int(input())
time = list(map(int, input().split()))

y, m = 0, 0

for i in time:
    y += i // 30 * 10 + 10
    m += i // 60 * 15 + 15

if y < m:
    print('Y', y)
elif y > m:
    print('M', m)
else:
    print('Y', 'M', y)
# --------------------------------------------------------------------
# Q.1284 집 주소
# 각 숫자 사이에는 1cm의 여백이 들어가야한다.
# 1은 2cm의 너비를 차지해야한다. 0은 4cm의 너비를 차지해야한다. 나머지 숫자는 모두 3cm의 너비를 차지한다.
# 호수판의 경계와 숫자 사이에는 1cm의 여백이 들어가야한다.
# --------------------------------------------------------------------
addr = []

while True:
    num = input()
    addr.append(num)
    if num == "0": break

for i in addr[:-1]:
    total = 2 + len(i) -1
    
    for j in i: 
        if int(j) == 1:
            total += 2
        elif int(j) == 0:
            total += 4
        else:
            total += 3
    print(total)

# --------------------------------------------------------------------
# Q.1547 공
N = int(input())

ball = 1
for i in range(N):
    a, b = map(int, input().split())

    if a == ball:
        ball = b
        continue

    if b == ball:
        ball = a
        continue

print(ball)

# Q.1598 꼬리를 무는 숫자 나열
a, b = map(int, input().split())

a, b = a - 1, b - 1
print(abs(b // 4-a // 4) + abs(b % 4-a % 4))

# Q.1703 생장점
l_leaf = []

while True:
    leaf = input().split()
    if leaf[0] == '0': break
    else:
        l_leaf.append(leaf)

for i in l_leaf:
    total = 1
    for j in range(1, len(i)):
        if j % 2 != 0:
            total *= int(i[j])
        else:
            total -= int(i[j])
    print(total)