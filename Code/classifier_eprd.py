import csv
import sys
import pandas as pd
import numpy as np
from mpmath import floor
from scipy.constants import precision
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import f1_score, roc_auc_score, precision_score, recall_score
from sklearn.model_selection import cross_val_score

def categorize(n):
    boundary = 42 # Use 730 for 2 years, 42 for 6 weeks
    if n > boundary:
        return 1
    return 0

path = "EPRD_MISSING" # Specify dataset file here, without .csv

fullframe = pd.read_csv("../Datasets/"+path+".csv")
fullframe.replace(-99, np.nan, inplace=True) # Replace "-99" with np.nan (missing value indicator)

# Drop features that can infer classification directly
xframe = fullframe.drop(["Durability", "FailInfection", "FailMech", "FailOther", "ObservationTime"], axis=1)
yframe = fullframe[["Durability"]]
yframe = yframe.map(lambda x: categorize(x))

print("Class balance: ", sum(yframe.values.ravel()) / len(yframe.values.ravel()))


catFeatures = ["Holiday", "TreatmentType", "Diagnosis", "entl_verleg_grund", "VitalStatus", "Sex",
               "GeriatricComplexTreat", "Fixation", "HemiType", "ShaftType", "ShellType", "AngegebenerWechselgrund",
               "StemFixationType", "OPMonth", "Weekday", "NumYear2022"]

catIndexes = [xframe.columns.get_loc(col) for col in catFeatures]


tsplit = int(floor(0.8 * fullframe.shape[0]))

xtrain = xframe[0:tsplit]
ytrain = yframe[0:tsplit].values.ravel()

xtest = xframe[tsplit:]
ytest = yframe[tsplit:].values.ravel()

clf = HistGradientBoostingClassifier(categorical_features=catIndexes, random_state=42)
clf.fit(xtrain, ytrain)


accuracy = clf.score(xtest, ytest)
print("Accuracy: ", accuracy)

crossval = cross_val_score(clf, xframe, yframe.values.ravel(), cv=5)
print("Cross-val scores: ", crossval)
print("Variance: ", np.var(crossval, ddof=1))

f1score = f1_score(clf.predict(xtest), ytest)
print("F1-score: ", f1score)

y_prob = clf.predict_proba(xtest)[:, 1]
rocauc = roc_auc_score(ytest, y_prob)
print("ROC-AUC: ", rocauc)

mroc = cross_val_score(clf, xframe, yframe.values.ravel(), cv=5, scoring="roc_auc")
print("MEAN ROC-AUC: ", mroc.mean())




