library(synthpop)

path <- "EPRD_KNN_small" # Specify filename without ".csv" suffix

df <- read.csv(paste0("Datasets/", path, ".csv"))


numericals <- c("ttSur", "ttDis", "AdmissionAge", "Durability", "ObservationTime", "ElixCount", "ElixScore", "BMI")

for (col in numericals){
  df[[col]] <- as.numeric(df[[col]])
}


for (col in colnames(df)[!colnames(data) %in% numericals]) {
  df[[col]] <- as.factor(df[[col]])
}

# How much additional data should be synthesized. Default: 30%
percentage <- 0.3

nrows <- round(percentage * nrow(df))

syn_model <- syn(df, k=nrows)

syndata <- syn_model$syn

combined <- rbind(df, syndata)

write.csv(combined, paste0("Output/", path, "_SYNTH30.csv"), row.names = FALSE)
print(paste0("Result has been written to: Output/", path, "_SYNTH30.csv"))


