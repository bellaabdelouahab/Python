
import numpy as np #don't worry it's just to easy multiple all the elements of a list 
pointsnumber= int(input("how many point you want to enter : "))
x=[]
y=[]
#get all the point x and y
for _ in range(pointsnumber):
    print(f'Enter The point number {_}:')
    x.append(float(input(f'x{_} = ')))
    y.append(float(input(f'y{_} = ')))
#get the point that we want to calculate its y   
xp = float(input('Enter calculation point xp: '))
# Calculating interpolated value
resualt=0
for i in range(pointsnumber):
    resualt+=y[i]\
            *np.prod([xp-x[j] for j in range(pointsnumber-1) if j!=i])\
            /np.prod([x[i]-x[j] for j in range(pointsnumber-1) if j!=i])
print(resualt)
