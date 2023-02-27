# ===============================================================
# Seoul Bike Sharing Demand
# ===============================================================
dat <- read.csv("C:\\Users\\user\\Desktop\\SeoulBikeData.csv")
dat

# check data
str(dat)

# check missing data
sum(is.na(dat))

# select columns
dat <- dat[ ,2:11]; dat

# correaltion
cor(dat)

# y = Rented_Bike_Count, x = each column except Rented_Bike_Count
par(mfrow = c(3,3))
plot(Rented_Bike_Count ~ ., data = dat)

# multiple linear regression
out <- lm(Rented_Bike_Count ~ ., data = dat); out
summary(out)

par(mfrow = c(2, 2))
plot(out)

# 다중공선성 확인
# 2보다 크면 다중공선성이 있는 것
car::vif(out)
sqrt(car::vif(out)) > 2
# -> True 제외(Temperature, Humidity, Dew_point_temperature)

# 전진 선택
# 상수항만 포함시킨 회귀모형
fit.con <- lm(Rented_Bike_Count~1, data = dat)
fit.forward <- step(fit.con, scope = list(lower = fit.con, upper = out),
                    direction = 'forward')
fit.forward

# 후진 소거
fit.backward <- step(out, scope = list(lower = fit.con, upper = out),
                     direction = 'backward')
summary(fit.backward)

# 단계별 선택법
fit.both <- step(fit.con, scope = list(lower = fit.con, upper = out),
                 direction = 'both')
fit.both
summary(fit.both)

# 변수의 상대적 중요도를 시각화
model_1 <- lm(Rented_Bike_Count ~ Temperature + Hour + Humidity + 
                Rainfall + Solar_Radiation + Visibility + Snowfall, data = dat)

relweights <-
  function(fit,...){                         
    R <- cor(fit$model)   
    nvar <- ncol(R)          
    rxx <- R[2:nvar, 2:nvar] 
    rxy <- R[2:nvar, 1]      
    svd <- eigen(rxx)        
    evec <- svd$vectors                           
    ev <- svd$values         
    delta <- diag(sqrt(ev))  
    lambda <- evec %*% delta %*% t(evec)        
    lambdasq <- lambda ^ 2   
    beta <- solve(lambda) %*% rxy           
    rsquare <- colSums(beta ^ 2)                   
    rawwgt <- lambdasq %*% beta ^ 2    
    import <- (rawwgt / rsquare) * 100 
    lbls <- names(fit$model[2:nvar])   
    rownames(import) <- lbls
    colnames(import) <- "Weights"
    barplot(t(import),names.arg=lbls,
            ylab="% of R-Square",
            xlab="Predictor Variables",
            main="Relative Importance of Predictor Variables", 
            sub=paste("R-Square=", round(rsquare, digits=3)),
            ...)  
    return(import)
  }

par(mfrow = c(1, 1))
result <- relweights(model_1, col = 'blue'); result

# ----------------------------------------------------------------
out <- lm(formula = Rented_Bike_Count ~ Temperature + Hour + Humidity + 
            Rainfall + Solar_Radiation + Visibility + Snowfall, data = dat)
summary(out)