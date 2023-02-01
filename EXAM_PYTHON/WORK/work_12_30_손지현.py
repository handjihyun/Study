# [문자열 변환 문제]----------------------------------------------------
# 1. 자동차 번호가 아래와 같을 때 뒤에 4자리만 출력하세요.
car_number = '12가 1234'
print(car_number[-4:])

# 2. ‘홀짝홀짝홀짝’ 문자열에서 ‘홀’만 출력하세요.
str = '홀짝홀짝홀짝'
print(str[::2])

# 3. ‘010-1111-2222’ 휴대폰 번호에서 ‘-’를 공백으로 변경해 주세요.
print('010-1111-2222'.replace("-", " "))

# 4. ‘hello’ 문자열에서 ‘Hello’로 출력해 주세요.
str = 'hello'
print(str.replace("h", "H"))

# 5. 파일명 ‘sensor.xlsx’에서 확장자만 출력해주세요.
# 그리고 ‘data.txt’ 파일명에서 확장자가 ‘xlsx’인지 검사하여 결과를 출력해 주세요.
file = 'sensor.xlsx'
print(file[-4:])

file1 = 'data.txt'
if file1[-4:] == 'xlsx': print("O")
else: print("X")

# 6. 아래 내용처럼 출력이 되도록 str을 연산자를 사용하여 구현하세요.
# ==================================================

# 2022 HAPPY YEAR

# ==================================================
print(f"{'='*30}\n\n2022 HAPPY YEAR\n\n{'='*30}")

# 7. 금액 “ 5,969,782,550 ” 에서 ‘,’를 제거하고 공백도 제거해 주세요.
bill = "5,969,782,550"
print(bill.replace(",", "").strip())

