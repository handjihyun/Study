# ======================================================
# Plot
# - plot() : draw plot in plot domain
#          : plot(y, options), plot(x, y, options)
# ======================================================
# Example (1)
var1 <- c(1, 2, 3, 4, 5)
plot(var1)

# Example (2)
x <- 1:3
y <- 3:1
plot(x, y, xlab = 'x축', ylab = 'y축', main = 'Plot Test')

# ------------------------------------------------------
# draw various chart with using plot function
# ------------------------------------------------------
x1 <- 1:5
y1 <- x1^2
z1 <- 5:1

# create matrix
mat1 <- cbind(x1, y1, z1); mat1

# create 2 rows 3 columns domain
par(mfrow = c(2, 3))
plot(y1, main = 'index')
plot(x = x1, y = y1, main = 'x^2')
plot(mat1, main = 'matrix')

plot(x1, y1, type = 'l', main = 'line')
plot(x1, y1, type = 'h', main = 'high density')
plot(x1, y1, type = 's', main = 'steps')

par(mfrow = c(1, 1))

# Example (1)
dat <- read.csv("C:/Users/user/Desktop/KIS.csv")
head(dat)

plot(dat$Trust, dat$DeR, type = 'l', xlab = '신뢰도', ylab = '부채비율',
     main = 'KIS chart')

# ======================================================
# Points
# - points(x, y, type = 'p', ...)
#   : dot
# ======================================================
x <- rep(1:5, rep(5, 5))
y <- rep(1:5, 5)

pchs <- c("!", "@", "#", "$", "%")
plot(1:5, type = 'n', xlim = c(0, 7.5), ylim = c(0.5, 5.5),
     main = 'poinys by "pch"')
points(x, y, pch = 1:25, cex = 2.5)
text(x - 0.4, y, labels = as.character(1:25), cex = 1.5)

# Example (1)
plot(iris$Sepal.Width, iris$Sepal.Length, cex = 1, pch = 20,
     xlab = 'width', ylab = 'length', main = 'iris')
points(iris$Petal.Width, iris$Petal.Length, cex = 1, pch = '+',
       col = 'blue')
points(iris$Sepal.Width, iris$Sepal.Length, cex = 1, pch = 15,
       col = 'pink')

# ======================================================
# Drawing line function
# : abline(), lines(), arrows()
# ======================================================
# ------------------------------------------------------
# abline(x, y, h(horizontal), v(vertical), reg(regression), coef(coefficient))
# ------------------------------------------------------
cars[1:4, ]
z <- lm(dist ~ speed, data = cars)

# check variable list
is(z)

# check coefficient
z$coefficients

plot(cars, main = 'abline')
abline(h = 20)                       # horizontal
abline(h = 30)
abline(v = 20, col = 'blue')         # vertical
abline(a = 40, b = 4, col = 'red')   # y = a + bx
abline(z, lty = 2, col = 'green')

# Example (1)
# - check 10 rows of cars dataset
cars[1:10, ]

# - use lm() for regression
z <- lm(cars$dist ~ cars$speed); z

# - draw plot
plot(cars, main = 'abline')

# draw horizontal line
abline(h = 30)
abline(h = 50)

# draw vertical line
abline(v = 10, col = 'purple')

# use a, b factor => y = a + bx equation
abline(a = 5, b = 5, col = 'red')

# use reg factor
abline(z, lty = 2, lwd = 2, col = 'blue')

# use coefficient factor
abline(z$coefficients, lty = 3, lwd = 2, col = 'orange')

# ------------------------------------------------------
# lines(x, y, lty)
# ------------------------------------------------------
lty1 = c('blank', 'solid', 'dashed', 'dotted', 'dotdash', 'longdash', 'twodash')
lty2 = c('33', '24', 'F2', '2F', '3313', 'F252', 'FF29')
plot(0:6, 0:6, type='n', ylim=c(0,20), xlab='', ylab='', main='lines')

# ------------------------------------------------------
lines(c(1,3), c(20,20), lty=1)
lines(c(1,3), c(19,19), lty=2)
lines(c(1,3), c(18,18), lty=3)
lines(c(1,3), c(17,17), lty=4)
lines(c(1,3), c(16,16), lty=5)
lines(c(1,3), c(15,15), lty=6)
lines(c(1,3), c(14,14), lty=lty1[1])
lines(c(1,3), c(13,13), lty=lty1[2])
lines(c(1,3), c(12,12), lty=lty1[3])
lines(c(1,3), c(11,11), lty=lty1[4])
lines(c(1,3), c(10,10), lty=lty1[5])
# ------------------------------------------------------
lines(c(1,3), c(9,9), lty=lty1[6])
lines(c(1,3), c(8,8), lty=lty1[7])
lines(c(1,3), c(7,7), lty=lty2[1])
lines(c(1,3), c(6,6), lty=lty2[2])
lines(c(1,3), c(5,5), lty=lty2[3])
lines(c(1,3), c(4,4), lty=lty2[4])
lines(c(1,3), c(3,3), lty=lty2[5])
lines(c(1,3), c(2,2), lty=lty2[6])
lines(c(1,3), c(1,1), lty=lty2[7])
legend(3.5, 20, legend=1:6, lty=1:6)
legend(3.5, 13, legend=c(lty1,lty2), lty=c(lty1,lty2))

