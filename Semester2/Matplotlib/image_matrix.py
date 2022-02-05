from random import randint
import matplotlib.pyplot as plt
def img(n):
	return [[randint(0,1) for i in range(n)] for j in range(n)]
n=int(input("donnez le nomber"))
t=img(n)
'''for i in range(n):
	print(t[i],end="\n")'''
plt.imshow(t)
olt.show()