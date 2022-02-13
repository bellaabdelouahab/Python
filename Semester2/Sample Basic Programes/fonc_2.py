a=float(input("donnez le 1er  nomber : "))
b=float(input("donnez le 2eme nomber : "))
c=float(input("donnez le 3eme nomber : "))
d=float(input("donnez le 4eme nomber : "))
def MAXI(a,b,c,d):
	if a>b and a>c and a>d :
		return a
	if b>a and b>c and b>d :
		return b
	if c>b and c>a and c>d :
		return c
	if d>b and d>c and d>c :
		return d
def MINI(a,b,c,d):
	if not(a>b and a>c and a>d ):
		return a
	if not(b>a and b>c and b>d ):
		return b
	if not(c>b and c>a and c>d ):
		return c
	if not(d>b and d>c and d>c ):
		return d 
print (f"le max est {MAXI(a,b,c,d)}")
print (f"le min est {MINI(a,b,c,d)}")