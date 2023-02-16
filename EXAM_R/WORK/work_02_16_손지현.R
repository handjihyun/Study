# Q1)
par(mfrow=c(3,1))
barplot(table(sample(1:6, 12, replace = T)), main = 'n=12')
barplot(table(sample(1:6, 1200, replace = T)), main = 'n=1200')
barplot(table(sample(1:6, 12000000, replace = T)), main = 'n=12000000')

# Q2) 이항분포관련 문제입니다.
#     아래 가지 조건 만족하는 분포도를 그리고 비교하여 설명해 주세요.

# Q2-1) - 확률변수 X가 시행 횟수가 10, 0.5 성공 확률이 인 이항분포를 따름
#          X ~ (10, 0.5), X . X B 확률변수 의 분포도를 그려주세요.
par(mfrow=c(3,1))
plot(1:10, pbinom(1:10, 10, 0.5))
plot(1:10, pbinom(1:10, 10, 0.1))
plot(1:10, pbinom(1:10, 10, 0.9))

# Q3) 정규분포 관련 문제입니다
# 국민소득 평균이 표준편차가 인 정규분포 $30,000, $10,000
# 확률변수 를 개인의 소득을 나타내는 확률변수라 할 때 X ,
# 어떤 사람의 소득이 사이에 있을 확률 계산 및 그래프로 $25,000 ~ $35,000
# 표현해 주세요.
pnorm(35000, 30000, 10000) - pnorm(25000, 30000, 10000)

par(mfrow=c(1,1))
x <- 25000:35000
plot(x, dnorm(x, 30000, 10000), type = 'l')

X <- rnorm(n = 10000, mean = 30000, sd = 10000)
hist(X, col = 'lightblue', breaks = 30)