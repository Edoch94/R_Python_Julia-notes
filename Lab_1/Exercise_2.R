rm(list = ls())

setwd(file.path("D:","Documenti","RAM_PHM","RAM_PHM_course","Lab_1"))

library(tidyverse)

TM <- 10^3
M <- 10^4

l <- 3*10^(-3)
mu <- 25*10^(-3)

DT = 1
Time_axis = seq(0,TM,by=DT)
counter_q = rep_along(Time_axis, 0)
unrel <- matrix(data = rep(0), nrow = M, ncol = length(Time_axis))

for(i in 1:M){
  t = 0
  unrel_flag = 0
  state = 0
  # start_F = 0
  # end_F = 0
  
  while (t < TM) {
    if(state == 0){
      t = t+rexp(1,l)
      failure_time = t
      if(failure_time < TM && unrel_flag == 0){
        unrel_flag = 1
        unrel[i,ceiling(t):ncol(unrel)] = 1
      }
      state = 1
      start_F = ceiling(failure_time)
    }
    else{
      t = t+rexp(1,mu)
      state = 0
      repair_time = t
      if(t < TM){
        end_F <- ceiling(repair_time)
      }
      else{
        end_F <- length(Time_axis)
      }
      unrel[i,start_F:end_F] <- 1
    }
  }
  
}

a <- rep.int(0, times = ncol(unrel))
for(i in ncol(unrel)) {
  a[i] <- mean(unrel[,i])
}





