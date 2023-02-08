# =================================================
print("Hellow")

1+1; 2+2; 3+3;

# =================================================
# arithmetic operator
# =================================================
3+5
8-3
3*8
12/4
5**2   # square
5^2
11%%4  # remainder
18%/%3 # quotient(share)

# =================================================
# comparison & logical operator
# =================================================
2 > 5
2 >= 6
4 == 4  # equal
5 != 5  # not equal
3 | 4   # or
3 & 4   # and

4>3 && 3==3   # return first element result
4<3 & 2==2
!FALSE

# =================================================
# create object
# =================================================
a <- 1
a = 1
a

# =================================================
# add
# =================================================
a <- 1
b <- 2
a + b

# =================================================
# rules of object name
# =================================================
Abc <- 1
a.b.c <- 3
# _abc <- 1 : cannot use "_" first
# if <- 1   : cannot use function name

# =================================================
# calculate area of circle
# =================================================
r = 4
r^2 * pi

# =================================================
# calculate mean
# =================================================
3500 / 30

# =================================================
# check type of data
# - mode(object)
# =================================================
x <- 'char'
mode(x)

x <- 5
is.character(x)
is.numeric(x)   # Is it numeric?
is.double(x)    # Is it float?

# =================================================
# change float to integer
# - as.integer()
# =================================================
real <- 3.5
as.integer(real)

intg <- 3
is.integer(intg)   # False => "intg" is float

intg2 <- as.integer(3)
is.integer(intg2)

# =================================================
# vector
# - put same data type in one vector
# - if type is different, they change the type automatically
# =================================================
vec <- c(1, 2, 3, 4, 5)
vec

num <- c(1, 2, 3)
ch <- c('red','blue','yellow')
lo <- c(T, F, F, T)
num2 <- c(1, 2, 'red', 'blue')
lo2 <- c(T, F, T, 1, 3)
lo3 <- c(T, F, 'abc')

# create empty vector
vec <- vector()

# numeric vector
vec <- 1:10

# character vector
vec2 <- c('abc', 'def')

# logical vector
vec3 <- c(T, F, F, T)

# give name to each element
names(vec2) <- c('first', 'second')

# create empty vector, use index to add element
vec4 <- vector()
vec4[1] <- 1; vec4[2] <- 5; vec4

# =================================================
# calculate various object
# =================================================
x <- c(1, 2, 3)
y <- c(1, 2, 3, 4)
x + y
x - y
x * y
x / y

# =================================================
# logical operation with objects
# =================================================
# AND operator (&)
A <- T; B <- F; C <- c(T, T);
D <- c(F, T)
A & B
A && B   # same with (A & B)
C & D
C && D

# OR operator (|)
A <- T; B <- F; C <- c(T, T);
D <- c(F, T)
A | B
A || B   # same with (A | B)
C | D
C || D

# Comparison operator (<, <=, >, >=, ==, !=)
a <- c(1, 2); b <- c(2, 2); d <- c(3, 4)
a < b
a <= b
a < d
a <= d
a > b
a >= b

# all() : all results are True  -> True
# any() : one of result is True -> True
A <- c(T, T); B <- c(F, T); C <- c(T, T); D <- c(T, F)
all(A == B)
all(C == D)
any(A == B)
any(A == C)

# != : not same
A <- c(T, T); B <- c(F, T); C <- c(T, T); D <- c(T, F)
all(A != B)
all(C != D)
any(A != B)
any(A != C)

# =================================================
# math functions
# =================================================
# log()
log10(10)

# exp()
exp(1); exp(2)

# sin(), cos(), tan()
sin(30); sin(pi/2)

# max(), min()
x <- c(1, 3, 2, 5, 10); max(x); min(x)

# range(vector) : return min, max of vector
x <- c(5, 10, 2, 5, 8, 9); range(x)

# sum() : add, prod() : multiple, mean(), var() : variance
var(x)
sum((x - mean(x)) ^ 2) / (length(x) - 1)   # same with var(x)

# =================================================
# sort functions
# - sort()
# - order() : 
# =================================================
x <- c(1, 5, 3, 2, 4)
sort(x, decreasing = T)

order(x)

# =================================================
# calculate BMI, mean, sd of weight
# =================================================
weight <- c(55, 65, 50, 60, 45)
height <- c(1.68, 1.70, 1.60, 1.65, 1.62)
bmi <- weight / height^2
bmi
avg <- mean(weight)
sqrt(var(weight))
sd(weight)

sqrt(sum((weight-avg)^2) / (length(weight)-1))   # same with sd(weight)

