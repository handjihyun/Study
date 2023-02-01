# ---------------------------------------------------------------------------
# read / write file (FILE INPUT / OUTPUT [I/O])
# ---------------------------------------------------------------------------
# (1) open          => movement mode : mode='w' write   mode='r' read
# (2) write & read
# (3) close
# ---------------------------------------------------------------------------

# ==============================[Write File]=================================
FILE_NAME = 'data.txt'

# (1) open file (file route + file name, mode, encoding)
fp = open(FILE_NAME, mode='w', encoding='utf-8')

# (2) write => write("str")
fp.write("Good\n")
fp.write("Happy")

# (3) close => close()
fp.close()

# ===============================[Read File]==================================
# (1) open file (file route + file name, mode, encoding)
fp = open(FILE_NAME, mode='r', encoding='utf-8')

# (2) read file => read() : bring every data ===> str type
allContext = fp.read()

# (3) close file
fp.close()

# Check file
print(f"allContext => {allContext}")

# ===============================[Read File]==================================
# (1) open file (file route + file name, mode, encoding)
data = open('DAY_1229\ex_class_03.py', mode='r', encoding='utf-8')

# (2) read file => read() : bring every data ===> str type
allData = data.read()

# (3) close file
data.close()

# Check file
print(f"allData => {allData}")