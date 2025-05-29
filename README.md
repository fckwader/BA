# Appendix - Missing Data Imputation and Synthesis for Clinical Tabular Data
Vedad Barucija  
Technical University of Munich

## 1. Code
The appendix includes the code used for imputation, synthesis and classification.
Code is separated by dataset (EPRD / PIMA) to avoid complicated execution, and includes some redundancy as a result.
Parameters such as file and algorithm to use are set in the code file directly, indicated by comments.

### 1.1. Classifiers
The classifier code files for both datasets use the same classification step with different preprocessing. File name can be specified in the file by adjusting the "path" variable.

### 1.2. Imputers
Similarly, the imputer files are identical except for the preprocessing step. File path is set identically to classifier code, and the imputation algorithm can be changed to either "mice" or "knn".

### 1.3. Synthesis
Similar pattern. File path and percentage to impute can be set in the file.


## 2. Datasets
The "Datasets" folder contains all datasets used in the thesis. "EPRD" and "PIMA" denote the respective origin of the dataset, with the following permutations:
- _MISSING: Dataset includes missing data.
- _KNN: KNN-imputed dataset.
- _MICE: MICE-imputed dataset.
- _SYNTH30: Respective imputed dataset with 30% additional synthetic data.

## 3. Miscellaneous
Under "Misc", a feature analysis of the EPRD dataset is included.

