# -----------------------------------------------------------------------
# Duck Typing
# - Dynamic Typing : Save Data ==> Decide Type
# - Type of Dynamic Typing
#   객체의 속성과 메서드를 보고 동일 타입 여부 결정
# -----------------------------------------------------------------------
class A:
    # Class Attribute
    LOC = '대구'

    # Create / Format Instance
    def __init__(self, num):
        self.num = num

    # Instance Method
    def play(self, item):
        print(f"{item} 하며 놀고 있다.")

class B:
    # Class Attribute
    LOC = '부산'

    # Create / Format Instance
    def __init__(self, num):
        self.num = num

    # Instance Method
    def movie(self, item):
        print(f"{item} 영화 재밌네요.")

class C:

    # Create / Format Instance
    def __init__(self, num):
        self.num = num

    # Instance Method
    def movie(self, item):
        print(f"{item} 영화 재밌네요.")

# Functions --------------------------------------------------------------
def printMsg(obj):
    print(f"{obj.LOC} 출력합니다.")

def doingNow(obj):
    obj.movie("아바타")

# Create / Use Instance
aa = A(2022)
bb = B(2023)
cc = C(2025)

# 다른 타입의 인스턴스 즉 객체 이지만 동일한 속성(ex. LOC)이 존재하는 경우
# 동일한 함수 사용 가능
printMsg(aa)
printMsg(bb)
# printMsg(cc)

# 다른 타입의 인스턴스 즉 객체 이지만 동일한 메서드(ex. movie)가 존재하는 경우
# 동일한 함수 사용 가능
# doingNow(aa)    # Error!
doingNow(bb)
doingNow(cc)