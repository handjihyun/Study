# ==============================================================
# Linear Regression Analysis
# - condition : exist linearity
#             : independent / dependent variable => causation, correlation
#             : data distribution -> normal distribution
# - result    : linear regression => regression coefficient
# - evaluation: smaller RSE, bigger R^2
# - test      : test about residual
# ==============================================================
# set data -----------------------------------------------------
file = "C:\\Users\\user\\Desktop\\iris.csv"
irisDF <- read.csv(file)

# check basic info of data
# (1) check with numerical value
str(irisDF)
summary(irisDF)

# (2) check with graph
# relationship between columns
plot(irisDF)

# check normality by column >> qqnorm()/qqline()/hist()/lines()
par(mfrow=c(2,4))
for (col in colnames(irisDF)[-5]){
  qqnorm(irisDF[,col], main = paste(col, 'Q-Q'))
  qqline(irisDF[,col], col = 'red', lwd = 2)
}

for (col in colnames(irisDF)[-5]){
  hist(irisDF[,col], freq = F, main = paste(col, 'HIST'))
  lines(density(irisDF[,col]), col = 'red', lwd = 2)
}

class(irisDF$sepal_length)        # numeric
class(irisDF['sepal_length'])     # data.frame
class(irisDF[, 'sepal_length'])   # numeric

# (3) check statistic function numerical value
# relationship between columns => cor(val1, val2)
# => select petal_length, petal_width
cor.test(irisDF$sepal_length, irisDF$petal_length)
cor.test(irisDF$sepal_length, irisDF$sepal_width)
cor.test(irisDF$sepal_length, irisDF$petal_width)
cor.test(irisDF$sepal_length, irisDF$petal_length)
cor.test(irisDF$petal_length, irisDF$petal_width)

# check normality by column >> shapiro.test()
for (col in colnames(irisDF[-5])){
  print(paste(col, round(shapiro.test(irisDF[, col])$p.value, 4)))
}

# Data Preprocessing -----------------------------------------
# (1) check missing value & mode

# (2) check duplication data

# (3) check & deal with outlier

# (4) range of data => change data : scale()

# ------------------------------------------------------------
# linear regression analysis of petal_length, petal_width
# - independent variable : petal_length
# - dependent variable   : petal_width
# - analysis method      : simple linear regression
# - lm(dependent ~ independent, data = )
# ------------------------------------------------------------
# (1) create simple linear regression model
irisMD <- lm(irisDF$petal_width ~ irisDF$petal_length, data = irisDF)

# (2) check value about simple linear regression model
# (2-1) regression coefficient : coef()
iris_slope <- round(coef(irisMD)[2], 4)
iris_inter <- round(coef(irisMD)[1], 4)

iris_slope; iris_inter

# (2-2) residual : resid()
resid(irisMD)

# simple linear regression report
summary(irisMD)

# ------------------------------------------------------------
# residual test
# - linearity
# - normality                  : shapiro.test()
# - homoscedasticity(등분산성) : ncvTest()  <- car package
# - independence               : lmtest package > dwtest()
# ------------------------------------------------------------
# (1) print test graph about model
plot(irisMD)

# (2) test numerical value based on function
# (2-1) normality
shapiro.test(resid(irisMD))

# (2-2) homoscedaticity
library(car)
ncvTest(irisMD)

# (2-3) independence
install.packages(lmtest)
library(lmtest)
dwtest()

# ------------------------------------------------------------
# linear regression analysis of petal_length, petal_width
# - independent variable : petal_length
# - dependent variable   : petal_width
# - analysis method      : multiple linear regression
# - lm(dependent ~ independent, data = )
# ------------------------------------------------------------
irisMD <- lm(irisDF$petal_width~., data = irisDF)
summary(irisMD)
