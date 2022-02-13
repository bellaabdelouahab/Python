import matplotlib.pyplot as plt
import numpy as np
''''a=np.linspace(0,np.pi,50)
b = np.cos(a)**2
c=(np.cos(a+1e-10)**2-np.cos(a)**2)/1e-10
plt.figure(figsize=(10,5))
plt.plot(a,b,label='name',ls=':',c='blue')
plt.scatter(a,c,label='nname',ls='-.',c='red')
plt.legend()
plt.xlabel("hello")
plt.ylabel('hey')
plt.title("nothing")
plt.show()'''
############################################
'''x=np.linspace(0,3,10)
m=np.arange(-4,0)
    for i in m:
        c=np.exp(i*x)
        plt.subplot(3,3)
        plt.bar(x,c)
plt.show()'''
############################################
'''from mpl_toolkits.mplot3d import Axes3D
w=np.random.randn(300,300)
ax=plt.axes(projection='3d')
ax.scatter(w[:,0],w[:,1],w[:,2])
plt.show()'''
############################################
'''from mpl_toolkits.mplot3d import Axes3D
def f(x,y):
    return np.sin(x)+np.cos(x+y)
x=np.linspace(0,5,10)
y=np.linspace(0,5,10)
x,y=np.meshgrid(x,y)
z=f(x,y)
ax=plt.axes(projection='3d')
ax.plot_surface(x,y,z,cmap='plasma')
plt.show()'''
############################################
'''img=plt.imread('IMG_20201109_171018.jpg')
plt.figure(figsize=(3,5))
print(img)
plt.imshow(img)
plt.show()'''
############################################
'''x=np.array(['java','python','php','javascript','c#','c++'])
m=np.array([22.2,17.6,8.8,8.7,7.7,6.7])
plt.bar(x,m)
plt.show()'''
############################################
'''t=np.linspace(0,2*np.pi,50)
def f(t):
    return np.sin(t)/(1+np.sin(t)**2)
x=f(t)
y=x*np.cos(t)
plt.plot(x,y)
plt.show()'''
#####################################################
'''from scipy.integrate import odeint
t=np.linspace(0,50,200)
f= lambda t,y : 3*y + 2*t
g= lambda t,y : np.sin(t)*np.sin(y)
sol = odeint(g,2,t)
plt.plot(t,sol)
plt.show()'''
############################################
from mpl_toolkits.mplot3d import Axes3D
def f(x,y):
    return np.sin((x**2+y**2)**0.5)
x=np.linspace(-5,5,1000)
y=np.linspace(-5,5,1000)
x,y=np.meshgrid(x,y)
z=f(x,y)
ax=plt.axes(projection='3d')
ax.plot_surface(x,y,z,cmap='plasma')
plt.show()