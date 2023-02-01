# --------------------------------------------------------------
# File In / Output
# Stream : 흐름, 데이터의 흐름, 데이터의 이동 통로
#         - Type : Input Stream, Ouput Stream
# --------------------------------------------------------------
# with ~ as 구문
# - close 기능을 자동 실행
# --------------------------------------------------------------

FILE_NAME = 'newyear.txt'

# 파일 쓰기(write) ==============================================
# mode - w : cover(덮어쓰기)
# mode - a : append
# mode - x : exist file => Error, only not exist file avaluable
# ==============================================================
with open(FILE_NAME, mode='w', encoding='utf-8') as f:
    f.write("새해 복 많이 받으세요~~~2023 검은 토끼")

# 파일 읽기(read) ==============================================
# mode - r : read
# ==============================================================
with open(FILE_NAME, mode='r', encoding='utf-8') as f:
    print(f.read())

# 파일 복사(copy) ==============================================
# 조건 : 파일명 끝 부분에 숫자 추가
# 예시 : data.txt => data_1.txt => data_2.txt, ...
# ==============================================================

def copyFile(filename):
    # create file name
    _filename = filename.replace('.txt', '_1.txt')
    print(f'"_filename : {_filename}')
    
    # Method 01
    # Read File & Write in New File
    # with open(filename, mode='r', encoding="utf-8") as f:
    #     data = f.read()
    # with open(_filename, mode='w', encoding="utf-8") as f:
    #     f.write(data)
    
    # Method 02
    with open(filename, mode='r', encoding="utf-8") as f1:
        with open(_filename, mode='w', encoding="utf-8") as f2:
            f2.write(f1.read())

copyFile(FILE_NAME)

# ==============================================================
# copy에만 인덱스번호붙이기
FILE_NAME = 'newyear.txt'

with open(FILE_NAME, mode='w', encoding='utf-8') as f:
    f.write("새해 복 많이 받으세요~~~2023 검은 토끼\n")
    f.write("새해 복 많이 받으세요~~~2024 용\n")
    f.write("새해 복 많이 받으세요~~~2023 뱀\n")
    f.write("새해 복 많이 받으세요~~~2023 호랑이\n")

def copyFile(filename):
    _filename = filename.replace('.txt', '_1.txt')
    
    with open(filename, mode='r', encoding="utf-8") as f1:
        with open(_filename, mode='w', encoding="utf-8") as f2:
            lines = f1.readlines()
            for i in range(1, len(lines)+1):
                f2.write(f"({i}) " + lines[i-1])

copyFile(FILE_NAME)