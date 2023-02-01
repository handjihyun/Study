# ----------------------------------------------------------------------
# Read File
# ----------------------------------------------------------------------

FILE_NAME = 'happy.txt'

# ----------------------------------------------------------------------
# read() : bring every data in file
# ----------------------------------------------------------------------

fp = open(FILE_NAME, mode='r', encoding='utf-8')
allData = fp.read()
fp.close()

print(f'allData type ==> {type(allData)}, {len(allData)}\n{allData}')

# ----------------------------------------------------------------------
# readlines() : bring file => LINE Unit (줄단위)
# ----------------------------------------------------------------------

fp = open(FILE_NAME, mode='r', encoding='utf-8')
allData = fp.readlines()
fp.close()

print(f'allData type ==> {type(allData)}, {len(allData)}\n{allData}')

# ----------------------------------------------------------------------
# readline() : bring file => ONE LINE
# ----------------------------------------------------------------------

fp = open(FILE_NAME, mode='r', encoding='utf-8')
allData = fp.readline()
fp.close()

print(f'allData type ==> {type(allData)}, {len(allData)}\n{allData}')

# ----------------------------------------------------------------------

fp = open(FILE_NAME, mode='r', encoding='utf-8')
while True:
    line = fp.readline()
    print(f'[LINE] : {line}')
    if not line: break
fp.close()

# ----------------------------------------------------------------------

count = 1
while True:
    line = fp.readline()
    if not line: break
    print(f'[LINE {count}] : {line}')
    count += 1

fp.seek()