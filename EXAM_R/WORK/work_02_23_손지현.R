# ==========================================
# heightweigth.csv
# ==========================================
# - 전처리
dat <- read.csv("C:\\Users\\user\\Desktop\\height_weight.csv"); dat
sum(is.na(dat))

boxplot(dat$height)
boxplot(dat$weight)

# 데이터 기술통계
str(dat)
describe(dat)

dat <- dat[!(dat$weight = 21),]

# 선형관계
plot(dat)
plot(dat$weight, dat$height)

out <- lm(height ~ weight, data = dat)
summary(out)

# ==========================================
# iris.csv
# ==========================================
dat <- iris[1:4]

# 데이터 기술통계
str(dat)
describe(dat)

boxplot(dat)

# 선형관계
cor(dat)
cor(dat$Petal.Length, dat$Petal.Width)

# 단순회귀분석
out <- lm(dat$Petal.Width ~ dat$Petal.Length); out
summary(out)
plot(out)

# 다중회귀분석
out2 <- lm(dat$Petal.Width ~ ., data = dat)
summary(out2)
plot(out2)

# 다항회귀분석
Petal.Length2 <- dat$Petal.Length^2
dat
