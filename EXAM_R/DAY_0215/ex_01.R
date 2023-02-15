# ==================================================
# Descriptive statistics
# - summary of number feature
# ==================================================
# load external data -------------------------------
fileName = "C:/Users/user/Desktop/cafedata.csv"
cafeData <- read.csv(fileName)
str(cafeData)

# select / print specific column -------------------
cafeData[1]    # column
cafeData[1,]   # row
cafeData[34,]  # 34 index row

# check & deal with missing value ------------------
# - is.na() => T, F  : check
sum(is.na(cafeData))
sum(is.na(cafeData$Coffees))

# - na.omit()      : delete
cafeData <- na.omit(cafeData)
sum(is.na(cafeData))

# complete.cases() 
# : check rows that don't have missing value
#   if all of elements of row aren't NA, return T
is.na(cafeData)
complete.cases(cafeData)

# mode ---------------------------------------------
# no function offer!
# mode about "coffee" column
# frequency >> max value of frequency table
coffee <- table(cafeData$Coffees)
coffee
max(coffee)

# stem - leaf plot ---------------------------------
# graph that express with number >> stem()
data <- c(1, 1, 2, 2, 3, 3, 3, 3, 4)
stem(data)

data <- c(11, 11, 22, 22, 23, 31, 32, 33, 34, 40)
stem(data)

# standard deviation---------------------------------
# check distribution of data
height <- c(164, 166, 168, 170, 172, 174, 176)

# (1) mean()
height.m <- mean(height); height.m

# (2) Deviation >> value - mean
height - height.m

# (3) variance >> distance between whole data and mean
sum(height - height.m)    # it'll offset because of +, -
(height - height.m)^2     # square

mean((height - height.m)^2)                  # var
sum((height - height.m)^2) / length(height)  # var

sqrt(mean((height - height.m)^2))            # s.d.

# Use R function -------------------------------------
# calculate s.d. & var about "sample" 
# => different from above value
var(height); sd(height)