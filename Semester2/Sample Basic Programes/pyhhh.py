from random import randint
def devi(n):
	l=[randint(0,20)]
	i=0
	while i<n:
		a=randint(0,20)
		print(a)
		if a>l[i]:
			l=l+[a]
			i+=1
	'''for i in  range (len(l)):
					for n in range(len(l)):
						if l[i]>l[n] :
							l[i],l[n]=l[n],l[i]'''
	return l
n=devi(int(input("donnez un nomber :")) )
print(n)
