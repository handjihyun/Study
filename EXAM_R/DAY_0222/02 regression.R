setwd('C:\\Users\\user\\Desktop\\class\\EXAM_R_VISUAL')
# ------------------------------------------------------------------------------
# 회귀(Regression)
# + 선형 데이터의 관계를 나타내는 모델 => 선형회귀모델 또는 선형회귀식
# + 전제 : 선형관계에 데이터
# + 예측 => 미래 데이터에 대한 예측 가능해짐
# ------------------------------------------------------------------------------
# 데이터 준비 ------------------------------------------------------------------
if (require(HistData)){
  print('Hi')
}else{
  install.packages('HistData')
  library(HistData)
}

source('utils\\util.r')

# 콜덴패밀리 데이터셋 정보 확인
displayInfo(GaltonFamilies)

# 부모 키 & 자식 키 데이터 관련성 
familyDf<- GaltonFamilies

# By 그래프
plot(familyDf$midparentHeight, familyDf$childHeight)

# By 수치
shapiro.test(familyDf$midparentHeight)
shapiro.test(familyDf$childHeight)

cor(familyDf$midparentHeight, familyDf$childHeight)
cor(familyDf$midparentHeight, familyDf$childHeight, method='kendall')

# 부모의 키가 자식의 키에 영향이 있다 ==> 직선
# lm()
# 종속 ~ 독림 <== familyDf$childHeight ~ familyDf$midparentHeight
lm(childHeight~midparentHeight, data=familyDf)

# ------------------------------------------------------------------------------
# 임의의 데이터 셋 ==> 회귀식 찾기
# ------------------------------------------------------------------------------

set.seed(14)
x <- runif(n=7, min=0, max=10)
y <- 3+2*x+rnorm(n=7,mean=0,sd=5)
round(x,2)
round(y,2)

# 선형 회귀 모델
df<- data.frame(x,y)
model <- lm(y~x,data=df)
coef(model)
intercept <- coef(model)[1]
slope <- coef(model)[2]
y.hat <- intercept + slope*x
round(y.hat,2)
r<- y - y.hat
round(r,2)


plot(df)
abline(model)







