# =================================================
# visualization package
# ggplot, tidyverse
# =================================================
if (!require(tidyverse)){
  install.packages('tidyverse')
  library(tidyverse)
}

if (!require(ggplot2)){
  install.packages('ggplot2')
  library(ggplot2)
}
# =================================================
# visualization
# =================================================
# internal dataset "mpg"
mpg

colnames(mpg)

# visualization "mpg" data => graph ---------------
# ggplot : reset plot variable
# geom_point() : function that mark data
#                - x, y coordinate setting
#                - color  (point color)
#                - size   (point size)
#                - alpha  (point transparency = 투명도)
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy,
                           color = class, size = class, alpha = 0.7))

# available color
colors()[1:10]

# print graph after division window ---------------
mpgPlot <- ggplot(data = mpg)
mpgPlot + geom_point(mapping = aes(x = displ, y = hwy))+
  facet_wrap(~class, nrow = 2)