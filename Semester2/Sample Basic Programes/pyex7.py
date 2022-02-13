

def rech(a,b):
	res = False 
	c=len(a)//2
	pr = b
	while pr >= 1  :
		if b == a[c]:
			res  = True
			break
		else:
			if b < a[c]:
				pr = pr -1
				c = c -pr
			else:
				pr = pr -1
				c = c + pr

	return res 

a=[-4,1,3,5,6,7,8,10,13,14]
b= int(input("donnez nbr"))
print(rech(a,b))
c=int (input ("donnez une nomber:"))
c=abs(c)
if c>10:
	c=c%10
print(a[c])