# --------------------------------------------------
# 내장 데이터셋 iris
# - 데이터 분석
# - 독립변수, 종속변수
# - 선형분석 후 선형식 도출
# --------------------------------------------------
# 데이터 준비 및 확인 ------------------------------
str(iris)

# 데이터 전처리 ------------------------------------
sum(is.na(iris))

# 데이터 분포 형태 체크 ----------------------------
plot(iris)

iris.cor <- cor(iris[, -5]); iris.cor

dataDF <- data.frame(length = iris$Petal.Length, width = iris$Petal.Width); dataDF
plot(dataDF$length, dataDF$width)

# 독립변수 & 종속변수 선택 -------------------------
# 종속변수 : 너비
# 독립변수 : 길이

# 선형회귀식 도출 및 결과 출력 ---------------------
lmout1 <- lm(dataDF$width ~ dataDF$length); lmout1

# 상세정보
summary(lmout1)
abline(lmout1, col = 'darkblue', lwd = 2)

# 회귀계수만 추출 => coef(선형객체)
coef(lmout1)[1]; coef(lmout1)[2]
mCoef <- coef(lmout1)

# 회귀식
pre_y <- mCoef[2] * dataDF$length + mCoef[1]

# 잔차 => (관측치 - 예측치)^2
r_err <-sum(dataDF$width - pre_y); r_err
