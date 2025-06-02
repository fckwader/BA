# Appendix - Missing Data Imputation and Synthesis for Clinical Tabular Data
Vedad Barucija  
Technical University of Munich

## 1. Code
The appendix includes the code used for imputation, synthesis and classification.
Our classifier is written in Python, and can take user input to specify the file to be read, as well as the decision boundary for "Durability" if an EPRD-dataset is selected.  
As user input in R can be inconsistent across environments, the imputer and synthesis code is split by EPRD- and PID-dataset types. The file name, imputation method and synthesis percentage are set directly in the code.

### 1.1. Classifiers
The classifier uses Python 3.9. Datasets that can be used are found in the  ***Datasets/***  directory. 

### 1.2. Imputers
As preprocessing varies for EPRD and PID datasets, the imputation and synthesis are split into respective files. The file name can be specified using the ***path*** variable, and the imputation method is specified using ***method***, with possible values "mice" and "knn".

### 1.3. Synthesis
Similar pattern. File name ***path*** and percentage to impute ***percentage*** can be set in the file.


## 2. Datasets
The "Datasets" folder contains the PIMA Indians Diabetes datasets used in the thesis. Since we do not have licensing to redistribute the EPRD dataset, please contact Dr. Florian Hinterwimmer for requests (florian.hinterwimmer@tum.de). The following permutations of the datasets are available:
- _MISSING: Dataset includes missing data.
- _KNN: KNN-imputed dataset.
- _MICE: MICE-imputed dataset.
- _SYNTH30: Respective imputed dataset with 30% additional synthetic data.
For EPRD, we also included two "_small" datasets with only 2000 records, as runtime for the full datasets can span multiple hours for imputation and synthesis.

## 3. Miscellaneous
Under "Misc", a feature analysis of the EPRD dataset is included.

