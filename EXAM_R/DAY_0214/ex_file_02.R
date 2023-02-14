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

# categorical data frequency expression >> bar graph
barplot(table(popData$gender))
barplot(table(popData$relationship))

# draw bar graph the number of boy babies born
barplot(table(popData$boy))
