import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from knn_imp import KNN

def accuracy(y_real, y_pred):
    res= np.sum(y_real[0] == y_pred) / len(y_real)
    return res

def veredict(i):
    switcher = {
        1: "Sin Rank",
        2: "Bronce",
        3: "Plata",
        4: "Oro",
        5: "Platino",
        6: "Diamante"
    }
    return switcher.get(i,"Not an option")

ds = pd.read_csv("Datos-Modif.csv")

X = ds[['orderTotal', 'c_percentile']].values
y= ds[['rank']]

#mapping using numbers instead of strings
class_mapping ={
    'Diamante': 6,
    'Platino': 5,
    'Oro': 4,
    'Plata': 3,
    'Bronce': 2,
    'Sin Rank': 1
}
y['rank'] = y['rank'].map(class_mapping)
y = np.array(y)

#split and shuffle our data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

k = int(input("Introduce value for 'k': \n"))
my_knn = KNN(k=k)
my_knn.fit(X_train, y_train)

predictions = my_knn.predict(X_test)
print("Predictions for this DS")
print(predictions)
print("**********")
print(y_test)
print("-------")
print(predictions)
print("custom KNN classification accuracy", accuracy(y_test, predictions))
to_Predict =[[None]*2]
res = "Y"
while res == "Y" or res == "y":
    print("Do you want to do a prediction?")
    to_Predict[0][0] = float(input("Enter de value for orderTotal"))
    to_Predict[0][1] = float(input("Enter de value for c_percentile"))
    newPred = my_knn.predict(to_Predict)
    print("VEREDICT: ", newPred)


print("Thanks for using this predictor :)")