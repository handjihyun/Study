# ==================================================
# express discrete data
# -> express frequency of each data(value) >> table()
# -> draw bar graph
# ==================================================
# --------------------------------------------------
# load external data
# --------------------------------------------------
fileName = "C:/Users/user/Desktop/2010_popu_house.csv"
popData <- read.csv(fileName, header = F)
str(popData)

# --------------------------------------------------
# data backup => save(data, file route)
# --------------------------------------------------
savePath <- "C:/Users/user/Desktop/2010_popu_house.RData"
save(popData, file = savePath)

# --------------------------------------------------
# change code(numeric) categorical data into character
# factor(data, levels, labels)
# --------------------------------------------------
popData$V1 <- factor(popData$V1, levels = 1:2, labels = c('M', 'F'))

popData$V3 <- factor(popData$V3, levels = 1:14,
                     labels = c('가구주', '가구주의 배우자', '자녀', '자녀의 배우자',
                                '가구주의 부모', '배우자의 부모', '손자녀, 그 배우자',
                                '증손자녀, 그 배우자', '조부모', '형제자매, 그 배우자',
                                '형제자매의 자녀, 그 배우자', '부모의 형제자매, 그 배우자',
                                '기타 친인척', '그외같이사는사람'))

popData$V4 <- factor(popData$V4, levels = 1:8, 
                     labels = c('안받았음', '초등학교', '중학교', '고등학교', '대학-4년제 미만',
                                '대학교-4년제 이상', '석사과정', '박사과정'))

colnames(popData) <- c('gender', 'age', 'relationship', 'education', 'boy', 'girl')

str(popData)

savePath <- "C:/Users/user/Desktop/2010_popu_house.RData"
save(popData, file = savePath)
