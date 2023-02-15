# =====================================
# internal data "airquality"
# =====================================
# check data
str(airquality)

# name of columns
colnames(airquality)

# number
dim(airquality)

# -------------------------------------
# extract rows that have missing value
# -------------------------------------
sel <- complete.cases(airquality); sel
airquality[sel, ]

# number of missing values
sum(complete.cases(airquality) == F)

# delete missing value
new <- na.omit(airquality); new

# -------------------------------------
# extract rows that don't have missing value
# -------------------------------------
airquality[!sel, ]

# -------------------------------------
# statistic about specific column
# ( mean, var, s.d., mode)
# -------------------------------------
# mean
mean(new$Ozone)

# variance
var(new$Ozone)

# standard deviation
sd(new$Ozone)

# mode
freq <- table(new$Ozone); freq
sort(freq)
max(freq)
which.max(freq) # mode = 23, 18th index