# 8. 아래 내용처럼 화면에 출력하세요.
#      *
#     ***
#    *****
#   *******
#  *********
#   *******
#    *****
#     ***
#      *
for i in range(1, 10, 2):
    print(" " * ((9-i)//2) + '*' * i)
for i in range(7, 0, -2):
    print(" " * ((9-i)//2) + '*' * i)

# 9. “에어컨이 월 48,584원에 무이자 36개월” 이라는 문자열에서 에어컨의 가격을
# 계산 후 출력해 주세요.
str = '에어컨이 월 48,584원에 무이자 36개월'
money = int(str[6:13].replace(",", ""))
month = int(str[-4:-2])

print(f"{money}원\n{month}개월\n{money*month}원")

# 10. 메시지를 입력 받은 후 변환 후 결과 출력하세요.
msg = input("메시지를 입력하세요 : ")

# - 모두 대문자로 변환 - 모두 소문자로 변환
print(f"대문자 : {msg.upper()}\n소문자 : {msg.lower()}")

# - 문자를 구성하는 요소가 문자안에 몇 개가 존재하는지 개수 출력
# (예: Hello ->H : 1 e : 1 l : 2 o :1 )
smsg = list(set(msg))
for i in range(len(smsg)):
    print(f"{msg} -> {smsg[i]} : {msg.count(smsg[i])}")

# - 문자 요소별로 대문자는 소문자로, 소문자는 대문자로 변환 출력
# (예: HeLLo => hEllO )
for i in msg:
    if i.isupper(): print(i.lower(), end='')
    else: print(i.upper(), end='')


# [List, Tuple 문제]----------------------------------------------------
# 1. 영화 순위 정보에서 영화 제목을 movieList 리스트에 저장하세요.
movieList = ['닥터 스트레인지', ' 스플릿', ' 럭키']

# 2. movieList에 새로운 영화 제목을 추가하세요.
movieList.append("아바타")
print(movieList)

# 3. movieList에서 제일 마지막에 입력된 영화제목을 리스트에 꺼내서 없애주세요.
movieList.remove(movieList[-1])
print(movieList)

# 4. 7과목 점수 저장한 jumsuList를 생성후 합계, 평균, 최대값, 최소값을 출력하세요.
jumsiList = [1, 2, 3, 4, 5, 6, 7]
print(f"합계 : {sum(jumsiList)}\n평균 : {sum(jumsiList)/len(jumsiList)}\n최대값 : {max(jumsiList)}\n최소값 : {min(jumsiList)}")

# 5. price=[‘20220322’, 100, 130, 140, 150, 170, 160] 리스트에서 날짜정보 제외한
# 나머지 데이터만 출력해주세요.
price = ["20220322", 100, 130, 140, 150, 170, 160]

price_1 = []
for i in price:
    if isinstance(i, int):
        price_1.append(i)
print(price_1)

# 6. 다음 리스트 nums=[9, 12, 49, 3, 2, 1, -1, 71, 8] 정렬해주세요
# - 오름차순 정렬 - 내림자순 정렬
nums=[9, 12, 49, 3, 2, 1, -1, 71, 8]
print(f"오름차순 : {sorted(nums)}\n내림차순 : {sorted(nums, reverse=True)}")

# 7. 1~1000 사이의 3의 배수를 요소로 갖는 리스트를 생성하세요.
numList = []
for i in range(1, 1001, 3):
    numList.append(i)
print(numList)

# 8. tmp=(‘apple’, ‘banana’, ‘cake’, ‘kiwi’)를 언패킹 후 출력해 주세요.
tmp = ('apple', 'banana', 'cake', 'kiwi')
for i in tmp:
    print(i, end="\t")

# 9. 숫자 1이 저장된 튜플을 생성해 주세요.
tp = (1,)
print(type(tp))

# 10. 개인정보 이름, 주민번호, 전화번호를 저장해주세요.
info = ['손지현', '123456-1234567', '010-1111-2222']

# 11. 3학생의 이름, 국어, 영어, 미술, 체육 점수를 저장하는 리스트를 생성한 후
# 학생별 합계, 평균을 출력해 주세요.
name = ['son', 'hong', 'lee']
kor = [90, 20, 10]
eng = [20, 30, 45]
art = [25, 36, 57]
ath = [26, 39, 30]


for i in range(3):
    print(f"{name[i]} 합계 : {kor[i] + eng[i] + art[i] + ath[i]}")
    print(f"{name[i]} 평균 : {(kor[i] + eng[i] + art[i] + ath[i]) / 4}")


# [ Dict ∙ Set ∙ If 문제 ]----------------------------------------------
# 1. 개인정보(이름, 휴대폰, 이메일, 직업, 키, 몸무게)를 딕셔너리로 구성해 주세요.
info = {'이름':'홍길동', '휴대폰':'010-2222-1111', '이메일':'a@naver.com', '직업':'학생', '키':160, '몸무게':50}
print(info)

# 2. 다음 아이스크림 데이터를 딕셔너리로 구성하세요..
# 이름 | 희망 가격
# ---------------------
# 메로나 | 1000
# 폴라포 | 1200
# 빵빠레 | 1800
icecream = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
print(icecream)

# 3. 아이스크림 딕셔너리에 월드콘, 1500을 추가해 주세요.
icecream['월드콘'] = 1500
print(icecream)

# 4. 개인정보 딕셔너리에서 Key만 따로, Value만 따로, Key-Value 묶음 형태로 따로 분리해 주세요.
print(f"key : {info.keys()}\n value : {info.values()}\n key-Value : {info.items()}")

# 5. 과일데이터를 미리 준비한 후 사용자에게 좋아하는 과일이름을 입력 받고
# 해당 과일이 존재할 경우 영어로 출력하고 없는 경우도 적당한 메시지 출력
# 하세요.
fruit = {'사과':'apple', '바나나':'banana'}
ask = input('좋아하는 과일 : ').strip()
lkeys = list(fruit.keys())

if ask in lkeys:
    print(fruit[ask])
else: print("입력한 과일이 존재하지 않습니다.")

# 6. 세 정수 A, B, C를 입력 받고 이때, 두 번째로 큰 정수를 출력하세요.
nums = input("세 정수를 입력하세요 : ").strip()

nums = nums.split(",")
n = []
for i in nums:
    n.append(int(i))
print(f"두 번째로 큰 정수 : {sorted(n)[1]}")

# 7. 사용자로부터 달러, 엔, 유로, 위안 금액을 입력받은 후 이를 원으로 변환하세요.
# ------------------
# 통화명 | 환율
# ------------------
# 달러 | 1167
# 엔 | 1.096
# 유로 | 1268
# 위안 | 171

money = input("달러, 엔, 유로, 위안 입력: ").strip()
money = money.split(",")
m = []

for i in money:
    m.append(int(i))
print(f'{"="*15}\n\n통화명 | 환율\n\n{"="*15}\n\n달러 | {m[0]*1254.06}\n엔 | {m[1]*9.51}\n유로 | {m[2]*1339.27}\n위안 | {m[3]*181.60}\n\n{"="*15}')

# 8. 사용자로부터 입력받은 데이터가 숫자인지, 소문자인지, 대문자인지 식별하여
# 출력해 주세요.
data = input("데이터를 입력하세요 : ").strip()

if data[0].isdecimal():
    print("숫자입니다.")
elif data[0].islower():
    print("소문자입니다.")
elif data[0].isupper():
    print("대문자입니다.")

# 9. 사용자로부터 입력받은 데이터 타입을 출력하세요.
# (예 : 12 => int 타입, True => bool 타입 )
data = input("데이터를 입력하세요 : ").strip()

if ('.' not in data) & (data[0].isdecimal()): print("int 타입")
elif ('.' in data) & (data[0].isdecimal()): print("float 타입")
elif (data == 'True') | (data == 'False'): print("bool 타입")
else: print("str 타입")

# 10. 3의 배수와 5의 배수로 구성된 리스트를 생성해주세요. 단, 중복은 허용하지
# 않습니다.
n35 = set()
for i in range(1, 51):
    if (i % 3 == 0) | (i % 5 == 0):
        n35.add(i)
print(list(n35))

# 11. 사용자로부터 정수를 입력 받은 후 입력여부 및 정수 여부를 체크하도록
# 코드 작성하세요.
num = input("정수를 입력하세요 : ").strip()

if len(num) > 0:
    if num[0].isdecimal(): print("PASS")
    else: print("정수를 입력하세요!")
else: print("입력한 정수가 없습니다.")


# [ Dict와 제어문과 함수 문제 ]------------------------------------------
# 1. icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}에서
# 아래 문제를 해결하세요.
icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

# 1-1. icecream['누가바']에서 오류가 발생하는 이유를 설명해 주세요.
#   -> 딕셔너리 icecream의 key에는 '누가바'가 존재하지 않기 때문이다.

# 1-2. 키(Key)만 출력해주세요.
print(icecream.keys())

# 1-3. 가장 큰 값, 가장 작은 값을 출력해 주세요.
val = list(icecream.values())

print(f"가장 큰 값 : {max(val)}, 가장 작은 값 : {min(val)}")

# 1-4. 키와 값을 쌍으로 묶어서 출력해 주세요.
print(icecream.items())

# 2. 다음 아이스크림 데이터에 대한 부분 문제를 해결하세요.
# 이름 | 가격 | 재고
# -------------------------------------------------
# 메로나 | 300 | 20
# 비비빅 | 400 | 3
# 죠스바 | 250 | 100

# 2-1. 딕셔러니 타입으로 데이터를 저장하세요.
icecream = {'메로나':[300, 20], '비비빅':[400, 3], '죠스바':[250, 100]}

# 2-2. 저장된 딕셔너리 데이터에서 비비빅의 가격을 출력해주세요.
print(icecream['비비빅'])

# 2-3. 저장된 딕셔너리 데이터에서 재고를 기준으로 오름차순 정렬해 주세요.
a = []
for i in icecream:
    a.append(icecream[i][1])
print(sorted(a))

# 3. 사용자로부터 숫자를 입력 받은 후 아래 문제를 해결해 주세요.
num = input("숫자를 입력하세요 : ")

# 3-1. 입력 받은 숫자가 짝수인지 홀수 인지 판별하는 코드 작성하세요.
if int(num) % 2 == 0: print("even")
else: print("odd")

# 3-2. 입력 받은 숫자 만큼 숫자를 곱셈하는 코드를 작성하세요.
# (예 – 입력 숫자 3, 3 * 3 * 3 = 27)
nlist = list(num * int(num))

total = 1
for i in range(len(nlist)):
    total *= int(nlist[i])
if len(nlist) > 2:
    print(f"{(num + ' * ') * (len(nlist)-1)}{num} = {total}")
elif len(nlist) == 2: 
    print(f'{(num + " * ")}{num} = {total}')
elif len(nlist) == 1:
    print(num)

# 3-3. 입력 받은 숫자가 양수, 0, 음수인지 판별 코드를 조건부 표현식으로 작성하세요.
num = input("숫자를 입력하세요 : ")
if int(num) > 0:
    print('양수')
elif int(num) == 0:
    print("0")
else: print("음수")

# 4. 빙고 프로그램을 만들어 주세요.
# 단계 1) 임의의 숫자 설정
# 단계 2) 지정된 범위에서 숫자 입력 받기
# 단계 3) 입력 받은 숫자 값이 임의의 정해 둔 숫자와 동일할 때까지 질문하여 찾기
nums = []
for i in range(1, 10):
    nums.append(i)

print(nums)