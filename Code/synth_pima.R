library(synthpop)

path <- "PIMA_KNN" # Specify filename here, without ".csv" suffix

data <- read.csv(paste0("Datasets/", path, ".csv"))



for (col in colnames(data)){
  data[[col]] <- as.numeric(data[[col]])
}


data[["Outcome"]] <- as.factor(data[[col]])

# How much additional data should be synthesized. Default: 30%
percentage <- 0.3

nrows <- round(percentage * nrow(data))

syn_model <- syn(data, k=nrows)

syndata <- syn_model$syn

combined <- rbind(data, syndata)

write.csv(combined, paste0("Output/", path, "_SYNTH30.csv"), row.names = FALSE)
print(paste0("Result has been written to: Output/", path, "_SYNTH30.csv"))

