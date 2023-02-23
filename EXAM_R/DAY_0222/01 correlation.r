setwd('C:\\Users\\user\\Desktop\\class\\EXAM_R_VISUAL')
# -----------------------------------------------------------------------------------
# 상관관계 & 상관분석
# - 상관계수(Correation Confecient) : -1 ~ 1
# -----------------------------------------------------------------------------------
# 다른 R 스크립트 파일 포함 -----------------------------------------------------------
source('utils\\util.r')
# 데이터 준비 - 내장 데이터셋 cats ----------------------------------------------------
# 기본 정보 확인
library(MASS)
str(cats)
summary(cats)

displayInfo(cats)

# 전처리 -----------------------------------------------------------------------------
# (1) 결측치 => 원소 단위 : is.na(), 행 단위(완벽한 행 보여줌) : complete.cases()
sum(is.na(cats))
sum(complete.cases(cats)) # 완벽한 행
sum(!complete.cases(cats)) # 결측치

checkNa(cats)

# (2) 최빈값 => 요소에 대한 빈도 테입블, 최빈값 체크
mT <- table(cats$Bwt)
mT
for (col in colnames(cats)){
    if(class(cats[col][1,1])=='numeric'){
        table(cats[col])
    }
}

checkMode(cats)

# (3) 이상치/특이값 체크 => 과제

# 기술통계 분석 ----------------------------------------------------------------------
# (1) 그래프 방식 
# 컬럼/변수 2개에 대한 산점도
# 포뮬러 형식 : 종속 ~ 독립
plot(cats$Bwt~cats$Bwt, main='고양이 무게에 따른 심장무게', 
     xlab='몸무게(BWT,kg)', ylab='심장무게(HWT, g)')

# (2) 통계함수/수치 방식
# 1. 변수/컬럼의 상관관계 체크 => 정규분포 여부 --> 계산 방법 선정
# 1-1. 정규성 검정정
shapiro.test(cats$Hwt)
shapiro.test(cats$Bwt)

# 1-2.상관계수 계산 방법 결정 및 계산
# >> 몸무게랑 심장 무게랑 양의 상관관계계
cor(cats$Hwt, cats$Bwt)
cor(cats$Hwt, cats$Bwt,method='spearman')
cor(cats$Hwt, cats$Bwt, method='kendall')

# 검증 ------------------------------------------------------------------------------
# 귀무가설 : 상관계수가 0이다. 즉, 아무 관계가 없다
cor.test(cats$Hwt, cats$Bwt)
cor.test(cats$Hwt, cats$Bwt, method='spearman')
cor.test(cats$Hwt, cats$Bwt, method='kendall')
?cor.test

# 데이터 준비 - 내장 데이터셋 iris ----------------------------------------------------
# (1) 데이터 기본 정보
displayInfo(iris)

# 전처리 -----------------------------------------------------------------------------
# (1) 결측치 체크
checkNa(iris)

# (2) 최빈값 체크 <-- Na가 아닌 이상 데이터 확인
checkMode(iris)

# 기술통계 분석 ----------------------------------------------------------------------
# 4개 컬럼들의 상관계수 계산
# 컬럼들의 상관계수
iris.cor <- cor(iris[-5])
class(iris.cor)
iris.cor[4,2]

# 4개 컬럼들의 상관계수 검정  -------------------------------------------------------
# >> 추가 패키지 설치
# install.packages('psych')
library(psych)

corr.test(iris[-5])

# install.packages('gmm')
# install.packages('corrgram')
library(corrgram)
corrgram(iris[-5], upper.panel=panel.conf)


# ------------------------------------------------------------------------------
# 편상관관계 & 편상관계수
# > 두 변수의 상관관계에 영향을 미치는 제 3의 변수에 의해서 잘못 검사된
#   상관계수 도출 가능성 있음
# > 해당 문제를 해결하기 위한 제 3의 변수를 제어(통제)해서 상관계수값 추출함
# ------------------------------------------------------------------------------

# 내장 데이터셋 - mtcars -------------------------------------------------------
source('utils\\util.r')

# mtcars 데이터 정보 확인
displayInfo(mtcars)

# (1) 데이터와 데이터 타입 체크
# 숫자 또는 문자 => 범주형
mtcars2 <- within(mtcars, {
    vs<-factor(vs,label=c('V','S'))
    am<-factor(am,label=c('auto','menu'))
    cyl<-ordered(cyl)
    gear<-ordered(gear)
    carb<-ordered(carb)
})

displayInfo(mtcars2)

# 전처리 -----------------------------------------------------------------------
# (1) 결측치 체크
checkNa(mtcars)

# (2) 최빈값 체크
checkMode(mtcars)

# 기술통계 분석 ----------------------------------------------------------------
# 연비 - 마력(hp), 무게(wt), 실린더(cyl) 상관계수값 확인
cor(mtcars[-8])

mtcars.cor <- cor(mtcars)

# mpg와 상관계수가 가장 높은 컬럼과 가장 낮은 컬럼
names(which.max(abs(mtcars.cor[-1,1])))
names(which.min(abs(mtcars.cor[-1,1])))


# 범주형 제거 후 상관계수 전체
str(mtcars2)

# 상관계수값 확인 후 2개 변수 선택
# 연관성있는 변수 선택
# pcor()
install.packages('ggm')

library(ggm)














