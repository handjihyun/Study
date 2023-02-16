# ======================================================
# Probability Distribution
# ======================================================
# ------------------------------------------------------
# Uniform distribution
# runif()
# ------------------------------------------------------
hist(runif(100, 0, 100), col = 'orange')
hist(runif(1000, 0, 100), col = 'blue')
hist(runif(10000, 0, 100), col = 'skyblue')
hist(runif(100000, 0, 100), col = 'lightblue')

# ------------------------------------------------------
# Binomial distribution
# success distribution of probability about success and fail
# dbinom() : probability of binomial distribution
# ------------------------------------------------------
dbinom(2, 10, 0.2)

a <- seq(0, 50, by = 1)

b <- dbinom(a, 50, 0.2)
plot(a, b)

b <- dbinom(a, 50, 0.6)
plot(a, b)

plot(a, pbinom(a, 100, 0.6))

# cumulative probability
# P[X > 3]
pbinom(3, 10, 0.2, lower.tail = F)
1 - pbinom(3, 10, 0.2)