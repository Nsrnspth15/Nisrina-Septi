klasifikasi2=read.delim("clipboard")
View(klasifikasi2)

library(e1071)
library(caret)


sampel=sample(1:nrow(klasifikasi2), 0.8*nrow(klasifikasi2), replace = TRUE)
training=data.frame(klasifikasi2)[sampel,]
testing=data.frame(klasifikasi2)[-sampel,]
modelNB=naiveBayes(ket~.,data = training)

prediksi=predict(modelNB,testing)
hasil=confusionMatrix(table(prediksi,testing$ket))
hasil

