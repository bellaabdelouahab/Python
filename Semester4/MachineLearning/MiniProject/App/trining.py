from black import Mode
import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier


def NormalizeData(Data,Max,Min):
        return (Data - Min )/ (Max - Min)


def Main():
    # import Data
    # import os
    # print(os.getcwd())
    VoiceDataSet = pd.read_excel("C:/Users/Abdelouahab/Documents/M&M/gendervoice.xlsx")
    VoiceDataSet = VoiceDataSet.drop(['Unnamed: 0'], axis=1)
    # VoiceDataSet = VoiceDataSet[VoiceDataSet["10"] != "other"]
    #Print head
    # print(VoiceDataSet.head(5))
    #nbr of clumns
    print(VoiceDataSet.columns)
    
    print(VoiceDataSet.shape)
    # counting values male and female
    

    VoiceDataSet=VoiceDataSet.sort_values(by=['Label'])
    # counting values male and female
    # VoiceDataSet = VoiceDataSet[0:1164]
    print(VoiceDataSet["Label"].value_counts())
    #show the Relations between attributes
    
    
    X_ = VoiceDataSet.drop(['Label'], axis=1)
    import numpy as np
    Xnorm=np.zeros(len(X_))
    for i in range(9):
        X_[X_.columns[i]] = NormalizeData(X_[X_.columns[i]],max(X_[X_.columns[i]]),min(X_[X_.columns[i]]))
    print(X_.info())
    correlation = X_.corr()
    
    sns.heatmap(correlation)
    
    plt.show()
    Y_ = VoiceDataSet['Label']
    
    X_train , X_test , y_train , y_test = train_test_split(X_,Y_, test_size=0.25)
    
    Model = RandomForestClassifier(random_state=0)
    
    Model.fit(X_train,y_train)
    # print(X_test)
    print(Model.score(X_test,y_test))
Main()