import pandas as pd
import numpy as np
class Fit:
    def __init__(self,input,output) -> None:
        if len(input)!=len(output): raise ValueError("input and output should have same size")
        self.input=input
        self.output=output
        self.length=len(input)
        self.input_mean=np.mean(input)
        self.output_mean=np.mean(output)
    def Train(self,Activation=False,lr=0.05,start=10):
        if not isinstance(Activation,str):   
            raise TypeError("Name of activation function should be a str \t ",type(Activation), "recived")
        if Activation=="linear":
            self.Linear()
        elif Activation=="Gradian-Distance":
            self.Gradian(lr)
    def Linear(self):
        Q1=(np.mean([self.input[i]*self.output[i] for i in range(self.length)])-self.input_mean*self.output_mean)/np.var(self.input)
        Q0=self.output_mean-Q1*self.input_mean
        self.Predict=lambda x: Q0+x*Q1
    def Gradia(self,lr):
        X = np.array([[i,1] for i in self.input])
        X_=np.array([[i[0] for i in X],[i[1] for i in X]])
        Q = np.array([[10],[10]])
        Y = np.array([[i] for i in self.output])
        for i in range(1000):
            Q=Q-(np.dot(X_,(np.dot(X,Q)-Y)))*(lr/self.length)
        self.Predict=lambda x: Q[1]+x*Q[0]
    def Gradian(self,lr):
        X = np.c_[np.ones((len(self.input), 1)), self.input]
        X_T=X.T
        Y = np.reshape(self.output, (len(self.output), 1))
        Q = np.random.randn(len(X[0]), 1)
        for i in range(100):
            Gradian=(X_T.dot(X.dot(Q)-Y))
            Q=Q-Gradian*(lr/self.length)
        self.Predict=lambda x: sum([x*Q[i] for i in range(len(Q))])
db= pd.read_csv("C:/Users/Abdelouahab/Downloads/archive/National_Stock_Exchange_of_India_Ltd.csv")
p=db.iloc[:,3:7].values
Data=[]
for i in p:
    Data.append([float(w.replace(",","")) if type(w) is str else w for w in i ])
# print(Data)
fit=Fit([[i[j] for j in range(len(i)-1)] for i in Data],[i[3] for i in Data])
fit.Train(Activation="Gradian-Distance")
print(fit.Predict([375,377.4,-22.7]))