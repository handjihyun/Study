# ---------------------------------------------------------------------
# 람다(lambda) 함수 : 익명함수, 1줄 함수
#                    짧은 코드의 함수
# 문볍 형식 : lambda 인자 : 실행코드
# ---------------------------------------------------------------------
# 입력받은 숫자를 모두 더해서 합계 출력하는 코드---------------------------
nums = input("원하는 수 만큼 숫자를 입력하세요. (예:1 3 5 2 ...)")

# '1 3 5 7 9 2' => ['1', '3', '5', '7', '9', '2']
nums = nums.split()  # [1, 3, 5, 7, 9, 2]

# str 요소 => int 요소
nums[0] = int(nums[0])
for idx in range(len(nums)):
    nums[idx] = int(nums[idx])
print('1 =>', nums)

# 리스트 컨프리핸션
nums = [int(n) for n in nums]
print('2 =>', nums)

# 값 * 3 결과로 반환하는 함수
def threeNum(num):
    return threeNum * 3

# 내장함수 => map(함수명, 반복가능객체) -> map 객체 반환
nums2 = list(map(str, nums))
print('3 =>', nums2)

nums4 = list(map(threeNum, nums))
print('4 =>', nums4)

nums5 = list(map(lambda n:n*3, nums))
print('5 =>', nums5)