raw_data <- read.csv("titanic_data.csv")

# 1) head 함수를 사용하여 입력된 raw_data를 확인하시오.
head(raw_data)

# 2) raw_data의 자료의 차원을 구하시오.
dim(raw_data)

# 3) raw_data의 첫번째 열에서 성별(Sex)을 추출하고 gender.txt로 저장하시오.
write.table(raw_data[1,]['Sex'], 'gender.txt')

# 4) raw_data의 2~10 열의 변수를 선택하여 새로운 객체에 저장하고
#    sub_data.txt로 저장하시오. (구분은 _을 이용할 것)
dat <- raw_data[, 2:10]
write.table(dat, 'sub_data.txt', sep = '_')

# 5) raw_data의 31~100의 행과 2~10 사이의 짝수 열을 선택하여 새로운 객체에
#    저장하고 sub_data2.csv로 저장하시오. (구분을 comma 사용)
dat2 <- raw_data[31:100, seq(2,10,2)]; dat2
write.table(dat2, 'sub_data2.txt', sep = ',')

# 6) raw_data에서 결측값의 갯수를 구하시오.
sum(is.na(raw_data))

# 7) raw_data에서 결측값의 위치를 1차원 인덱스로 찾으시오.
which(is.na(raw_data))

# 8) raw_data에서 결측값의 위치를 2차원 인덱스로 찾으시오.
which(is.na(raw_data), arr.ind = T)

# 9) raw_data의 Age변수의 결측값의 위치를 index 변수에 저장하고 이를 이용하여
#    모든 결측 값을 20으로 변경하시오.
index <- which(is.na(raw_data['Age'])); index
raw_data[index, 'Age'] <- 20

# 10) If 조건문을 활용하여, raw_data의 Age 변수를 활용하여 10이상 20미만,
#     20이상 30미만 ... 60이상 70미만, 그 외로 출력하는 r프로그램을 작성하시오.
ifelse(raw_data['Age'] >=10 & raw_data['Age'] < 20, '10이상 20미만',
       ifelse(raw_data['Age'] >=20 & raw_data['Age'] < 30, '20이상 30미만',
              ifelse(raw_data['Age'] >=30 & raw_data['Age'] < 40, '30이상 40미만',
                     ifelse(raw_data['Age'] >=40 & raw_data['Age'] < 50, '40이상 50미만',
                            ifelse(raw_data['Age'] >=50 & raw_data['Age'] < 60, '50이상 60미만', '그 외')))))

# 11) If 조건문을 활용하여 raw_data의 Cabin 변수에서 결측값이 들어간 위치에
#     ‘DELETE’라는 값으로 변경하시오.
ifelse(raw_data[, 'Cabin'] == "", 'DELETE', raw_data[, 'Cabin'])