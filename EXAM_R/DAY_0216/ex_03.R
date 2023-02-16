# ------------------------------------------------------
# Normal distribution
# A bell-shaped distribution in which data is concentrated
# in the center and small data exist on the left and right sides
# => 규격화 --> standard normal distribution : mean 0, s.d. 1
# ------------------------------------------------------
par(mfrow = c(1,2))

# height mean : 172, s.d. : 10
set.seed(2022)
X <- rnorm(n = 1000, mean = 172, sd = 10)
hist(X, col = 'skyblue', breaks = 30)

mean(X); sd(X)

# height mean : 120, s.d. : 7
set.seed(2022)
X <- rnorm(n = 1000, mean = 120, sd = 7)
hist(X, col = 'lightblue', breaks = 30)

# P[160 < height < 180]
pnorm(q = 160, mean = 172, sd = 10)                  # P[height <= 160]
pnorm(q = 160, mean = 172, sd = 10, lower.tail = F)  # P[height > 160]
pnorm(q = 180, mean = 172, sd = 10)
pnorm(q = 180, mean = 172, sd = 10, lower.tail = F) 

1 - pnorm(160, 172, 10) - pnorm(180, 172, 10, lower.tail = F)
pnorm(q = 180, mean = 172, sd = 10) - pnorm(q = 160, mean = 172, sd = 10)