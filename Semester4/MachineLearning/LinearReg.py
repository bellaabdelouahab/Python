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
    def Train(self,Activation=False,multi=True,lr=0.02):
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
            self.Gradian_poly(lr)
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
        for i in range(100):
            Gradian=1/self.length*(X_T.dot(X.dot(Q)-Y))
            # print(Gradian)
            Q=Q-lr*Gradian
        self.Predict=lambda x:self.DeNormalizeData(\
                            Q[0] +sum([self.NormalizeData(x,self.inputNrmlzer)[i-1]*Q[i]\
                            for i in range(1,len(Q))]),self.outputNrmlzer)
    def Gradian_poly(self,lr):
        degree=10
        X = np.c_[np.ones((len(self.input), 1)),np.array([[j[0]**i for j in self.input] for i in range(1,degree+1)]).T]
        X_T=X.T
        Y = np.reshape(self.output, (len(self.output), 1))
        Q = np.random.randn(degree+1, 1)
        # exit()
        for i in range(1000):
            Gradian=(X_T.dot(X.dot(Q)-Y))
            # print(Q)
            Q=Q-Gradian*(lr/self.length)
        self.Predict=lambda x : Q[0] +sum([Q[i]*x**i for i in range(1,len(Q))])
    def NormalizeData(self,Data,max_min):
        return (Data - max_min[1] )/ (max_min[0] - max_min[1])
    def DeNormalizeData(self,Data,max_min):
        return  (Data * (max_min[0] - max_min[1])+ max_min[1] )
# X = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
import pandas as pd
dataset = pd.read_csv('Position_Salaries.csv')
# print(dataset)

X = np.array(dataset.iloc[:,1:2].values)
Y = np.array(dataset.iloc[:,2].values)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=3)
X_poly = poly_reg.fit_transform(X)
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_poly,Y)
# print(lin_reg.predict(X_poly))
def NormalizeDatax(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))
def NormalizeData(data,max_,min_):
    return (data - min_ )/ (max_ - min_)
def DeNormalizeData(data,max_,min_):
    return  (data * (max_ - min_)+ min_ )
X_poly = NormalizeDatax(X_poly)
Ymax = 1000000
Ymin = 450000
print(Ymax,Ymin)
# print(Y)
Y_poly = np.array(NormalizeData(Y,Ymax,Ymin))
# print(Y_poly)
# Y_poly = DeNormalizeData(Y_poly,Ymax,Ymin)
# print(Y_poly)
fit=Fit(X_poly,Y_poly)
fit.Train(Activation="Gradian-Distance")#,multi=False)
Ynew=[]
for i in range(len(X_poly)):
    print(X_poly[i],Y_poly[i])
    Ynew.append(fit.Predict(np.array(X_poly[i]))[0])
print(Ynew)
Y=DeNormalizeData(np.array(Ynew),Ymax,Ymin)
print(Y)
testinput=[[1,2],[3,4],[5,6],[7,8],[9,10]]
testoutput=[500,400,300,200,100]
# testinput=[1,2,4,5]
# testoutput=[9,8,7,6]
from matplotlib import pyplot as plt
# plt.scatter(X,Y, color='red')
# def NormalizeData(data):
#     return (data - np.min(data)) / (np.max(data) - np.min(data))
# def DeNormalizeData(data):
#     return (data  * (np.max(data) - np.min(data))- np.min(data))
# X_poly = np.array(NormalizeData(X_poly))
# Y = np.array(NormalizeData(Y))
# fit=Fit(testinput,testoutput)
# fit.Train(Activation="Gradian-Distance")#,multi=False)
# print(fit.Predict(np.array(testinput)[0]))

# print(fit.Predict(1))
# plt.plot(X, fit.Predict(X_poly),color='blue')
# plt.show()


