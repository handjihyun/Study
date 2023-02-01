# --------------------------------------------------------------------------
# 사람 데이터 타입          ==> 헬스장 회원 데이터 타입
# 속성 / 성질 / 외모 ...    ==> 건강검진
# - 팔, 다리
# - 눈, 코, 입
# - 혈액형
# - 성격
# - mbti
# - 이름
# - 키, 몸무게
# - 생년월일
# - 홍채
# - 지문
# - 머리카락 색상
# - 성별
# - 직업
# - 나이
# - 주민번호, 휴대폰, 이메일

# 기능/역할/행동 ..
# - 말한다
# - 먹는다
# - 공부한다
# - 잔다
# - 논다
# - 걷는다
# - 생각한다
# - 쇼핑하다
# --------------------------------------------------------------------------


# --------------------------------------------------------------------------
# 사람 데이터 타입          ==> 동사무소에서 우리 동네 주민 관리 프로그램
# 속성 / 성질 / 외모 ...                Jumin
# - 이름
# - 생년월일        비공개
# - 성별
# - 주소            비공개
# - 나이            비공개
# - 전화번호        비공개
# - 주민번호        비공개
# - 생애주기

# 기능/역할/행동 ..
# - 필수 정보확인
# - 기본 정보확인
# --------------------------------------------------------------------------
class Jumin:
    # 클래스 변수 => 모든 인스턴스 함께 사용 ----------------------------------
    __DONG = '행복동'                     # 비공개, 클래스 내에서는 사용가능

    # 생성자 메서드
    def __init__(self, name, birth, gender, addr, age, phone, juminNum, lifecycle):
        self.name = name
        self.__birth = birth
        self.gender = gender
        self.__addr = addr
        self.__age = age
        self.__phone = phone
        self.__juminNum = juminNum
        self.lifecycle = lifecycle
    
    #Getter/Setter 메서드 => 비공개 속성 접근 여부 메서드
    # 전화번호, 주소는 변경될 수 있음 => set메서드 필요
    def set__phone(self, phone):
        self.__phone = phone

    def set__addr(self, addr):
        self.__addr = addr

    # 비공개 메서드

    # 일반 메서드 => 인스턴스 메서드
    def allInfo(self):
        print(f'------ [ 개인정보 상세 ] ------')
        print(f'- 이    름 : {self.name}')
        print(f'- 주    소 : {self.__addr}')
        print(f'- 주민번호 : {self.__juminNum}')

    def info(self):
        print(f'------ [ 개인정보 ] ------')
        print(f'- 이    름 : {self.name}')
        print(f'- 주    소 : {self.__addr}')
        print(f'- 생애주기 : {self.lifecycle}')