import numpy as np
print(np.array([5,9,1,3]))
print(np.linspace(28, 12,9))
a=np.arange(1,50)
print(a[a%2==0]*2)
b=np.array(['f','m','f','m'])
b=np.where(b=='f',1,0)
print(b)
print(np.concatenate((a, b), axis=0))
print(b+500)
