# -------------------------------------------------------------------------
# Exception Handling
# 실행 중 발생되는 오류로 프로그램이 중단되는 것을 
# 막아주기 위한 방법
# -------------------------------------------------------------------------
# num1 = 10

# try:
#     num2 = int(input("숫자 입력 : "))

# except ValueError as e: 
#     print(f"{e}")


# try:
#     print(f'{num1} / {num2} = {num1 / num2}')

# except ZeroDivisionError as e:
#     print(f"Error : ", {e})
#     # pass                   # Ignore Error

# print("============END============")

# -------------------------------------------------------------------------

# num1 = 10

# try:
#     num2 = int(input("숫자 입력 : "))
#     print(f'{num1} / {num2} = {num1 / num2}')

# except ZeroDivisionError as e:
#     print("Error: ", e)
# except ValueError as ve:
#     print(f"Error : ", {ve})

# print("============END============")

# -------------------------------------------------------------------------

num1 = 10

try:
    num2 = int(input("숫자 입력 : "))
    print(f'{num1} / {num2} = {num1 / num2}')

except Exception as e:
    print(f"Error: {e}")

finally:
    print("항상 실행")

# -------------------------------------------------------------------------

FILE = 'a.txt'

try:
    fp = open(FILE, mode='w', encoding='utf-8')
    fp.write(1234)

except FileExistsError as e:
    print("이미 존재하는 파일입니다")
except FileNotFoundError as e:
    print("존재하지 않는 파일입니다.")
except Exception as e:              # Exception이 제일 위로 가면 위에 2개의 처리는
    print("오류발생 :", e)           # 실행되지 않는다!
finally:
    if fp: fp.close()
    print("파일 닫기")