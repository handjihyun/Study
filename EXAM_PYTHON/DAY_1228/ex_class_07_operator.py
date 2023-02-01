# ---------------------------------------------------------------------------
# 연산자 (Operator) => 산술, 비교, 논리, 멤버, 대입
# 객체의 연산
# - list + list     || list * 정수
# - tuple + tuple   || tupe * 정수
# - str + str       || str  * 정수
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 평면에 점을 나타내는 데이터 타입의 클래스
# - 좌표 (x, y)     => 속성
# - 점찍다          => 메서드
# ---------------------------------------------------------------------------
class Point:
    # instance (즉, 객체) 속성 생성 및 초기화
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 덧셈 연산 시 자동 호출되는 콜백메서드
    def __add__(self, other):   # 객체 + 객체
        print('__add__()')
        return self.x + other.x, self.y + other.y   # tuple

    def __sub__(self, other):   # 객체 + 객체
        """_summary_
        Args: other
            other (int): _description_
        """
        print('__sub__()')
        self.x = self.x - other
        self.y = self.y - other

    # instance method
    def drawPoint(self):
        print(f"({self.x}, {self.y}) 찍다!!")

# Create instance (즉 개체)---------------------------------------------------
zeroPoint = Point(0, 0)
endPoint = Point(50, 50)

# method 호출 => 객체변수명.메서드명()
zeroPoint.drawPoint()
endPoint.drawPoint()

# Plus Point Instance (Point 인스턴스 덧셈하기) -------------------------------
result = zeroPoint + endPoint   # 자동으로 __add__() 불러옴
print(f'result => {result}')    # Error!

result2 = zeroPoint - 10
print(f'result2 => {result2}')
zeroPoint.drawPoint()


# ---------------------------------------------------------------------------
class A:
    def aa(self, a):
        print(a)

a = A()
a.aa(10)