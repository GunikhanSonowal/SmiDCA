import pandas as pd
import numpy as np
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn import svm
from sklearn import metrics
import matplotlib.pyplot as plt
import csv
from Features import feature_extract
filename = 'english_dataset.csv'
data = pd.read_csv(filename)

def get_verify(test):

    df = data.values
    x = df[:, 0:-1]
    y = df[:, -1]

    clf = RandomForestClassifier(n_estimators=10, max_depth=None,
                                 min_samples_split=2, random_state=0)
    model = clf.fit(x, y)
    
    return  model.predict(test)


def smishing_verify(text):
    
    line = feature_extract(text)
    result = get_verify(line)
    if result.item() == 0:
        legitimate = "legitimate"
        return 0

    # phishing = "\n \n Warning - Smishing Suspected \n This message has been identified as forgery, intended to trick you into disclosing, personal or other information \n\n Suggestions: \n Tap the Proceed Button if you know the sender \n Otherwise Tap the Go Back button to delete the message \n\n More information Please Visit the site: https://************** or \n You may mail me at Email : ******@ **** \n you may contact me 9*************\n\n Thank you"
    return 1
        
if __name__ == "__main__":
    fp = open("test1.txt", "r")
    print smishing_verify(fp.read())
