# --------------------------------------------------------------------
# Decorator
# - 메서드에 명확한 의미 부여
# - 형식 : @XXXX
# --------------------------------------------------------------------
# 클래스 종류
# - 완성된 클래스 ==> class
# - 미완성 클래스 ==> Abstract Class
#                    미구현(method without code) 메서드를 가지는 클래스
#                    Include abc module -> Use
# --------------------------------------------------------------------
# 메서드 종류
# - 객체 생성해야만 사용가능한 메서드 => self
#   - Instance Method
# - 객체 생성 없이 사용가능한 메서드  => cls
#   - 정  적 메서드 --> 객체 없이 사용가능
#   - 클래스 메서드 --> 클래스 정보를 가진 객체 없이 사용가능
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# Student Information Class
# - Class Name : Student
# - Attribute
#       - Class    Attribute : school
#       - Instance Attribute : name, number, grade
#- Method
#       - Class  Method : print school name
#       - Static Method : print school name
# --------------------------------------------------------------------
class Student:
    # Class Attribute
    school = '대구중학교'

    # Create Instance / Format Attribute Method
    def __init__(self, name, number, grade):
        self.name = name
        self.number = number
        self.grade = grade

    # 객체 미생성으로 사용가능한 메서드들
    @staticmethod
    def showSchoolName(count):
        Student.school = 'Happy중학교'
        print(f"[staticmethod]School => {Student.school} - {count}")

    @classmethod
    def printSchool(cls, count):
        print(f"cls ===> {cls}")
        print(f"[Classmethod ]School => {Student.school} - {count}")

# Use Class / Instance
print(Student.school)
Student.showSchoolName(1)
Student.printSchool(1)


# --------------------------------------------------------------------
# 대학생 정보를 담고 있는 클래스
# Class Name : BigStudent
# Attribute  : school, name, phone, grade, major
# --------------------------------------------------------------------
class BigStudent(Student):
    # Class Variable
    school = '한국대학교'

    # Create Instance / Format Attribute Method
    def __init__(self, name, number, grade, major):
        super().__init__(name, number, grade)
        self.major = major

# Use Class / Instance
BigStudent.showSchoolName(2)    # static Method
BigStudent.printSchool(2)       # Class  Method  # 클래스 정보를 가지고 가기 때문에 BigStudent의 cls 출력