# =================================================
# seq(start, end, step) : Sequence operator
# =================================================
x <- seq(1, 100, 2)
x

x <- 1:10
y <- 3.3:8
x; y;


x <- 100:1; x

# =================================================
# rep() : Repeat function
# =================================================
rep(c(1, 2), times = 3)
rep(c(1, 2), each = 3)

# =================================================
# Practice
# =================================================
# (1)
x <- c('0', '21', '12', '16'); x

# (2)
x <- as.integer(x); sort(x);
# as.double(x)

# (3)
x <- as.character(x); x

# (4)
y <- seq(0, 30, 10); y

# (5)
x < y & x <= y

# (6)
z <- rep(c(T, F), times = 5); z

# =================================================
# matrix(value, nrow=num1, ncol=num2, byrow=F)
#                                     -> default
# =================================================
x1 <- matrix(1:10, nrow = 5, ncol = 2, byrow = T); x1
x2 <- matrix(1:10, 5, 2, byrow = F); x2

# add columns based row
cbind(x1, x2)

# add rows based column
rbind(x1, x2)

# =================================================
# give name to row, columns of matrix
# rownames, colnames
# matrix(..., dimnames = list(rname, cname))
# =================================================
A <- matrix(1:12, 4, 3)
rownames(A) <- c('n1', 'n2', 'n3', 'n4')
colnames(A) <- c('x1', 'x2', 'x3'); A

rname <- c('n1', 'n2', 'n3', 'n4')
cname <- c('x1', 'x2', 'x3')
B <- matrix(1:12, 4, 3, dimnames = list(rname, cname)); B

# =================================================
# select element from matrix
# =================================================
A <- matrix(1:12, 4, 3); A

# select one element
A[1, 2]; A[2, 3]

# select one row / column
A[1,]   # first row
A[,2]   # second column

# select many rows
A[c(1, 3),]
A[, 1:2]
A[, -3]      # except third column

# =================================================
# operation of matrix
# =================================================
# add matrix
A <- matrix(1:12, 4, 3); B <- matrix(1, 4, 3)
A + B
A - B

# multiple matrix
A <- matrix(1:6, 2, 3); B <- matrix(1, 3, 2)
A %*% B

# Inverse - solve()
A <- matrix(1:4, 2, 2)
solve(A)

# Transpose
t(A)

# determinant
det(A)

# =================================================
# List
# =================================================
# (1) list1 = list(name1 = element1, element2, ...)
lst1 <- list(a = 1:10, b = matrix(1:4, 2, 2)); lst1

# Indexing Method : select a
lst1$a

# (2) use [[sequence]]
lst2 <- list()                   # create empty list
lst2[[1]] <- matrix(1:10, 5, 2)
lst2[[2]] <- lst1
lst2

# (3) list[[sequence]]
lst1[1]         # return list object
lst1[[1]]       # element of list ( = lst1$a)
lst2[[1]]
lst2[[1]][3]    # index of matrix
lst2[[2]][[1]]

# =================================================
# Factor
# levels = when you create character vector, show level / order
# order = T : Ordinal, order = F : Nominal
# =================================================
grade <- c('A', 'A', 'B', 'C', 'B', 'B')
f.grade <- factor(grade); f.grade

f2.grade <- factor(grade, order = T); f2.grade

# To show wanted sequence : small >>> big
# Define on lev
lev <- c('C', 'B', 'A')
f3.grade <- factor(grade, levels = lev, order = T); f3.grade

# =================================================
# DataFrame
# df = data.frame(name1=val1, name2=val2, ...)
# length of valuable must be same
# =================================================
x1 = 1:4
x2 <- c('Kim', 'Lee', 'Jung', 'Park')
dat = data.frame(x1, x2); dat
dat2 = data.frame(num = x1, name = x2); dat2

# if, set the variable name -> Use $
dat2$num
dat2$name

# stringsAsFactors = F -> Prevent factor auto changing
dat3 = data.frame(x1, x2, stringsAsFactors = F);

dat[,1]; dat[,2]
dat[1,]; dat[2,]
dat[2, 1]; dat[3, 2]; dat3[3, 2]


# =================================================
# Array
# name <- array(vector, dim = dimension)
# =================================================
x1 <- array(1:24, dim = c(4, 3, 2)); x1
x2 <- array(1:32, dim = c(2, 2, 4, 2)); x2

# Indexing Method
x1[ , ,1]     # 4 X 3
x1[ , ,2]     # 4 X 3
x2[ , ,3, 1]  # 2 X 2
