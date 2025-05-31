import pandas as pd
import numpy as np
from mpmath import floor
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import f1_score, roc_auc_score
from sklearn.model_selection import cross_val_score

dftype = None
xframe = None
yframe = None
catIndexes = []
boundary = 730

def getBoundary():
    bound = input("Specify decision boundary (default = 730):")
    if bound == "":
        return 730
    if not bound.isnumeric() or (bound.isnumeric() and int(bound) <= 0):
        print("Please specify numeric value > 0.")
        return getBoundary()
    return int(bound)

def categorize(n):
    global boundary
    if n > boundary:
        return 1
    return 0

def preprocess():
    global xframe
    global yframe
    global catIndexes
    if dftype == "EPRD":
        fullframe.replace(-99, np.nan, inplace=True)
        xframe = fullframe.drop(["Durability", "FailInfection", "FailMech", "FailOther", "ObservationTime"], axis=1)
        yframe = fullframe[["Durability"]]
        yframe = yframe.map(lambda x: categorize(x))
        cat_features = ["Holiday", "TreatmentType", "Diagnosis", "entl_verleg_grund", "VitalStatus", "Sex",
                       "GeriatricComplexTreat", "Fixation", "HemiType", "ShaftType", "ShellType",
                       "AngegebenerWechselgrund",
                       "StemFixationType", "OPMonth", "Weekday", "NumYear2022"]

        catIndexes = [xframe.columns.get_loc(col) for col in cat_features]
    elif dftype == "PIMA":
        fullframe.replace("NAN", np.nan, inplace=True)
        xframe = fullframe.drop(["Outcome"], axis=1)
        yframe = fullframe[["Outcome"]]

def get_file():
    fname = input("Enter file name (without .csv): ")
    try:
        file = pd.read_csv("../Datasets/"+fname+".csv")
        global dftype
        if fname.startswith("EPRD"):
            dftype = "EPRD"
        elif fname.startswith("PIMA"):
            dftype = "PIMA"
        else:
            str(KeyError("Invalid file."))
            exit(-1)
        return file
    except FileNotFoundError:
        print(fname+" not found, please try again:")
        return get_file()



fullframe = get_file()
if dftype == "EPRD":
    boundary = getBoundary()
preprocess()


print("Class balance: ", sum(yframe.values.ravel()) / len(yframe.values.ravel()))





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




