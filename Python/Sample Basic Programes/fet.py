a=[10,1,2,3,4,5,6,67,7,7,56,34,2,45,7,9,5,3,2]
m=max(a)
b=[0]*(m+1)
s=0
for x in range(len(b)):
	s=0
	for i in range(len(a)):
		if x==a[i]:
			s+=1
	b[x]=s
l=[]
for i in range(m+1):
	l=l+[i]*b[i]
print(l)