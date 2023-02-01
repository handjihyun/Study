# Q1
msg = ['Good', 'child', 'Zoo', 'apple', 'Flower', 'zero']

def maxminstr(msg):
    msg = sorted(msg, reverse = True)
    print(f'정렬 결과 : {msg}\n가장 높은 문자열 : {max(msg)}, 가장 낮은 문자열 : {min(msg)}')
maxminstr(msg)

# Q2
data = "가나다"

def encoding(data):
    i, h, b = [], '', ''
    for n in data:
        i.append(ord(n))
    for j in i:
        h += hex(j)
        b += bin(j)
    print(f'"{data}"의 인코딩 : {h}\n"{data}의 인코딩 : {b}')
encoding(data)

print(" ord(가) : ",  ord("가"))
print(" oct(가) : ",  oct(ord("가")))
print(" bin(가) : ",  bin(ord("가")))
print(" hex(가) : ",  hex(ord("가")))

# Q3
data = '123,42,98,18'

def maxminNum(data):
    data = ''.join(data.split(','))
    num = []
    for i in data:
        num.append(int(i))
    print(f'"{data}"의 합 : {sum(num)}, 가장 큰 수 : {max(num)}, 가장 작은 수 : {min(num)}')
maxminNum(data)

# Q4
num = int(input("게임 정수 입력 : ").strip())

i = 1
while True:
    if (i % 10 == 2) | (i % 10 == 4) | (i % 10 == 8):
        print('#', end='')
        i += 1
    if i % 20 == 0:
        print(i, end='\n')
    else:
        print(i, end='')
    i += 1
    if i > num: break

# Q5
mon = input("좋아하는 월 입력 : ")

m_dict = {'1':'Jan Winter','2':'Feb Winter','3':'March Spring', '4':'April Spring', '5':'May Spring', '6':'June Summer', '7':'July Summer', '8':'Aug Summer', '9':'Sep Fall', '10':'Oct Fall', '11':'Nov Fall', '12':'Dec Winter'}
if mon in m_dict.keys():
    print(m_dict[mon])
else:
    print("존재하지 않는 월입니다.")

# Q6
num = input("숫자 입력 : 예) 123456, $")

def money(num):
    num = num.split(',')
    num[0] = format(int(num[0]), ',d')
    print(str(num[0]) + num[1].strip())
money(num)

# Q7
num = int(input("약수 구하고 싶은 수 : ").strip())

divi = []
for i in range(1, 10):
    if num % i == 0:
        divi.append(str(i))
print(f'{num}의 약수 : {", ".join(divi)}')

# Q8
msg = input("메시지 입력 : ")
msg = ''.join(msg.split(' '))
def num(msg):
    msg = ''.join(msg.split(' '))
    nums = set()
    for i in msg:
        if i.isnumeric():
            nums.add(str(i))
    print(', '.join(nums))
num(msg)

# Q9
birth = input("생년월일 입력 : ")

def age(birth):
    from datetime import datetime
    today = datetime.now().date()
    birth = datetime.strptime(birth, '%Y.%m.%d.')
    year = today.year - birth.year
    
    if today.month < birth.month:
        print(f'당신의 한국 나이는 {year+1}세입니다.\n당신의 외국 나이는 {year}세입니다.')
    elif (today.month == birth.month) & (today.day < birth.day):
        print(f'당신의 한국 나이는 {year+1}세입니다.\n당신의 외국 나이는 {year-1}세입니다.')
age(birth)

# Q10
num = int(input("팩토리얼 수 입력 : "))

i = 1
origin = num
fact = []
if num == 0:
    print('0! => 0')
else:
    while num:
        i *= num
        fact.append(str(num))
        num -= 1

        if num == 0: break
    print(f'{origin}! => {" * ".join(fact)} = {i}')

# Q11
num = int(input("범위 숫자 입력 : "))

prime = []
for i in range(1, num+1):
    for j in range(2, i+1):
        if i == j:
            prime.append(str(i))
        elif i % j == 0: break
print(f'1 ~ {num} 범위에서 소수 : {", ".join(prime)}')

# Q12
datas = {"이름":["베트맨","마징가","슈퍼맨","슈렉","피오나"], "국어":[90,82,77,94,78], "수학":[89,71,100,82,99],"윤리":[98,80,92,93,91],"국사":[99,91,90,71,83]}

keys = list(datas.keys())
for i in range(1, len(keys)):
    print(f"[{keys[i]}] 최고 점수 : {max(datas[keys[i]])}, 최저 점수 : {min(datas[keys[i]])}")

