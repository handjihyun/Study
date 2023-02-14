# ===========================================================
# "cars" data
# print information of cars data
# draw graph about relationship between speed and distance of 50 cars
# ===========================================================
# load data -------------------------------------------------
cars

# check data ------------------------------------------------
# (1) structure / information - str()
str(popdata)

# (2) number of row & column - dim()
dim(cars)

# (3) number of row / column - nrow(), ncol()
nrow(cars); ncol(cars)

# (4) name of columns
colnames(cars)

# draw scatter ----------------------------------------------
# compare two variables => two datas
plot(cars$speed, cars$dist, main = 'speed vs distance',
     xlab = 'speed', ylab = 'distance')

# ===========================================================
# Nile Data
# ===========================================================
# load data -------------------------------------------------
Nile

# check data ------------------------------------------------
# (1) structure / information - str()
str(Nile)

# draw time-series plot -------------------------------------
plot(Nile)