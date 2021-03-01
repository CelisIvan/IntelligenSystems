import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
import array

def veredict(i):
    switcher = {
        1: 'AB: Abnormal',
        2: 'NO: Normal',
        3: 'SL: Spondylolisthesis',
        4: 'DH: Disk hernia'
    }
    return switcher.get(i,"Not an option")

data = pd.read_csv('vertebral.dat', delim_whitespace=True)
print(data.head())
x = data[[
    'p_in',
    'p_tilt',
    'l_lor_a',
    's_slope',
    'p_radius',
    'g_spond'

]].values

y = data[['class']]

# map classes to numbers in order to get the model working properly
#  DH (Disk Hernia) = 4, Spondylolisthesis (SL) = 3, Normal (NO)= 2 and Abnormal (AB)= 1.
class_mapping ={
    'DH': 4,
    'SL': 3,
    'NO': 2,
    'AB': 1
}
y['class'] = y['class'].map(class_mapping)
y = np.array(y)

print("p_in: Pelvic incidence is defined as the angle between a line perpendicular to the sacral plate at its midpoint and a line connecting this point to the femoral head axis.")

# create model
knn = neighbors.KNeighborsClassifier(n_neighbors=25, weights='uniform')

x_training, x_testing, y_training, y_testing = train_test_split(x,y,test_size= 0.2)
knn.fit(x_training, y_training)

prediction = knn.predict(x_testing)

accuracy = metrics.accuracy_score(y_testing, prediction)

print("prediction: ", prediction)
print("accuracy: ", accuracy)


again = "Y"
while again == "Y" or again == "y":
    option = int(input("Choose an option\n 1. Predict for input \n2. Compare prediction to actual value"))
    if option == 1:
        features = ["pelvic incidence", "pelvic tilt", "lumbar lordosis angle", "sacral slope" "pelvic radius","grade of spondylolisthesis"] 
        arr = [None] * 6
        for i in range(6):
            arr[i] = float(input("Enter the value for ", features[i]))
        print("Your values: ", arr)
        print("Predicted value for given input: \n" , knn.predict(arr))
    elif option == 2:
        myRow = int(input("Insert a number for the row you want to compare (0-310)"))
        print("Actual value: ", y[myRow])
        pre = knn.predict(x)[myRow]
        print("predicted value: ", pre)
        veredict(pre)
    else:
        print("Please choose a valid option")
    
    again = input("Again?")
print("Thanks for using this predictor :)")
