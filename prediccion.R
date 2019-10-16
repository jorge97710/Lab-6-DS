
library(tidyverse)
library(tau)
library(tm)
library(hash)

data <- read.csv("C:/Users/User/Desktop/Lab-6-DS/GrammarandProductReviews.csv")
data<- data.frame( text = data$reviews.text)

for (val in data){
  variable %+=% val + " "
}

removeURL <- function(data) gsub("http\\S+", "", x)
removeHash <- function(data) gsub("[@#&]\\S+", "", x)

removeNumPunct <- function(data) gsub("[^A-z[:space:]']*", "", x)
h <- hash()

nbtach <- 60
for (b in 1:49) {
  # for (b in 12932) {
  message(sprintf("Processing the %i-th batch", b))
  
  #concatetar los textos
  data <- data[data.len * b + (1:data.len)]

  bnt <- c(data) %>% 
    removeURL() %>% removeHash() %>% 
    removeNumPunct() %>% tolower() %>% stripWhitespace()
  
  #busqueda de trigrama
  trigram <- textcnt(bnt, n=3, split=" ", method="string", decreasing = TRUE) 
  
  #crear hash
  for (i in 1:length(trigram)) {
    if (trigram[i] < 4) {
      break
    } else {
      gram <- strsplit(names(trigram[i]), split = ' ')[[1]]
      history <- paste0(gram[1:2], collapse = ' ')
      candidate <- gram[3]
      count <- trigram[[i]]
      if (candidate %in% h[[history]]$candidate) {
        index <- h[[history]]$candidate == candidate
        h[[history]]$count[index] <- h[[history]]$count[index] + count
      } else {
        h[[history]]$candidate <- c(h[[history]]$candidate, candidate)
        h[[history]]$count <- c(h[[history]]$count, count)
      } 
    }
  }
  gc()
}

#Ejemplo h[["how are"]] y saca sugerencias. correr desde linea #67

h[["thank you"]]
