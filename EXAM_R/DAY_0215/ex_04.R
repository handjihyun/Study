# ==============================================
# internal data "iris"
# ==============================================
iris
str(iris)

# basic info
dim(iris)
colnames(iris)

# check & deal with missing value
sum(is.na(iris))

# check outlier about "Sepal Width"
box <- boxplot(iris$Sepal.Width, horizontal=TRUE)
text(box$out, rep(1, NROW(box$out)), labels = box$out, pos = c(1, 1, 3, 1))

Q <- quantile(iris$Sepal.Width, probs = seq(0, 1, 0.25), na.rm = F); Q
iqr <- IQR(iris$Sepal.Width); iqr

lout <- Q[2] - (1.5 * iqr); lout
uout <- Q[4] + (1.5 * iqr); uout