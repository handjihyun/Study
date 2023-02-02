# ------------------------------------------------------------------
# 1. 홀수차 마방진 프로그램
#   - 화면상에서 홀수를 입력 받아서 해당하는 (n x n) 행렬모양의 마방진을
#     구현하고 화면에 출력하시오.
# ------------------------------------------------------------------
import numpy as np
def magic_square():
    size = int(input("홀수차 배열의 크기를 입력하세요: "))

    if size % 2 != 0:
        print('Magic Square ({}x{})'.format(size, size))
    else:
        print("짝수를 입력하였습니다. 다시 입력하세요.")
        magic_square()
    
    ms = np.zeros((size, size))

    y1, x1 = 0, (size // 2)
    ms[y1, x1] = 1

    y, x = 0, 0

    for i in range(2, size**2+1):
        y, x = y1, x1
        y1 -= 1
        x1 += 1
    
        if (y1 < 0):
            y1 = size-1   
        if (x1 > size-1):
            x1 = 0
        if ms[y1, x1] == 0:
            ms[y1, x1] = i
        else:
            y1 = y + 1
            x1 = x
            ms[y1, x1] = i

    print(ms)

magic_square()