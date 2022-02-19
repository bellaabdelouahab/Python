from math import exp
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


class Fit:
    def __init__(self,input,output) -> None:
        if len(input)!=len(output): raise ValueError("input and output should have same size")
        self.input=np.array(input)
        self.output=np.array(output)
        self.inputNrmlzer = (np.max(self.input),np.min(self.input))
        self.outputNrmlzer = (np.max(self.output),np.min(self.output))
        self.input=self.NormalizeData(np.array(input),self.inputNrmlzer)
        self.output=self.NormalizeData(np.array(output),self.outputNrmlzer)
        self.length=len(input)
        self.input_mean=np.mean(input)
        self.output_mean=np.mean(output)
        self.Qvalues=0
    def Train(self,Activation=False,degree=2,multi=True,lr=0.02):
        if not isinstance(Activation,str):   
            raise TypeError("Name of activation function should be a str \t ",type(Activation), "recived")
        if Activation=="linear":
            self.Linear()
        elif Activation=="Gradian-Distance":
            if multi:
                self.Gradian_multi(lr)
            else:
                self.Gradian(lr)
        elif Activation=="Gradian-Poly":
            print("dfsdfds")
            self.Gradian_poly(lr,degree)
        elif Activation=="Regretion-Logistique":
            self.RegretionLogistique(lr)
        else:
            print("wtf")
    def Linear(self):
        Q1=(np.mean([self.input[i]*self.output[i] for i in range(self.length)])-self.input_mean*self.output_mean)/np.var(self.input)
        Q0=self.output_mean-Q1*self.input_mean
        self.Predict=lambda x: Q0+x*Q1
    def Gradian(self,lr):
        X = np.array([[i,1] for i in self.input])
        X_=np.array([[i[0] for i in X],[i[1] for i in X]])
        Q = np.array([[10],[10]])
        Y = np.array([[i] for i in self.output])
        for i in range(1000):
            Q=Q-(np.dot(X_,(np.dot(X,Q)-Y)))*(lr/self.length)
        self.Predict=lambda x: Q[1]+x*Q[0]
    def Gradian_multi(self,lr):
        X = np.c_[np.ones((len(self.input), 1)), self.input]
        X_T=X.T
        Y = np.reshape(self.output, (len(self.output), 1))
        Q = np.random.randn(len(X[0]), 1)
        print(Q)
        for i in range(10000):
            Gradian=1/self.length*(X_T.dot(X.dot(Q)-Y))
            Q=Q-lr*Gradian
        self.Predict=lambda x:self.DeNormalizeData(Q[0]+sum([self.NormalizeData(np.array(x),self.inputNrmlzer)[i-1]*Q[i] for i in range(1,len(Q))]),self.outputNrmlzer)
        return Q
    def Gradian_poly(self,lr,degree):
        X = np.c_[np.ones((len(self.input), 1)),np.array([[j[0]**i for j in self.input] for i in range(1,degree+1)]).T]
        print("sdfsdifudsfiuhj",X)
        X_T=X.T
        Y = np.reshape(self.output, (len(self.output), 1))
        Q = np.random.randn(degree+1, 1)
        # exit()
        for i in range(1000):
            Gradian=(X_T.dot(X.dot(Q)-Y))
            Q=Q-Gradian*(lr/self.length)
        self.Predict=lambda x:self.DeNormalizeData(sum([self.NormalizeData(np.array(x),self.inputNrmlzer)**i*Q[i] for i in range(1,len(Q))]),self.outputNrmlzer)
    def RegretionLogistique(self,lr):
        Q = self.Gradian_multi(lr)
        print("==>",Q.T)
        self.Predict=lambda x:1/(1+exp(-Q.T[0][0]-sum([Q.T[0][i]*x[i-1] for i in range (1,len(Q.T[0]))])))
    def NormalizeData(self,Data,max_min):
        return (Data - max_min[1] )/ (max_min[0] - max_min[1])
    def DeNormalizeData(self,Data,max_min):
        return  (Data * (max_min[0] - max_min[1])+ max_min[1] )
import pandas as pd
dataset = pd.read_csv('./Start/banking.csv')
print(dataset)
X = np.array(dataset.iloc[:,1:2].values)
Y = np.array(dataset.iloc[:,2].values)
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=5)
X_poly = poly_reg.fit_transform(X)
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_poly,Y)
# print(lin_reg.predict(X_poly))
print(Y)
# X=[i[0] for i in X]
# Y=[i[0] for i in Y]
fit=Fit(X,Y)
fit.Train(Activation="Regretion-Logistique")#,multi=False)
Ynew=[]
print(X)
print(fit.Predict(X))
# for i in range(len(X_poly)):
#     Ynew.append(fit.Predict(np.array(X[i]))[0])
#     print(Ynew)
# from matplotlib import pyplot as plt
# plt.scatter(X,Y, color='red') 
# plt.plot(X, Ynew,color='blue')
# plt.plot(X,lin_reg.predict(X_poly),color='gold')
# plt.show()