import platform; print(platform.platform())
import sys; print("Python", sys.version)
import numpy; print("NumPy", numpy.__version__)
import scipy; print("SciPy", scipy.__version__)

import os
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier
import pandas as pd
from joblib import load
from sklearn import preprocessing

training = "./train.csv"
data_train = pd.read_csv(training)
        
y_train = data_train['# Letter'].values
X_train = data_train.drop(data_train.loc[:, 'Line':'# Letter'].columns, axis = 1)

print("Shape of the training data")
print(X_train.shape)
print(y_train.shape)
print(X_train)
        
# Data normalization (0,1)
X_train = preprocessing.normalize(X_train, norm='l2')
    
# Models training


#Linear Discrimant Analysis (Default parameters)
clf_lda = LinearDiscriminantAnalysis()
clf_lda.fit(X_train, y_train)
        
# Neural Networks multi-layer perceptron (MLP) algorithm
clf_NN = MLPClassifier(solver='adam', activation='relu', alpha=0.0001, hidden_layer_sizes=(500,), random_state=0, max_iter=1000)
clf_NN.fit(X_train, y_train)


testing = "test.csv"
data_test = pd.read_csv(testing)
        
y_test = data_test['# Letter'].values
X_test = data_test.drop(data_test.loc[:, 'Line':'# Letter'].columns, axis = 1)
   
print("Shape of the test data")
print(X_test.shape)
print(y_test.shape)
    
# Data normalization (0,1)
X_test = preprocessing.normalize(X_test, norm='l2')
    
# Models training

#LDA results
print("LDA score and classification:")
print(clf_lda.score(X_test, y_test))
print(clf_lda.predict(X_test))

#NN results
print("NN score and classification:")
print(clf_NN.score(X_test, y_test))
print(clf_NN.predict(X_test))
       
