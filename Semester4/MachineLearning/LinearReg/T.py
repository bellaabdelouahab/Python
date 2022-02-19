import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('Position_Salaries.csv')
# print(dataset)

X = dataset.iloc[:,1:2].values  
y = dataset.iloc[:,2].values
print(y)