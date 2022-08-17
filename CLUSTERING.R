CLUSTERING 

prediksi=read.delim("clipboard")
view(prediksi)
library(cluster)
library(factoextra)
library(tidyverse)
summary(prediksi)
str(prediksi)
prediksiku=prediksi[,-1]          
view(prediksiku)           
row.names(prediksiku)=prediksi[,1]             
view(prediksiku)
fviz_nbclust(prediksiku, kmeans, method = "wss")
fviz_nbclust(prediksiku, kmeans, method = "silhouette")
final=kmeans(prediksiku,3)
final
fviz_cluster(final, prediksiku)
finalakhir=data.frame(prediksiku, final$cluster)
view(finalakhir)

prediksiku%>% mutate(cluster=final$cluster)%>%
  group_by(cluster)%>%summarise_all("mean")

finalakhir[order(finalakhir$final.cluster),]
