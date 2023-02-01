# 1) 정수인 변수가 주어졌을 때, 홀수(odd)인지 짝수(even)인지 판별하는 프로그램을 작성하라.
num = 3
if num % 2 == 0: print("even")
else: print("odd")

# 2) 월(month)이 대입된 정수인 변수가 주어졌을 때, 해당 월이 며칠인지 출력하는 프로그램을 작성하라.
date = 1225
print(str(date)[-2:])

# 3) x, y, z의 세 개의 변수가 있다.
#   이 세 변수를 검사하여 가장 큰 홀수를 프린트하라.
#   만약 세 변수가 모두 홀수가 아니라면, 홀수가 없다는 메시지를 출력하라.
x, y, z = 9, 5, 5

value = [x, y, z]
check = []

if (x % 2 == 0) & (y % 2 == 0) & (z % 2 == 0):
    print("홀수 없음")
else:
    for i in value:
        if i % 2 != 0:
            check.append(i)
    print(max(check))

# 4) 삼각형 세 변의 길이가 변수로 주어졌을 때, 정삼각형(Equilateral triangle), 이등변삼각형(Isosceles triangle), 일반삼각형(triangle)을 구분하는 프로그램을 작성하라.
tri = [6, 6, 6]
if tri[0] == tri[1] == tri[2]:
    print("정삼각형(Equilateral triangle)")
elif (tri[0] == tri[1]) | (tri[0] == tri[2]) | (tri[1] == tri[2]):
    print("이등변삼각형(Isosceles triangle)")
else:
    print("일반삼각형(triangle)")

# 5) 삼각형 세 변의 길이가 변수로 주어졌을 때, 직각 삼각형인지 아닌지 판단하는 프로그램을 작성하라.
tri = [3, 4, 5]
if (tri[0]**2 + tri[1]**2 == tri[2]**2) | (tri[0]**2 + tri[2]**2 == tri[1]**2) |(tri[1]**2 + tri[2]**2 == tri[0]**2):
    print("직각삼각형")
else:
    print("직각삼각형이 아니다.")

# 6) 두 자리 정수가 대입된 변수를 검사하여, 십의 자리 숫자와 일의 자리 숫자의 합이 10이 넘는지 판단하는 프로그램을 작성하라.
num = 36
def check(num):
    nums = []
    for i in str(num):
        nums.append(int(i))
    if sum(nums) > 10:
        print("10이 넘는다.")
    else:
        print("10이 넘지 않는다.")
check(num)