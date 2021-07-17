a=int (input("entrer un nombre \nNB: numbre>2\n"))
while a<2 :
	a=int (input("entrer un nombre \nNB: numbre>2\n"))
x=a
s=1
print(a,"= 1",end="")
for i in range(a//2+1,1,-1):
	if x%i==0 :
		print(" +",i,end="")
		s+=i
print(' =',s)
if a!=s :
	print("se nomber n est pas parfiat !")
else :
	print("se nomber est parfait !")
for b in range(3,100):
	x=b
	s=1
	for i in range(b//2+1,1,-1):
		if x%i==0 :
			s+=i
	if b==s :
		print(b)