# ------------------------------------------------------
# Draw arrows
# arrow(x #start, y #start, x1 #end, y1 #end, length,
#       angel, code, ...)
# ------------------------------------------------------
plot(1:9, type='n', axes=F, xlab='', ylab='', main='arrows')
arrows(1, 9, 4, 9, angle=30, length=0.25, code=2)
arrows(1, 8, 4, 8, length=0.5)
arrows(1, 7, 4, 7, length=0.1)
arrows(1, 6, 4, 6, angle=60)
arrows(1, 5, 4, 5, angle=90)
arrows(1, 4, 4, 4, angle=120)
arrows(1, 3, 4, 3, code=0)
arrows(1, 2, 4, 2, code=1)
arrows(1, 1, 4, 1, code=3)
# ------------------------------------------------------
text(4.5, 9, adj=0, 'angle=30, length=0.25, code=2 (default)')
text(4.5, 8, adj=0, 'length=0.5')
text(4.5, 7, adj=0, 'length=0.1')
text(4.5, 6, adj=0, 'angle=60')
text(4.5, 5, adj=0, 'angle=90')
text(4.5, 4, adj=0, 'angle=120')
text(4.5, 3, adj=0, 'code=0')
text(4.5, 2, adj=0, 'code=1')
text(4.5, 1, adj=0, 'code=3')

# ------------------------------------------------------
# Draw rectangle
# rect(xleft, ybottom, xright, ytop, density, angle, col
#     , border, lty, lwd ...)
# ------------------------------------------------------
op <- par(no.readonly = TRUE)
par(mar = c(0, 2, 2, 2))
plot(1:10, type = "n", main = "rect", xlab = "", ylab = "", axes = F)
rect(xleft = 1, ybottom = 7, xright = 3, ytop = 9)
text(2, 9.5, adj = 0.5, "defalut")
rect(1, 4, 3, 6, col = "gold")
text(2, 6.5, adj = 0.5, "col = \"gold\"")
rect(1, 1, 3, 3, border = "gold")
text(2, 3.5, adj = 0.5, "border = \"gold\"")
rect(4, 7, 6, 9, density = 10)
text(5, 9.5, adj = 0.5, "density = 10")
rect(4, 4, 6, 6, density = 10, angle = 315)
text(5, 6.5, adj = 0.5, "density=10, angle=315")
# ------------------------------------------------------
rect(4, 1, 6, 3, density = 25)
text(5, 3.5, adj = 0.5, "density = 25")
rect(7, 7, 9, 9, lwd = 2)
text(8, 9.5, adj = 0.5, "lwd = 2")
rect(7, 4, 9, 6, lty = 2)
text(8, 6.5, adj = 0.5, "lty = 2")
rect(7, 1, 9, 3, lty = 2, density = 10)
text(8, 3.5, adj = 0.5, "lty=2, density=10")
par(op)

# ------------------------------------------------------
# Draw polygon
# polygon(x, y, density, angle, col, lty, ...)
# ------------------------------------------------------
op <- par(no.readonly = TRUE)
par(mar = c(0, 2, 2, 2))
theta <- seq(-pi, pi, length = 12)
x <- cos(theta)
y <- sin(theta)
plot(1:6, type = "n", main = "PLOYGON", xlab = "", ylab = "", axes = F)

x1 <- x + 2
y1 <- y + 4.5
polygon(x1, y1)

x2 <- x + 2
y2 <- y + 2
polygon(x2, y2, col = "red", border="blue")

x3 <- x + 5
y3 <- y + 4.5
polygon(x3, y3, density = 10, angle=135)

x4 <- x + 5
y4 <- y + 2
polygon(x4, y4, lty = 2, lwd = 2)

text(2, 5.7, adj = 0.5, "defalut")
text(5, 5.7, adj = 0.5, "density = 10")
text(5, 3.2, adj = 0.5, "lty = 2, lwd = 2")
par(op)

# Example (1)
plot(c(1,8), c(-4,4), type = 'n')
x <- c(1,2, 3, NA, 4, 4, 6, 6)
y <- c(1, -4, 3, NA, -3, 3, 3, -3)

polygon(x, y, col = c('pink', 'blue'), border = c('red', 'orange'), lwd = 2,
        lty = c('dotted', 'solid'))
lines(c(1, 8), c(-2, -2), lty = 4, col = 'green')
arrows(1, 2, 8, 2, length = 0.5)
title('Polygons')

# Draw circle with polygon function
theta <- seq(-pi, pi, length = 361)
x <- cos(theta); y <- sin(theta)

plot(x, y, type = 'n')
polygon(x, y)

# move center of circle + adjust length of radius
plot(x, y, type = 'n')
x <- 0.5 + 0.1*cos(theta)
y <- -0.5 + 0.1*sin(theta)
polygon(x, y, col = 'red', border = 'white')

points(0.5, -0.5, pch = 20)
