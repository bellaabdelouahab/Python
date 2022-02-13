import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(-10,10,30)
z=np.exp(x/4)

'''
plt.figure(figsize=(8,6))
plt.plot(x,x,c='blue',label='y=x')
plt.plot(x,x**2,ls='--',c='red',label='y=x^2')
plt.plot(x,2*x-1,c='green',label='affine')
#plt.scatter(x,x**3,lw=4,c='black',label="y=x^3")
plt.title("polynômes")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# une autre figure
plt.figure()
plt.plot(x,3*x+2,lw=0.5,ls='-.',label='fuck')

plt.legend()
plt.show()'''


x=np.linspace(0,3,20)
'''
plt.figure(figsize=(8,6))
for m in range(-4,0):
    plt.plot(x,np.exp(m*x),label='y=e^({}*x)'.format(m))
plt.title("$e^{m*x}$")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


'''



'''def graphique(data):
    n=len(data)
    plt.figure(figsize=(10,6))
    for i in range(n):
        plt.subplot(n,1,i+1)
        plt.plot(data["experience"+str(i)])
        plt.title("experience"+str(i))
    plt.show()'''


'''dataset={}
for i in range(1):
    dataset["experience"+str(i)]=np.random.randn(100)

graphique(dataset)
'''



'''z=np.random.randn(30,2)
plt.hist2d(z[:,0],z[:,1],cmap='Reds',bins=50)
plt.xlabel('z0')
plt.ylabel('z1')
plt.title('hist 2D')
plt.colorbar()'''

'''x=np.random.randn(20,1)
y=np.random.randn(20,1)
plt.hist(x,bins=8)
plt.hist(y,bins=3)'''




def F(x,y):
    return np.sin(x)+np.cos(x+y)

x=np.linspace(0,5,10000)
y=np.linspace(0,5,10000)
x=x.astype("i")
y=y.astype("i")
X,Y=np.meshgrid(x,y)
Z=F(X,Y)
ax=plt.axes(projection='3d')
ax.plot_surface(X,Y,Z,cmap='plasma')



plt.show()