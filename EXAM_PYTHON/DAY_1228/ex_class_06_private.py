# --------------------------------------------------------------------
# 객체지향언어   --> 정보은닉(캡슐링)
# - 속성 / 필드  --> 비공개 private
# - 메서드       --> 비공개 private ==> 공개 가능한 것만 공개 public
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# BMI 지수 => 키와 몸무게로 계산
# --------------------------------------------------------------------
class A:

    # 속성 2개 가지는 클래스 -------------------------------------------
    # self는 클래스 안에서만 사용
    def __init__(self, weight, height, bmi=0):
        self.__weight = weight  # private # in class => usable # out class unusable
        self.__height = height  # private # 객체변수명으로 사용불가
        self.bmi = bmi          # open class   # 객체변수명으로 사용 가능
    
    # 비공개 속성을 제어할 수 있는 메서드 -------------------------------
    # 비공개 속성의 값을 읽을 수 있는 메서드 => get속성명()
    # 비공개 속성의 값을 변경할 수 있는 메서드 => set속성명()
    def setWeight(self, weight):
        self.__weight = weight

    def getWeight(self):            # --> get이나 set뒤에 붙는 것은 속성명이라
        return self.__weight        #     생각할 수 있음

    # BMI calculator Method
    # BMI = weight / ( height / 100 ) ** 2
    def __calcBMI(self):
        self.bmi = self.__weight / ((self.__height / 100)**2)
        # self.bmi = self.__weight / ((self.__height / 100)*(self.__height / 100))

    # Information Method
    def showInfo(self):
        self.__calcBMI()
        print(f"몸무게 : {self.__weight}")      # == print(f"몸무게 : {self.getWeight()}") # 메서드 안 메서드
        print(f"  키   : {self.__height}")
        print(f"  BMI  : {self.bmi}")
    
    # Weight + / - Method
    def diet(self, value):
        self.__weight = self.__weight + value

# Create Instance (즉 객체) -------------------------------------------
# 변수 = 클래스명()
me = A(160.3, 78.3, '')

# 인스턴스 속성 확인 (Check Instance Attribute) ==> 변수명, 속성명
print("me.bmi => ", me.bmi)
print("me.__weight => ", me.getWeight())

me.showInfo()