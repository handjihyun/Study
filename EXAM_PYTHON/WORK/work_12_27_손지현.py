# ---------------------------------------------------
# 1. 주소록 프로그램을 만들고자 합니다.
# [ 조건 ]
# (1) 주소록에 필요한 클래스 선정 후 클래스 생성
# ---------------------------------------------------
# 속성
# - 이름
# - 전화번호
# - 이메일

# 기능
# - 정보확인
# - 전화번호, 이메일 수정
# ---------------------------------------------------
class PhoneNum:

    # 생성자 메서드
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def showInfo(self):
        print(f'이    름 : {self.name}')
        print(f'전화번호 : {self.phone}')
        print(f'이 메 일 : {self.email}')

    def newphone(self, phone):
        self.phone = phone
    def newemail(self, email):
        self.email = email

myAddr = PhoneNum('손지현', '010-1111-2222', 'a@gmail.com')
myAddr.showInfo()

# ---------------------------------------------------
# 2. 은행 프로그램을 만들고자 합니다.
# [조건]
# (1) 은행 관리 업무에 필요한 클래스 선정 후 클래스 생성
# ---------------------------------------------------
# 속성
# - 은행명          #클래스
# - 이름
# - 전화번호        # 비공개
# - 주민번호        # 비공개
# - 계좌번호        
# - 통장 비밀번호   # 비공개
# - 잔액           # 비공개

# 기능
# - 정보확인
# - 전화번호 변경
# - 통장 비밀번호 변경
# ---------------------------------------------------
class Bank:

    # 클래스 변수 => 모든 인스턴스 함께 사용
    BANKNAME = '한국은행'

    # 생성자 메서드
    def __init__(self, name, phone, id, account, pw, money):
        self.name = name
        self.__phone = phone
        self.__id = id
        self.account = account
        self.__pw = pw
        self.__money = money
    
    #Getter/Setter 메서드 => 비공개 속성 접근 여부 메서드
    # 전화번호, 비밀번호는 변경될 수 있음 => set메서드 필요
    def set__phone(self, phone):
        self.__phone = phone
    def set__pw(self, pw):
        self.__pw = pw

    def ShowInfo(self):
        print(f'은 행 명 : {self.BANKNAME}')
        print(f'이    름 : {self.name}')
        print(f'계좌번호 : {self.account}')
        print(f'잔    액 : {self.__money}')

    def PriviteInfo(self):
        print(f'은 행 명 : {self.BANKNAME}')
        print(f'이    름 : {self.name}')
        print(f'전화번호 : {self.__phone}')
        print(f'주민번호 : {self.__id}')
        print(f'계좌번호 : {self.account}')
        print(f'잔    액 : {self.__money}')

myAccount = Bank('손지현', '010-1111-2222', '000000-0000000', 12345678, 0000, 0)
myAccount.ShowInfo()
myAccount.PriviteInfo()