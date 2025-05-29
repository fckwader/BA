#install.packages("VIM")
#install.packages("mice")

library(mice)
library(VIM)

path <- "EPRD_MISSING_small" # Specify name of dataset without ".csv" here

df <- read.csv(paste0("Datasets/", path, ".csv"))
df[df == -99] <- NA

#Specify numerical and categorical variables of EPRD dataset
numericals <- c("ttSur", "ttDis", "AdmissionAge", "Durability", "ObservationTime", "ElixCount", "ElixScore", "BMI")

for (col in numericals){
  df[[col]] <- as.numeric(df[[col]])
}

for (col in colnames(df)) {
  if (!(col %in% numericals)) {
    df[[col]] <- as.factor(df[[col]])
  }
}


method <- "mice" # Specify imputation method here, "mice" or "knn"


if(method == "mice"){
  imputed <- mice(df, m = 1)
  write.csv(complete(imputed), paste0("Output/", path, "_MICE.csv"), row.names = FALSE)
}else if(method == "knn"){
  imputed <- kNN(df, trace = TRUE, imp_var = FALSE)
  write.csv(imputed, paste0("Output/", path, "_KNN.csv"), row.names = FALSE)
}else{
  stop("Invalid method specified. Use 'mice' or 'knn'.")
}




