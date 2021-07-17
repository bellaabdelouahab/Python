d=[]
for a in range(2,51):
	x=0
	for i in range(2,(a//2)+1) :
		if a%i==0:
			x=1
			break	
	if x==0:
		d.append(a)
c=' '.join(map(str,d))
print(c)
f=open('test.txt','w')
f.write(c)
f.close()

		
