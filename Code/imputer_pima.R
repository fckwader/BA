library(mice)
library(VIM)

path <- "PIMA_MISSING"


df <- read.csv(paste0("Datasets/", path, ".csv"))


df[df == "NAN"] <- NA

df_int <- data.frame(lapply(df, as.integer))

# Specify categorical and numerical features
for(col in colnames(df)){
  df[[col]] <- as.numeric(df[[col]])
}

df[["Outcome"]] <- as.factor(df[["Outcome"]])


method <- "knn" # Specify imputation method here, "mice" or "knn"

if(method == "mice"){
  imputed <- mice(df, m = 1)
  write.csv(complete(imputed), paste0("Output/", path, "_MICE.csv"), row.names = FALSE)
}else if(method == "knn"){
  imputed <- kNN(df, trace = TRUE, imp_var = FALSE)
  write.csv(imputed, paste0("Output/", path, "_KNN.csv"), row.names = FALSE)
}else{
  stop("Invalid method specified. Use 'mice' or 'knn'.")
}

