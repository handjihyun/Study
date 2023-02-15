# ===============================================
# Check Outlier data
# : meaning of out of range data
# Use internal data "cars"
# columns : speed, dist
# ===============================================
# (1) structure & characteristic of data
str(cars)

# (2) dist data
disData <- cars$dist; disData

# (3) statistic about dist data
mean(disData)
median(disData)
min(disData)
max(disData)

hist(disData, breaks = seq(0, 120, by = 10))

# (4) check outlier >> quantile
Q <- quantile(disData, probs = seq(0, 1, 0.25), na.rm = F); Q

# IQR normal data interval
iqr <- IQR(disData); iqr
lout <- Q[2] - (1.5 * iqr); lout
uout <- Q[4] + (1.5 * iqr); uout

boxplot(disData)

# select data except outlier
sum(disData > lout)
sum(disData < uout)