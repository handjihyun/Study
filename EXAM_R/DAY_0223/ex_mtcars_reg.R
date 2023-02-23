# -----------------------------------------------
# 내장 데이터셋 mtcars
# - 독립변수, 종속변수
# - 회귀모델 생성
# - 회귀계수만 출력
# -----------------------------------------------
# 데이터 확인
str(mtcars)

plot(mtcars)

# 결측치 확인
sum(is.na(mtcars))

# 상관계수 확인
cor(mtcars)

# 독립변수 : disp, 종속변수 : cyl
plot(mtcars$disp, mtcars$cyl)

# 회귀모델 생성
out <- lm(mtcars$cyl ~ mtcars$disp); out
summary(out)
abline(out, col = 'blue', lwd = 2)


# 다중회귀분석
out2 <- lm(mpg ~ ., data = mtcars); out2
summary(out2)

# =========================================================================
# 데이터 전처리
sortData <- sort(abs(cor(mtcars)[, 'mpg']), decreasing = T)[-1]; sortData
selNames <- names(sortData <- sortData[sortData > 0.7])
selNames <-  c(selNames, 'mpg'); selNames

mtcars[, selNames]

# 다중선형모델 생성 ------------------------------------------------------
# 종속변수 mpg ~ 독립변수 .(전체)
mModel <- lm(mtcars$mpg ~ ., data = mtcars); mModel

summary(mModel)

# (1) 회귀계수
coef(mModel)

# (2) 잔차체크
resid(mModel)

# (3) 선형회귀식 기반 연비 예측 결과
pre_value <- round(fitted(mModel), 1); pre_value

par(mfrow = c(2,2))
plot(mModel)

x <- 1:dim(mtcars)[1]; x

par(mfrow = c(1,1))
plot(x, pre_value, col = 'blue', pch = 20, cex = 2)  # 예측값 vs mtcars$mpg
par(new = T)
plot(mtcars$mpg, col = 'red', pch = 20, cex = 2)

# 예측함수 => predict(모델객체, newdata = 독립변수)

# -----------------------------------------------------------
library(car)
Prestige

# 변수의 표준화
sData <- scale(Prestige$income)
mean(sData); sd(sData)
# VS
mean(Prestige$income); sd(Prestige$income)
