# CSC 302 Draft - Question 2 Skyler West

library(ggplot2)
library(tidyr)


df <- house_prices
# 2a

gg1 <- ggplot(df, aes(x=date)) +
  geom_line(aes(y=house_price_index), color= '#E51837') +
  facet_wrap(vars(state), nrow=10, ncol=10)
  
gg1

# 2b 

house<-gather(df, "measure", "value", 2:3)
house


# 2c
ggplot(df, aes(x=date, y=house_price_index)) +
  geom_line(color= '#E51837') +
  facet_wrap(vars(state), nrow=10, ncol=10)
