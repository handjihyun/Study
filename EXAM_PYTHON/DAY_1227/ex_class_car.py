# ----------------------------------------------------------------------
# 자동차 클래스
# 모델
# 가격
# 색상
# 크기
# 연료

# 얼마의 출력을 내보내는지
# ----------------------------------------------------------------------

class car:
    wheel = 4
    def __init__(self, model, cost, color, size, fuel):
        self.model = model
        self.cost = cost
        self.color = color
        self.size = size
        self.fuel = fuel

    def engine(self, num):
        print(f"{self.model}은 {num}의 출력을 내보낸다.")

myCar = car('캐스퍼', 1500, 'blue', '경형', '가솔린')
print(myCar.model, myCar.cost, myCar.color, myCar.fuel)
myCar.engine(75)

# ------------------------------------------------------------
# 클래스명 : Car
#   클래스변수 - Car클래스의 모든 인스턴스가 공유하는 변수
#   : maker
#   인스턴스변수 - 인스턴스마다 가지는 속성
#   : name, model, color, price, food, wheel, number

#   시스템 메서드
#   : __init__() -> 인스턴스 생성 시 속성 저장
#   메서드
#   def drive()
#   def eat()
#   def changeDir()
# ------------------------------------------------------------
class Car:
    MAKER = 'HD'

    # 생성자 메서드 - 시스템에서 자동 호출 즉 callback
    def __init__(self, name, model, color, food, wheel, number):
        # 인스턴스 변수들/속성들/필드들
        self.name = name
        self.model = model
        self.color = color
        self.food = food
        self.wheel = wheel
        self.number = number
    
    # 소멸자 메서드 - 시스템에서 자동 호출 즉 callback
    def __del__(self):
        pass

    # 메서드
    def drive(self, loc):
        print(f'{self.number}자동차가 {loc} 달리고 있다.')

    def eat(self):
        print(f'{self.number}자동차가 {self.food} 보충 중이다.')

    def changeDir(self, dir):
        print(f'{self.color}자동차가 {dir} 하고 있다.')
    
    def displayInfo(self):
        print(f'"이  름" : {self.name}')
        print(f'"연  료" : {self.food}')
        print(f'"바  퀴" : {self.wheel}')
        print(f'"번  호" : {self.number}')
        print(f'"모  델" : {self.model}')
        print(f'"브랜드" : {self.MAKER}')

# --------------------------------------------------------------------------
# 인스턴스와 클래스
# --------------------------------------------------------------------------
# Car 인스턴스 생성
myCar = Car('소나타', '승용차', '블랙', '휘발유', 4, '12가1212')

print(myCar.MAKER, Car.MAKER)

print('myCar.__dict__ :', myCar.__dict__)   # 인스턴스의 현재재 속성값 --> { 속성 : 값 }의 형태
print('myCar.__class__ :', myCar.__class__) # 인스턴스를 생성한 클래스 정보

for item in Car.__dict__.items():
    print(item)