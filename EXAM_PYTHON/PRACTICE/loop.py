# 1) 1500에서 2700사이의 숫자 중에서 7로 나누어 떨어지고, 5의 배수인 모든 숫자를 출력하라.
for i in range(1500, 2701):
    if (i % 7 == 0) & (i % 5 == 0):
        print(i, end=" ")

# 2) 킬로미터를 미터로, 미터를 킬로미터로 변환하는 프로그램을 작성하라.
# 예를 들어 1500m을 입력하면, 1.5km을 출력하고, 2.3km을 입력하면 2300m를 출력하게 하라.
# (이 예제는 list 단원을 공부하면 더욱 쉽게 해결할 수 있다.)

# 3) 다음 패턴을 출력하는 프로그램을 작성하라.
# @

# @ @

# @ @ @

# @ @ @ @

# @ @ @ @ @

# @ @ @ @

# @ @ @

# @ @

# @
for i in range(6):
    print(f"{'@ '*i}")
for i in range(4, 0, -1):
    print(f"{'@ '*i}")

# 4) 입력받은 숫자의 약수를 모두 출력하는 프로그램을 만들어라.
num = input("숫자를 입력하세요 : ")
for i in range(1, 10):
    if int(num) % i == 0: print(i, end=' ')

# 5) 1부터 100까지 숫자 중 약수의 개수가 5개인 숫자를 모두 찾는 프로그램을 작성하라.
nums = []
for i in range(1, 101):
    for j in range(1, 10):
        if i % j == 0:
            nums.append(j)

# 6) 자신을 제외한 모든 약수들의 총합이 자기 자신이 되는 수를 완전수라고 한다.
# 1이상 1000이하의 모든 완전수를 출력하는 프로그램을 작성하라.
# 예: 6의 약수는 1,2,3,6이며 1+2+3=6이므로 완전수이다.
nums = []
i = 1
while i < 1001:
    for j in range(1, 10):
        if (i % j == 0) & (i = sum(j)):

# 7) 메르센 수(Mersenne number)는 2의 거듭제곱에서 1이 모자란 숫자를 가리킨다.
# 즉 2**n - 1의 형태로 나타난다.
# 3 = 2**2 - 1이므로 메르센 수이다.
# 1부터 1000까지의 숫자 중 메르센 숫자를 모두 찾는 프로그램을 작성하라.
for i in range(1001):
    if 2**i - 1 == i:
        print(i)