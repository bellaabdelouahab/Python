from math import sin,log
print ("la fonction : f(x)=sin(x)+ln(x)-x**(0.5)")
a=int(input("donnez le max valeue de la fonction :"))
b=int(input("donnez le min valeue de la fonction :"))
while a<b:
	a=int(input("donnez le max valeue de la fonction :"))
	b=int(input("donnez le min valeue de la fonction :"))
def calculs(a,b):
	e=2.718281
	for i in range(b,a):
		print(sin(i)+log(e,i)+i**0.5)
	return 0
calculs(a,b)