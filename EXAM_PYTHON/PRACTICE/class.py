# 클래스 정의
# 비어있는 사람 (Human) 클래스를 "정의" 해보세요.
class Human:
    pass

# 인스턴스 생성
# 사람 (Human) 클래스의 인스턴스를 "생성" 하고 이를 areum 변수로 바인딩해보세요.
class Human:
    pass

areum = Human()

# 클래스 생성자-1
# 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하세요.
class Human:
    def __init__(self):
        print("응애응애")

areum = Human()

# 클래스 생성자-2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.
class Human:
    def __init__(self, name, age, gender):
        print("응애응애")
        self.name = name
        self.age = age
        self.gender = gender

areum = Human("아름", 25, "여자")

# 인스턴스 속성에 접근
# 위에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 인스턴스 변수에 접근하여 값을 출력하면 됩니다.
print(areum.name, areum.age, areum.gender)

# 클래스 메소드 - 1
# 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.
class Human:
    def __init__(self, name, age, gender):
        print("응애응애")
        self.name = name
        self.age = age
        self.gender = gender
    def who(self):
        print(f"이름: {self.name}, 나이: {self.age}, 성별: {self.gender}")

areum = Human("아름", 25, "여자")
areum.who()

# 클래스 메소드 - 2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.
class Human:
    def __init__(self, name, age, gender):
        print("응애응애")
        self.name = name
        self.age = age
        self.gender = gender

    def who(self):
        print(f"이름: {self.name}, 나이: {self.age}, 성별: {self.gender}")

    def setInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

areum = Human("모름", 0, "모름")
areum.who()

areum = Human("아름", 25, "여자")
areum.who()

# 클래스 소멸자
# 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.
class Human:
    def __init__(self, name, age, gender):
        print("응애응애")
        self.name = name
        self.age = age
        self.gender = gender

    def who(self):
        print(f"이름: {self.name}, 나이: {self.age}, 성별: {self.gender}")

    def setInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __del__(self):
        print("나의 죽음을 알리지 마라")

areum = Human("아름", 25, "여자")
del(areum)

areum.who()