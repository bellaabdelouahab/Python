a=int(input('donnnez une nomber :'))
for x in range(0,10):
	if a//(10**x)==0 :
		break
b=0
x=x-1
while a!=0:
	b=b+(a%10)*(10**x)
	a=a//10
	x=x-1
print(b)
