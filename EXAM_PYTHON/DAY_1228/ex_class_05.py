# ---------------------------------------------------------------------
# (1) 어떤 클래스                 ===> 클래스 클래스명
# (2) 특징 / 성격 / 외형 / 속성 등 ===> 변수 속성(attribute), 필드(field)
# (3) 기능 / 역할 / 행동          ===>  클래스 전용 함수 메서드(Method)
# ---------------------------------------------------------------------
# 휴대폰 클래스
# ---------------------------------------------------------------------
# 전화
# 앱, 배터리, 번호, 문자보내기
# 브랜드 제조사
# 사진, 음악 네비게이션, 날씨
# 웹서핑하다 전화하다 사진찍다 
# 폴더 형태 크기 
# ---------------------------------------------------------------------
class Phone:
    # Class Variable
    MAKER = 'samsung'
    # 인스턴스 속성 생성 및 초기화
    def __init__(self, number, color):
        print('__init__()')
        # self ==> 메모리 주소
        self.__number = number  # 비공개 데이터 (Privite Data) # 클래스 안에선 사용, 변경가능
        self.color = color
    
    # 인스턴스 메서드
    def calling(self, phoneNumber):
        print(f"{phoneNumber}에 전화합니다.")

    def mms(self, message):
        print(f"{self.__number}에 {message}를 전송합니다.")

# 객체 생성 (Create Object, Create Phone Instance)
# variable = ClassName()
myPhone = Phone()   # Error! 속성 입력X
myPhone = Phone('samsung', '010-1111-2222', 'pink')

myPhone = Phone('010-1111-2222', 'pink')

hisPhone = Phone('samsung', '010-1111-2222', 'pink')
hisPhone.color = 'red'
hisPhone.number = '000-0000-0000' # 비공개 데이터는 밖에서 사용, 변경 불가!

# 클래스로 인스턴스 즉 객체 생성 -----------------------------------------
# 클래스명()  생성자 메서드 (Constructor Method)
# 메모리 힙에 객체 생성
myPhone = Phone()   # myPhone이라는 주소에 저장