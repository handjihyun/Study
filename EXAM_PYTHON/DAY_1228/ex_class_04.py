# -----------------------------------------------------------------
# 연락처 프로그램을 구현하고자 합니다.
# -----------------------------------------------------------------
# - 기  능 : 연락처 저장 / 삭제 / 수정
# - 데이터 : 이름, 전화번호, 사진, 별명, 직장, 그룹, 이메일 ...
# -----------------------------------------------------------------
# contact = {}
# contact['010'] = {'name':'hong', 'email':'hong@naver.com'}
# contact['110'] = {'name':'Kim'}
# contact['231'] = {'email':'hong@naver.com'}
# contact['009'] = {}

# del contact['110']
# del contact

# def saveContact(phone, *info):
#     # 존재 여부 체크 => 멤버 연산자 in
#     if phone not in contact:
#         contact[phone] = phone
#     else:
#         print("이미 저장된 연락처 입니다.")
# -----------------------------------------------------------------

class Contact:

    def __init__(self):
        self.member = Member()

# -----------------------------------------------------------------
# 연락처 프로그램 데이터 클래스 => 데이터 타입
# - Member
# - 필수 데이터 => 이름, 전화번호, 이메일
# - 선택 데이터 => 별명, 사진, 주소, 생일
# -----------------------------------------------------------------
class Member:
    # 클래스 변수

    # 인스턴스 변수 생성 및 초기화 메서드
    def __init__(self, phone, name, alias='', picture='', email='', addr='', birth=''):
        self.phone = phone
        self.name = name
        self.alias = alias
        self.picture = picture
        self.email = email
        self.addr = addr
        self.birth = birth
    
    # 인스턴스 메서드
    def showInfo(self):
        print(f"--- [{self.phone}]---")
        print(f"이  름 : {self.name}")
        print(f"별  명 : {self.alias}")
        print(f"주  소 : {self.addr}")
        print(f"이메일 : {self.email}")

mem = Member('010-1111-2222', 'hong')
mem2 = Member('111-222-1212', '마징가', addr='대구시')

mem.showInfo()
mem2.showInfo()

# -----------------------------------------------------------------
# 은행 관리 프로그램을 구현하고자 합니다.
# -----------------------------------------------------------------
# - 기  능 : 계좌 개설, 해지, 입금, 출금
# - 데이터 : 계좌번호, 예금주, 개설날짜, 이율, 잔액, 개설지점
# -----------------------------------------------------------------
class Bank:
    
    def __init__(self):
        self.account = Account

# -----------------------------------------------------------------
# 은행 관리 프로그램 데이터 클래스 => 데이터 타입
# - Account
# - 필수 데이터   => 계좌번호, 예금주, 개설날짜, 이율, 잔액, 개설지점
# - 선택 데이터   => 없음
# - 비공개 데이터 => 주민등록
# -----------------------------------------------------------------
class Account:
    # 클래스 변수
    BANK_NAME = 'DGB'

    # 인스턴스 변수 생성 및 초기화
    def __init__(self, number, name, date, rate, balance, branch, jumin):
        self.number = number
        self.name = name
        self.date = date
        self.rate = rate
        self.__balance = balance    # 비공개 데이터 => 클래스 밖에서 사용 불가
        self.branch = branch
        self.__jumin = jumin        # 비공개 데이터 => 클래스 밖에서 사용 불가

    # 인스턴스 메서드
    def accountInfo(self):
        print(f"--- [{self.number}]---")
        print(f"예 금 주 : {self.name}")
        print(f"주민 번호 : {self.__jumin}")
        print(f"잔    액 : {self.__balance}")   # 클래스 안에서 작용, 변경 가능
        print(f"이    율 : {self.rate}")

myAccount = Account('111', 'm', '121', 0.1, 1000, '-', '000131')
myAccount.accountInfo()
print('공개데이터 ', myAccount.rate)
print('비공개데이터 ', myAccount.__balance)   # 접근 불가!

# myAccount.__balance = 10000000              # 불법 증축!  # 클래스 밖에서 작용, 변경 불가
# print('나만의 데이터 ', myAccount.__balance)
print(myAccount.__dict__)

myAccount.accountInfo()