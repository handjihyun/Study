# ======================================================
# IF conditional statement
# ======================================================
x <- 1:5
y <- -2:2

if (any(x>0)) {print(x)}
if (any(y<0)) {print(abs(y))}
if (any(y<0)) {
  print(abs(y))
  cat("\n y contains negative values")
  }

# Example 1)
if (pi > 3) {cat('\n expr(T)')} else {cat('\n expr(F)')}
if (pi < 3) {cat('\n expr(T)')} else {cat('\n expr(F)')}

x <- 1:5
if (length(x) == 5) {
  if (sum(x) == 15) {cat('\n Vector x length =', length(x), 'sum =', sum(x))}
  else {cat('\n Vector x length !=', length(x))}
}

# Example 2)
a <- 1; b <- 2; c <- -3
d <- b**2 - 4 * a * c; d
if (d > 0) {c((-b - sqrt(d)) / 2 * a, (-b + sqrt(d)) / 2 * a)} else if (d==0) {
  -b / (2 * a)} else {
    cat('No roots')
  }

# ======================================================
# Ifelse conditional statement
# - ifelse(logical vector, if True expression, if False expression)
# ======================================================
x <- c(10, 3, 6, 9)
y <- c(1, 5, 4, 12)
ifelse (x > y, x, y)

# if score is greater than 50, pass or not fail
score <- c(80, 75, 40, 48)
grade <- ifelse (score >= 50, "pass", "fail")
data.frame(score, grade)

# Example (1) various conditional
y <- -2:2
ifelse (y > 0, y, -y)
abs(y)

tmp <- c(3, -1, 1, -2, 0)
sn <- ifelse (tmp > 0, 'pos', ifelse(tmp < 0, 'neg', 'zero'))
data.frame(tmp, sn)

# ======================================================
# switch(value, case1, case2, ...)
# ======================================================
# numeric valuable
x <- c(1, 3, 2, 5, 2)
i <- 1   # return mean(x)
i <- 2   # return median(x)
i <- 3   # return sd(x)
i <- 4   # return var(x)

switch (i, mean(x), median(x), sd(x), var(x))

# string valuable
type <- 'mean'
switch(type, mean = mean(x), sd = sd(x), var = var(x))

# Example (1)
x <- c(1, 3, 2, 5, 2)
i <- 3

if (i == 1) {
  mean(x)
} else if (i == 2) {
    median(x)
} else if (i == 3) {
    sd(x)
} else if (i == 4) {
    var(x)
  }

# Example (2)
type <- 'sd'

if (type == 'mean') {
  mean(x)
} else if (type == 'median') {
    median(x)
} else if (type == 'sd') {
    sd(x)
} else if (type == 'var') {
    var(x)
  }

# Example (3)
x <- c(1, 3, 2, 5, 2)

if (sum(x) > 5) {
  'sum(x) is greater than 5'
} else if (sum(x) < 5) {
    "sum(x) is less than 5"
} else if (sum(x) == 5) {
    "sum(x) is equal to 5"
}

# Example (4)
x <- c(1, 3, 2, 5, 2)

ifelse (x > 3, x - 3, x)

# Example (5)
x <- c(1, 3, 2, 5, 2)
y <- ifelse (x > 3, x - 3, x)
i <- 3

switch (i, x+y, x-y, x*y)

# Example (5)
score <- 65

if (score >= 90) {
  'A'} else if (score >= 75) {
    'B'} else if (score >= 50) {
      'C'} else {
        'D'}

ifelse(score >= 90, 'A',
       ifelse (score >=75, 'B',
       ifelse (score >= 50, 'C', 'D')))

# Example (6)
score <- 65
type <- 'square'

switch (type, 'sqrt' = sqrt(score), 'square' = score^2, 'log' = log(score))

# ======================================================
# for iteration statement
# - for (value in numeric or string vector)
#   {
#    expression to repeat 1
#    expression to repeat 2
#   }
# ======================================================
x <- vector()

for (i in 1:5) {
  x[i] <- i
}
x

# Example (1) ==========================================
x <- 3

for (i in 1:9) {
  cat(x, ' * ', i, ' = ', x * i, '\n')
}

# Example (2) ==========================================
for (i in 1:5) {
  cat(rep("*", i), '\n')
}

# Example (3) calculate mean ===========================
x <- c(1, 2, 3, 4, 5)
total <- 0

