asosiasi=read.delim("clipboard")
View(asosiasi)

library(rattle)
library(arules)
library(arulesViz)

matrans<-split(asosiasi$Tahun.23, asosiasi$Bulan)
matrans<-as(matrans,"transactions")
summary(matrans)
inspect(matrans)
itemFrequencyPlot(matrans,support=0.2)
itemFrequencyPlot(matrans,topN=3)

myrules<-apriori(data = matrans, parameter = list(support=0.2,confidence=0.1,minlen=1))
inspect(myrules)