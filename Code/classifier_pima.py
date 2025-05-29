from math import floor
import pandas as pd
import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import f1_score, roc_auc_score
from sklearn.model_selection import cross_val_score


path = "PIMA_MISSING" # Specify file, without ".csv" suffix

fullframe = pd.read_csv("../Datasets/"+path+".csv")
fullframe.replace("NAN", np.nan, inplace=True)


xframe = fullframe.drop(["Outcome"], axis=1)
yframe = fullframe[["Outcome"]]

print("Class balance: ", sum(yframe.values.ravel()) / len(yframe.values.ravel()))


tsplit = int(floor(0.8 * fullframe.shape[0]))


xtrain = xframe[0:tsplit]
ytrain = yframe[0:tsplit].values.ravel()

xtest = xframe[tsplit:]
ytest = yframe[tsplit:].values.ravel()

clf = HistGradientBoostingClassifier(random_state=42)
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



