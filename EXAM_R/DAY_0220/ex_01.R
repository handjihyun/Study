# ====================================================
# "t - distribution"
# get sample from normal distribution
# ====================================================
t_value = 3.98
dt(t_value, df = 19)

# cumulative value
# default value : p[X <= 3.98]
pt(t_value, df = 19)

# change : P[X > 3.98]
pt(t_value, df = 19, lower.tail = F)

# probability about percentage
qt(0.05, df = 19)      # 95%
qt(0.5, df = 19)       # 50%
qt(0.25, df = 19)      # 25%
qt(0.25, df = 19)      # 25%

# ====================================================
# t - test based on "t - distribution"                     
# ====================================================
library(MASS)
str(cats)

# Null hypothesis : weight = 2.6kg
h0 = 2.7
data = cats$Bwt

# test
result <- t.test(data, mu = h0)
result

result$p.value    # p-value
result$conf.int   # 1 - alpha(significance level)

t.test(survey$Height, mu = 171, conf.level = 0.99)
# H1 : height < 171
t.test(survey$Height, mu = 171, alternative = 'less')

# H1 : height > 171
t.test(survey$Height, mu = 171, alternative = 'greater')