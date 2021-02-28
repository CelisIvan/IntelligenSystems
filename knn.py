import numpy as np
import pandas as pd
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split

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

# create model
knn = neighbors.KNeighborsClassifier(n_neighbors=25, weights='uniform')

x_training, x_testing, y_training, y_testing = train_test_split(x,y,test_size= 0.2)
knn.fit(x_training, y_training)