# Q13
nums = input("시작 구구단, 종료 구구단 입력 : ")
def calc(nums):
    nums = nums.split('-')
    a = int(nums[0].strip())
    b = int(nums[1].strip())

    print(f"--[{a}단]--\t--[{a+1}단]--\t--[{b}단]--")
    for j in range(1, 10):
        print(f"{a} * {j} = {a*j}\t{a+1} * {j} = {(a+1)*j}\t{b} * {j} = {b*j}")
calc(nums)

for dan in range(2, 10):
    print(f"---{dan}단---", end = '  ')
    for num in range(1, 10):
        print(f"{dan}*{num}={dan*num:02}", end = '\n')

# 2*1=2     3*1=3       4*1=4       5*1=5
# 2*2=4     3*2=6       4*2=8       5*2=10
# 단이 바뀌는 경우! (곱해지는 숫자는 고정)
for num in range(1, 10):
    # print(f"---{dan}단---", end = '  ')
    for dan in range(2, 10):
        print(f"{dan}*{num}={dan*num:0>2}", end = '\n' if dan==9 else ' ')

gugudan = [print(f"{dan}*{num}={dan*num:0>2}", end = '\n') if dan == 9 else print(f"{dan}*{num}={dan*num:0>2}", end = '  ') for num in range(1, 10) for dan in range(2, 10)]

# Q14
num = input("숫자 입력 : ")

print(f"숫자 : {num}\n만의 자리 : {num[0]}\n천의 자리 : {num[1]}\n백의 자리 : {num[2]}\n십의 자리 : {num[3]}\n일의 자리 : {num[4]}")

# Q15
def addData(*data):
    if len(data) > 0:
        total = '' if isinstance(data[0], str) else 0
    else:
        total = None
    for i in data:
        total += i
    print(total)

addData()
addData(1, 3, 5)
addData(True, True, False, False, True)
addData('A')
addData('A','BC','Good')

# 정수, 실수형 데이터를 모두 더하는 함수만들기
# 방법1)
def addData(*nums):
    total = 0
    for num in nums:
        total += num
    return total if len(nums) > 0  else None

print( addData() )
print( addData(True, True, False) )
print( addData(-1, 1, 0) )

# 방법2)
def addData(*nums):
    total = 0
    for num in nums:
        total += num

    if len(nums)>0:
        return total

# Q16
for i in range(1, 16, 2):
    print(' '*((15-i) // 2) + "*"*i)
print(" "*6 + "*"*4)
print(" "*6 + "*"*4)
print("Merry Christmas")
print(" "* 6 + "2023")

# Q17
msg2 = 'Merry Christmas HaPPy New YEaR'
result = [print(i.upper(), end='') if i.islower() else print(i.lower(), end='') for i in msg2]

# Q18
nums = input("숫자 2개 입력 (3, 4) : ")
def calc(nums):
    nums = nums.split(',')
    a = int(nums[0])
    b = int(nums[1])
    
    print(f"덧셈 결과 : {a+b}")
    print(f"뺄셈 결과 : {a-b}")
    print(f"곱셈 결과 : {a*b}")
    
    if b == 0:
        print(f"나누기 결과 : 0")
        print(f"몫 결과 : 0")
        print(f"나머지 결과 : 0")
    else:
        print(f"나누기 결과 : {a / b}")
        print(f"몫 결과 : {a // b}")
        print(f"나머지 결과 : {a % b}")        
calc(nums)

# Q19
def Info(**datas):
    for k, v in datas.items():
        print(f"{k:7} ==> {v}")
Info(age=12, phone='010-2222-1111', job='학생', loc='대구')

# Q20
def mycalc():
    while True:
        print(f'{"-"*30}\n<나의계산기>\n{"-"*30}')
        print(f'1.입  력  2.덧  셈  3.뺄 셈')
        print(f'4.곱  셈  5.나눗셈  6.종 료')
        print("-"*30)
    
        menu = input("메뉴 선택(1~6): ").strip()
        if menu == '1':
            nums = input("숫자 2개 입력 :(예:1, 7) ").split(',')
            a = int(nums[0])
            b = int(nums[1])
        elif menu == '2':
            print(a+b)
        elif menu == '3':
            print(a-b)    
        elif menu == '4':
            print(a*b)
        elif menu == '5':
            print(a/b)
        elif menu == '6':
            print('나의계산기 프로그램을 종료합니다.')
            break
mycalc()