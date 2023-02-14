# ==================================================
# load saved data >> load(data route)
# ==================================================
savePath <- "C://Users//user//Desktop//2010_popu_house.RData"
load(savePath)

# check data
str(popData)

# number of data by column >> table(data)
table(popData$gender)
table(popData$relationship)

# ==================================================
# Data Summary - Graph
# ==================================================
# --------------------------------------------------
# categorical data frequency expression >> bar graph
# --------------------------------------------------
barplot(table(popData$gender))
barplot(table(popData$relationship))

# --------------------------------------------------
# draw bar graph the number of boy babies born
# --------------------------------------------------
barplot(table(popData$boy))

# --------------------------------------------------
# draw histogram
# - hist(data, prbability=T, breaks=c(), right=F,
#        main= , xlab= , ylab= )
# --------------------------------------------------
hist(table(popData$age), breaks = c(seq(0:80, by = 10)))