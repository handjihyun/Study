# ======================================================
# law of large numbers (대수의 법칙)
?rbinom

# ------------------------------------------------------
# compare arithmetic probability & statistics probability by sample size 
# ------------------------------------------------------
v <- rbinom(10, 1, 0.5); v
mean(v)
sum(v) / 10

v1 <- rbinom(100, 1, 0.5)
mean(v1)
sum(v1) / 100

v2 <- rbinom(1000, 1, 0.5)
mean(v2)
sum(v2) / 1000

v3 <- rbinom(10000, 1, 0.5)
mean(v3)                                                                                                                                              
sum(v3) / 10000

# sample() : monte carlo
sample(1:10, 3)               # sampling without replacement
sample(1:2, 10, replace = T)  # sampling with replacement (복원추출)

sample(1:2, 10, replace = T, prob = c(0.8, 0.2))

# create random function
runif(1)
runif(10, min = 1, max = 10)