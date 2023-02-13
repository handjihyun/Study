plot(1:3, xlim = c(-1.3, 1.3), ylim = c(-1.3, 1.3), type = 'n', xlab = '', ylab = '', axes = TRUE)

theta <- seq(-pi, pi, length = 365)
x <- cos(theta)
y <- sin(theta)

angle <- 40
rotation_matrix <- matrix(c(cos(angle), -sin(angle), sin(angle), cos(angle)), ncol = 2)
xy_rotated <- as.matrix(cbind(x-0.6, y/3+0.2)) %*% rotation_matrix
polygon(xy_rotated[,1], xy_rotated[,2], col = '#e00045', lty = 0)

angle <- 45
rotation_matrix <- matrix(c(cos(angle), -sin(angle), sin(angle), cos(angle)), ncol = 2)
xy_rotated <- as.matrix(cbind(x-0.6, y/3)) %*% rotation_matrix
polygon(xy_rotated[,1], xy_rotated[,2], col = '#e00045', lty = 0)

polygon(x/4-0.7, y/2+0.7, col = '#fea9d7')

angle <- 200
rotation_matrix <- matrix(c(cos(angle), -sin(angle), sin(angle), cos(angle)), ncol = 2)
xy_rotated <- as.matrix(cbind(x/2+0.75, y/4+0.6)) %*% rotation_matrix
polygon(xy_rotated[,1], xy_rotated[,2], col = '#fea9d7')

polygon(x, y, col = '#fea9d7')
polygon(x/8+0.2, y/3+0.5, col = '#0b0a13', lty = 0)
polygon(x/8-0.2, y/3+0.5, col = '#0b0a13', lty = 0)

polygon(x/14+0.2, y/6+0.65, col = 'white', lty = 0)
polygon(x/14-0.2, y/6+0.65, col = 'white',lty = 0)

polygon(x/15-0.2, y/11+0.27, col = '#244cd4', lty = 0)
polygon(x/15+0.2, y/11+0.27, col = '#244cd4', lty = 0)

polygon(x/6-0.5, y/8+0.2, col = '#f95fa8', lty = 0)
polygon(x/6+0.5, y/8+0.2, col = '#f95fa8',lty = 0)

polygon(c(-0.2,0.2,0), c(0.1,0.1,-0.1), col = '#f3212d',lty = 0)