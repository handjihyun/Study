# --------------------------------------------------------------------------------------
# 사용자 정의 클래스 / 커스텀 클래스
# --------------------------------------------------------------------------------------
# 만들고자 하는 프로젝트(프로그램)에서 사용할 데이터를 저장하는 타입
# --------------------------------------------------------------------------------------
# 학생 정보를 저장하고 출력
# => 학교, 이름, 학년

# school = []
# name = []
# grade = []

# def study(subject):
#     print(f"{subject} 공부합니다.")

# def test(subject):
#     print(f"{subject} 시험칩니다.")

# def eat(food):
#     print(f"{food} 먹습니다.")

# ===> CLASS METHOD
class Student:
    # class variable - 모든 인스턴스 공유
    #                - 객체(Instance) 생성하지 없이 사용
    #                - 사용법 : 클래스명, 클래스변수명
    school = "대구중학교"
    name = '홍길동'
    grade = 1
    
    # Instance 즉 객체 생성 및 초기화 메서드 => 생성자 메서드(Constructor Method)
    # 새로운 메모리 공간에 생성 ===> self 담겨 있음
    def __init__(self, school, name, grade, schoolNum, num):
        self.school = school
        self.name = name
        self.grade = grade
        self.schoolNum = schoolNum
        self.num = num
    
    def play(self):
        print(self.name)
        print(Student.school)
        self.aa()
        Student.study('미술')

    def aa(self):
        pass

    # Class Method  - Instance 즉 객체 생성 없이 사용
    #               - 사용법 : 클래스명, 클래스메서드명
    def study(subject):
        print(f"{subject} 공부합니다.")

    def test(subject):
        print(f"{subject} 시험칩니다.")

    def test(self, subject):
        print(f'{subject} 시험칩니다.')

    def eat(food):
        print(f"{food} 먹습니다.")

# ==> 클래스 속성 및 메서드 사용
# st1 = Student()
# print(f"st1.school : ", st1.school)
# print(f"Student.school : ", Student.school)
# st1.study('미술')

# Student.school = '제주고등학교'
# Student.study('국어')

st1 = Student("대구중", "홍길동", 1, 1, 10)
# Student.test("국어")
Student.test("Happy") # -> test(self, subject)에 self로 들어가기 때문에 실행되지 않음