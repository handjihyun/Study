# ----------------------------------------------------------------
# File Input / Output (I/O)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# Route
# - 절대경로(Absolute Path) : C 드라이브 기준
#                            'C:\EXAM_PYTHON'

# - 상대경로(Relative Path) : 현재 위치 기준
#                            .  ==> 현재위치
#                            .. ==> 한단계 위
# ----------------------------------------------------------------

FILE_NAME = './mydata.txt'  # mydata.txt (상대경로)

# (1) open file => write mode
fp = open(FILE_NAME, mode='w', encoding='utf-8')

# (2) write context
fp.write("Good Luck, Happy New Year")

# (3) close file
fp.close

# ----------------------------------------------------------------

FILE = 'DAY_1228\ex_class_04.py'
fp = open(FILE, mode='r', encoding='utf-8')
fp.read()