for (i in x) {
  total <- total + i
}
print(total / length(x))

# + calculate variance
x <- c(1, 2, 3, 4, 5)
mean_x <- mean(x)
total <- 0

for (i in x) {
  total <- total + (i - mean_x) ** 2
}
total / (length(x) - 1)
var(x)

# Example (4) ==========================================
x <- c(1, 2, 3, 4, 5)
total <- 0

for (i in x){
  if (i %% 2 != 0) {
    total <- total + i
  }
}
total / length(x[x %% 2 != 0])

# -----------------------------------------------------
for (i in x[x %% 2 != 0]) {
  total <- total + i
}
total / length(x[x %% 2 != 0])

# Example (5) ==========================================
xmat <- matrix(nrow = 4, ncol = 5)
n = 1

for (i in 1:5) {
  for (j in 1:4) {
    xmat[j, i] <- n
    n = n + 1
  }
}
xmat

# ======================================================
# while
# - while(conditional) {
#     expression to repeat 1
#     expression to repeat 2
#   }
# ======================================================
i = 1
while (i < 6) {
  cat(rep("*", i), '\n')
  i = i + 1
}

# ======================================================
# break
# - To stop while iteration statement
# ======================================================
s = 0

for (i in 1:10) {
  s = s + i
  if (i >= 5) {break}
}
s

# Example (1)
i <- 1

while (i < 11) {
  cat(i, sep = '\n')
  i = i + 1
  if (i == 8) {
    cat(i, "\n발사!")
    break
  }
}

# ======================================================
# next 
# - if satisfy specific conditional, don't run code that
#   inside of iteration statement and run next code
# ======================================================
s = 0

for (i in 1:10) {
  if (i %% 2 == 1) {next}
  s = s + i}
s

# Example (1)
x <- c(1, 5, 2, 3, 8)
total = 0

for (i in x) {
  if (i %% 2 == 1){next}
  total = total + i
}
total / length(x[x %% 2 == 0])

# ======================================================
# User-Defined function
# ======================================================
googoo81 <- function(x) {
  cat('\n')
  for (i in 1:9) {
    cat(x, '*', i, '=', x*i, '\n')
  }
  cat('\n')
}
googoo81(5)

# element of function could set default
# element setted by default can skip
a <- c(1, 3, 5, 6)

mean.k <- function(x, k) {
  return(mean(x^k))
}
mean.k(a, 2)
mean.k(a)     # Error!

mean.k2 <- function(x, k=3) {
  return(mean(x^k))
}
mean.k2(a, 2)
mean.k2(a)

# input various elements : if skip name of element, put element in order
a <- c(1, 3, 5, 6)

m.k <- function(x, k, t) {
  return(mean((x-t)^k))
}
m.k(a, 2, 1)
m.k(a, 1, 2)
m.k(a, k=2, t=1)
m.k(a, t=2, k=1)

# return value of function allow only one object
a <- c(1, 3, 5, 6)

std.ftn <- function(x) {
  return(mean(x), var(x))
}
std.ftn(a)   # Error! => Two return value

# Solution : Use list or data.frame to tie values
a <- c(1, 3, 5, 6)

std.ftn <- function(x) {
  return(list(mean = mean(x), var = var(x)))
}
std.ftn(a)

# ======================================================
# Local Valuable
# - can use inside of function
# - when function is end, delete valuable
# ======================================================
a <- c(1, 3, 5)

noact <- function(x) {
  loc <- 3
  return(loc)
}
noact(a)
loc

# ======================================================
# Global Valuable
# - valuable name "<<-" value
# - can use outside of function
# ======================================================
a <- c(1, 3, 5)

noact <- function(x) {
  a[1] <- 3
  glb <<- c(1, 2)
  return(a)
}
noact(a)
glb

# Example(1) Create BMI function
w <- c(55, 65, 50, 60, 45)
h <- c(1.68, 1.70, 1.60, 1.65, 1.62)

bmi <- function(w, h) {
  return(w / (h^2))
}
bmi(w, h)
bmi(51, 1.63)

# ------------------------------------------------------
a <- c(1, 3, 5)

noact <- function(x, type = 1) {
  if(type == 1) {a[1] <- 3}
  if(type ==2) {a[1] <<- 3}
  return(a)
}
noact(10)
a
noact(5, 2)
a
