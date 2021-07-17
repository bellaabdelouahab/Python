a=int (input("entrer un nombre \nNB: numbre>2\n"))
while a<2 :
	a=int (input("entrer un nombre \nNB: numbre>2\n"))
x=0
for i in range(2,(a//2)+1) :
	if a%i==0:
		print('pas premier')
		x=1
		break	
if x==0:
	print('premier')

for n in range(1,101):
	x=0
	for i in range(2,(n//2)+1) :
		if n%i==0:
			x=1	
	if x==0 :
		print(n)