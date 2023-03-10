# ---------------------------------------------------------------
# 바둑알이 놓여지는 위치 저장 클래스
# 클래스명 : point
# 변수
#       - 클래스변수
#       - 인스턴스변수 : x(공개용 속성), __y(비공개용 속성)
# 메서드
#       - 시스템 메서드 : __init__()
#       - 커스텀 메서드 : put(), show()
#       - getter/setter 메서드 : 비공개 속성의 값 읽기, 쓰기
#         get속성명(), set속성명()
# ---------------------------------------------------------------
class Point:
    # 클래스 속성

    # 인스턴스 속성 초기화 및 생성 메서드 => 생성자메서드
    def __init__(self, x, y):
        self.x = x  # 공개 데이터
        self.y = y  # 공개 데이터

    # 메서드 -----------------------------------------------------
    def put(self):
        print(f"({self.x}, {self.y}) -- o")

# 인스턴스(객체) 생성 ---------------------------------------------
p1 = Point(10, 5)
p2 = Point(5, 5)
p1.put()

print('p1 : ', p1.__dict__)
print('p2 : ', p2.__dict__)

# 클래스 상에 없는 속성, 인스턴스 생성 후 추가된 속성
p1.z = 17   # 불편증축
p1.__z = 'a'
# p1.__y = 200

print('p1 : ', p1.__dict__)
print('p2 : ', p2.__dict__)


# ----------------------------------------------------------------
class Point:
    # 클래스 속성

    # 인스턴스 속성 초기화 및 생성 메서드 => 생성자메서드
    def __init__(self, x, y):
        self.__x = x    # 비공개 데이터
        self.__y = y    # 비공개 데이터

    # 메서드 -----------------------------------------------------
    def put(self):
        print(f"({self.__x}, {self.__y}) -- o")
    
    # Getter/Setter 메서드 ---------------------------------------
    # 비공개 속성을 외부에서 접근 기능 제공 메서드
    def get__y(self): return self.__y
    
    def set__y(self, y): self.__y = y


p1 = Point(10, 5)
p1.put()

p1.__y = 12
p1.put()    # y값이 12로 변경되지 않음!

p1.set__y(50)
p1.put()

# 비공개 속성 값 읽기
print("p1.__y : ", p1.get__y())