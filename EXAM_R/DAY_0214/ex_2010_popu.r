# ======================================================
# data file loading
# ======================================================
popdata <- read.csv('D:/Study/DATA/2010_popu_house.csv', header = F)
head(popdata)

# check data
# (1) structure / information - str()
str(popdata)

# (2) number of row & column - dim()
dim(popdata)

# (3) number of row / column - nrow(), ncol()
nrow(popdata); ncol(popdata)

# (4-1) name of column - colnames()
colnames(popdata)

# (4-2) rename columns - colnames()
colnames(popdata) <- c('gender', 'age', 'relationship', 'education', 'boy', 'girl')
str(popdata)
