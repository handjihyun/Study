# ----------------------------------------------------------------------------------
# 상속
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# 선생님을 나타내는 데이터 타입 => Class
# - attribute / field
#   학교
#   이름
#   학년
#   반
#   과목

# - Method
#   가르친다
#   담당하다
#   정보
# ----------------------------------------------------------------------------------
class teacher:
    def __init__(self, school, name, grade, tnum, subject):
        self.school = school
        self.name = name
        self.grade = grade
        self.tnum = tnum
        self.subject = subject

    def teach(self):
        print(f"{self.name} 선생님은 {self.subject} 을/를 가르친다.")

    def repon(self):
        print(f"{self.name}은 {self.tnum}반의 담임이다.")
    
    def showTinfo(self):
        print("--[선생님 정보]--")
        print(f"학교 : {self.school}")
        print(f"이름 : {self.name}")
        print(f"  반 : {self.tnum}")
        print(f"과목 : {self.subject}")

my = teacher("영남대학교", "이경섭", "4", "파이썬")
my.showTinfo()

# ----------------------------------------------------------------------------------
# 학생을 나타내는 데이터 타입 => Class
# - attribute / field
#   학교
#   이름
#   학년
#   반
#   번호
#   성별

# - Method
#   정보
# ----------------------------------------------------------------------------------
class student:
    def __init__(self, school, name, grade, ban, snum, gender) -> None:
        self.school = school
        self.name = name
        self.grade = grade
        self.ban = ban
        self.snum = snum
        self.gender = gender
    
    def showSinfo(self):
        print("--[학생 정보]--")
        print(f"학교 : {self.school}")
        print(f"이름 : {self.name}")
        print(f"{self.grade}학년 {self.ban}반 {self.snum}번")
        print(f"성별 : {self.gender}")


# ----------------------------------------------------------------------------------
# Parent Class
class common:
    def __init__(self, school, name, grade, ban):
        self.school = school
        self.name = name
        self.grade = grade
        self.ban = ban 

    def printInfo(self):
        print(f"학교 : {self.school}")
        print(f"이름:  {self.name}")
        print(f"학년:  {self.grade}")
        print(f"  반 : {self.ban}")

# Child Class
class teacher(common):
    def __init__(self, school, name, grade, ban, gender, subject):
        super().__init__(school, name, grade, ban)
        self.gender = gender
        self.subject = subject
    
    def teaching(self):
        print(f"{self.name} 선생님이 {self.ban}반에서 {self.subject}을 수업하신다.")

class student(common):
    def __init__(self, school, name, grade, ban, sub):
        super().__init__(school, name, grade, ban)
        self.sub = sub

    def study(self):
        print(f"{self.name}가 {self.sub}를 공부하고있다.")

t1 = teacher("영남대학교", "이경섭", 4, 1, "남", "파이썬")
my.teaching()

s1 = student("영남대", "손지현", 4, 1, "python")
s1.study()

# ----------------------------------------------------------------------------------
# 매개변수 => 값, 가변값, 키=값 가변, 디폴트값
# ----------------------------------------------------------------------------------
def calc(num1, num2, op='+'):   # default
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == "/":
        return num1 / num2 if num2 > 0 else print("0으로 나눌 수 없습니다!")

print(calc(10, 2, '*'))
print(calc(10, 2))