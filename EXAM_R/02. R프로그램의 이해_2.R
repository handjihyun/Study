# ======================================================
# apply(): 
# rnorm(): random function
# ======================================================
x_mat <- matrix(rnorm(100), 20, 5)
x_mat

# Calculate mean values of each columns
apply(x_mat, 1, mean)
# Calclate mean values of each rows
apply(x_mat, 2, mean)
# Calclate variance values of each columns
apply(x_mat, 1, var)
# Calclate mean values of each rows
apply(x_mat, 2, var)

set.seed(1234)
rnorm(100)

# ======================================================
## character
# ======================================================
# paste(): attach string
#   - sep = ' ': defalt
# ======================================================
myname <- 'Woo chang'
paste('My name is', myname, sep = ' ')
paste0('My name is', myname)

# file name
file_id = 1533
paste('Dataset_', file_id, '.txt', sep = '')

# ======================================================
# nchar(): length of character
# ======================================================
test <- c('abcdefg', 'AFFY1245820')
test <- 'abcdefg'
nchar(test)
as.character()

# ======================================================
# substr(): Extract string
# ======================================================
f_name <- 'AFFY1245820'
substr(f_name, 5, 7)
substr(f_name, 5, nchar(f_name))

# ======================================================
# file IO
# ======================================================
# current working folder
getwd()

# Setting the location of the working folder(desktop)
setwd('C:/Users/user/Desktop')

getwd()

dir()

# Using file editor provided by R
dat <- data.frame()
dat <- edit(dat)
dat

# ======================================================
# Input Data
# ======================================================
# Use "scan"
x <- scan(file = 'input_noh.txt', what = numeric()); x
x <- scan(file = 'input_noh.txt', what = character()); x
x <- scan(file = 'input_noh.txt'); x

# Use "read.table"
dat <- read.table(file = 'input_noh.txt'); dat
dat2 <- read.table(file = 'input_noh.txt', header = F); dat2

# Use "read.csv"
dat <- read.csv("개인정보.csv", fileEncoding = 'euc-kr'); dat

# select height, weight
dat_info <- dat[, c(2, 3)]; dat_info

# create mean, median, variance row
stat_info <- c('평균', '중앙값', '분산'); stat_info

# calculate mean
mean_info <- apply(dat_info, 2, mean);
mean_info <- as.vector(c('평균', mean_info)); mean_info

dat[6, ] <- mean_info; dat[6, ]
# dat[(nrow(dat)+1), ] <- mean_info

# calculate median
median_info <- apply(dat_info, 2, median);
median_info <- as.vector(c('중앙값', median_info)); median_info

dat[7, ] <- median_info; dat[7, ]
# dat[(nrow(dat)+1), ] <- median_info

# calculate variance
var_info <- apply(dat_info, 2, var);
var_info <- as.vector(c('분산', var_info)); var_info

dat[8, ] <- var_info; dat[8, ]
# dat[(nrow(dat)+1), ] <- var_info

# export csv file
write.csv(dat, '작업완료.csv')

# ======================================================
# Print Data on Console or File
# ======================================================
# Use cat(object, file = 'path', sep='\n' or '\t')
x <- 1:10
cat(x, file = 'x.txt', sep = '\n')
cat(x, sep = '\t')
cat('\n', 1, 'st elememt of x =', x[1])

# Use write.table
x1 <- 1:20
x2 <- rep(c("A", "B", "B", "A"), 5)
x3 <- rep(c(T, F), each = 10)

dat <- cbind(x1, x2, x3)       # change to string
dat <- data.frame(x1, x2, x3)

write.table(dat, file = 'test1.txt', row.names = T, col.names = T, quote = T, sep = '\t')
write.table(dat, file = 'test2.txt', row.names = F, col.names = F, quote = F, sep = '\n')
#                                                                   -> " "
write.table(dat, file = 'test3.txt', sep = ', ')

# ======================================================
# Data summary / search Functions
# ======================================================
# head() or tail() : print first or end part of data
dat = read.csv(file = 'test3.txt')
head(dat, 5)
tail(dat)

# length(object) or dim(object) : check length or dimension of data
length(dat[,1])
dim(dat)
dim(dat)[1]
dim(dat)[2]
nrow(dat); ncol(dat)

# ======================================================
# Check NA(Not Available) / missing value
# ======================================================
# is.na()
x <- matrix(c(NA, 1, 3, NA, NA, 2), 3, 2)
is.na(x)
sum(is.na(x))   # number of missing values

# which() : return index that have TRUE value
# check location of missing values
which(is.na(x))               # 1-dimension 
which(is.na(x), arr.ind = T)  # 2-dimension   # row1 col1 -> exists missing value
which(is.na(x), T)            # 2-dimension

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

# Example 1) various conditional
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

# Example 1)
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

# Example 2)
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

# Example 3)
x <- c(1, 3, 2, 5, 2)

if (sum(x) > 5) {
  'sum(x) is greater than 5'
} else if (sum(x) < 5) {
    "sum(x) is less than 5"
} else if (sum(x) == 5) {
    "sum(x) is equal to 5"
}

# Example 4)
x <- c(1, 3, 2, 5, 2)

ifelse (x > 3, x - 3, x)

# Example 5)
x <- c(1, 3, 2, 5, 2)
y <- ifelse (x > 3, x - 3, x)
i <- 3

switch (i, x+y, x-y, x*y)

# Example 5)
score <- 65

if (score >= 90) {
  'A'} else if (score >= 75) {
    'B'} else if (score >= 50) {
      'C'} else {
        'D'}

ifelse(score >= 90, 'A',
       ifelse (score >=75, 'B',
       ifelse (score >= 50, 'C', 'D')))

# Example 6)
score <- 65
type <- 'square'

switch (type, 'sqrt' = sqrt(score), 'square' = score^2, 'log' = log(score))