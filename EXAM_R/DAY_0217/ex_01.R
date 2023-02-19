# =======================================
# CLT (Center Limit Theorem)
# =======================================
# ---------------------------------------
# normal distribution population
# mean : 52, s.d. : 5
# number of data : 10000
# function >> rnorm()
# ---------------------------------------
n <- 10000
nData <- rnorm(n, mean = 52, sd = 5)
hist(nData, main = 'population of normal distribution')

# sample group => sample size : 10, 30, 50
nData.bar <- c()
for (i in 1:1000) {
  nData.bar <- c(nData.bar, mean(sample(nData, size = 30)))
}
hist(nData.bar, col = 'skyblue', freq = F)

plot(density(nData.bar))


mean(nData.bar)
sd(nData.bar)

# ---------------------------------------
# Uniform distribution population
# min : 0, max : 1000
# number of data : 10000
# function : runif()
# ---------------------------------------
uData <- runif(n, min = 0, max = 1000)
hist(uData, main = 'population of uniform distribution')

uData.bar <- c()
for (i in 1:10000) {
  uData.bar <- c(uData.bar, mean(sample(uData, size = 100)))
}
hist(uData.bar, col = 'lightblue', freq = F)

mean(uData)
sd(uData)

# ---------------------------------------
# Chi-Squared distribution population
# Use at significance test
# probability distribution based on d.f.
# -> (cumulative prob, prob density, ...)
# ---------------------------------------
# prob about X
df = 30; x = 43.77
dchisq(x, df)

# cumulative prob about X
pchisq(x, df)                   # P[X <= x]
pchisq(x, df, lower.tail = F)   # P[X > x]

# A random variable that corresponds to a percentage
qchisq(0.95, df)

x = 0:50
plot(x, dchisq(x, 1), type = 'l', col = 'black')
lines(x, dchisq(x, 2), type = 'l', col = 'blue')
lines(x, dchisq(x, 3), type = 'l', col = 'red')
lines(x, dchisq(x, 4), type = 'l', col = 'orange')
lines(x, dchisq(x, 5), type = 'l', col = 'green')

# =======================================
# Binomial distribution Hypothesis test
# =======================================
#        Null hypothesis : p = 0.5
# Alternative hypothesis : p != 0.5
# alpha = 0.05
binom.test(x = 60, n = 100, p = 0.5)

set.seed(2022)
X <- rbinom(n = 10000, size = 100, prob = 0.5)
hist(X, col = 'lightblue', breaks = 15, freq = F)

x <- seq(0, 100, 1)
curve(dnorm(x, mean(X), sd(X)), add = T, col = 'pink', lwd = 2)

qnorm(p=0.095, mean(X), sd(X), lower.tail = F)
pnorm(q = 60, mean(X), sd(X), lower.tail = F)

# alpha = 0.01
binom.test(65, 100, 0.5, conf.level = 0.99)

# =======================================
# Normal distribution Hypothesis test
# =======================================
set.seed(9)
n <- 10
x <- 1:100
y <- seq(-3, 3, by = 0.01)

smps <- hist()
xbar <- apply(smps, 1, mean)
se <- 1 / sqrt(10)

alpha = 0.05

# 
z <-qnorm(1 - alpha / 2)
ll <- xbar - z * se
ul <- xbar + z * se