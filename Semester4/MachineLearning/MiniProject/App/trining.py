from black import Mode
import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier

def Main():
    # import Data
    # import os
    # print(os.getcwd())
    VoiceDataSet = pd.read_csv("C:/Git-hub/Python/Semester4/MachineLearning/MiniProject/App/voice.csv")
    #Print head
    print(VoiceDataSet.head(5))
    #nbr of clumns
    print(VoiceDataSet.columns)
    
    print(VoiceDataSet.shape)
    # counting values male and female
    print(VoiceDataSet["label"].value_counts())
    #show the Relations between attributes
    correlation = VoiceDataSet.corr()
    
    sns.heatmap(correlation)
    
    plt.show()
    
    X_ = VoiceDataSet.drop(['label'], axis=1)

    Y_ = VoiceDataSet['label']
    
    X_train , X_test , y_train , y_test = train_test_split(X_,Y_, test_size=0.25)
    
    Model = RandomForestClassifier(random_state=0)
    
    Model.fit(X_train,y_train)
    
    print(Model.score(X_test,y_test))
