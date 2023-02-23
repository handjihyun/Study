# -----------------------------------------------------
# 선형회귀 구현
# -> 회귀계수 기울기, 절편
# -----------------------------------------------------
# 데이터 준비
score <- c(52, 66, 72, 83, 91, 97)
hour <- c(1, 2, 3, 4, 5, 6)
shDF <- data.frame(score = score, hour = hour)

# 데이터 분포 확인 -------------------------------------
# 선형성 확인
plot(score, hour, main = 'Score-StudyHour', col = 'blue', pch = 20, cex = 2)

# 정규분포 (정규성 검정)
shapiro.test(shDF$hour)
shapiro.test(shDF$score)

qqplot(shDF$hour, shDF$score)

# 데이터를 만족하는 직선 생성 --------------------------
# 1차 함수 y = slope * x + intercept
# By 최소제곱법으로 기울기와 절편 계산
# ------------------------------------------------------
sMean <- mean(shDF$score)
hMean <- mean(shDF$hour)

#기울기
slope <- sum((shDF$score-sMean)*(shDF$hour-hMean)) / sum((shDF$score-sMean)^2)
slope

# 절편
intercept <- hMean - (sMean * slope)
intercept

# 직선 식 : y = slope * x + intercept
pre_y <- slope * x + intercept
