# ----------------------------------------------------------------------------------------
# 상속(Inheritance) : 재사용 및 기능확장
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# 포인트를 나타내는 데이터 타입 => 클래스
# - class name
#   Point2D

# - attribute / field
#   좌표 x, y

# - function / role
#   점 찍기
#   동그라미 그리기
#   별 그리기
# ----------------------------------------------------------------------------------------
class Point2D:
    # class variable

    # create instance
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # instance method
    def pointting(self):
        print(f"{self.x, self.y}에서 점찍기")
    
    def drawCircle(self, color):
        print(f"{self.x, self.y}위치에 {color} 색상 동그라미 그리기")
    
    def drawStar(self, action):
        print(f"{self.x, self.y}위치에 {action} 별 그리기")
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# 3D 입체공간에 포인트를 나타내는 데이터 타입 => 클래스
# - class name
#   Point3D

# - attribute / field
#   좌표 x, y, z

# - function / role
#   점 찍기
#   동그라미 그리기
#   별 그리기
# ----------------------------------------------------------------------------------------
# class Point3D:
#     # class variable

#     # create instance
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     # instance method
#     def pointting(self):
#         print(f"({self.x}, {self.y}, {self.z})에서 점찍기")
    
#     def drawCircle(self, color):
#         print(f"{self.x, self.y, self.z}위치에 {color} 색상 동그라미 그리기")
    
#     def drawStar(self, action):
#         print(f"{self.x, self.y, self.z}위치에 {action} 별 그리기")
# ----------------------------------------------------------------------------------------
# Point2D 클래스 상속 받음
# 부모클래스 / 슈퍼(super)클래스 == Point2D
# 자식클래스 / 서브(serve)클래스 == Point3D
# 상속 관계 사용되는 키워드      => super
# ----------------------------------------------------------------------------------------
class Point3D(Point2D):

    # 인스턴스(즉 객체) 생성 및 속성 초기화 메서드
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    
    # 부모 클래스로부터 상속받은 메서드의 구현 부분을 변경 => 오버라이딩(Overriding)
    # 동일 = 메서드명, 매개변수
    # 변경 = 기능 구현 코드
    def drawCircle(self, color):
        print(f"{self.x, self.y, self.z}위치에 {color} 색상 동그라미 그리기")
# ----------------------------------------------------------------------------------------

# Create Instance => classname( 매개변수 ) <- __init__ 메서드랑 갯수 같아야 함
bluePoint = Point2D(20, 4)
bluePoint.drawCircle('파랑색')
bluePoint.drawStar("반짝이는")

bluePoint = Point3D(5,10,3)
bluePoint.drawCircle('핫핑크')

pinkPoint = Point2D(10, 5)
pinkPoint.drawCircle('pink')