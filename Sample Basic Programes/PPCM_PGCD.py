a=int(input('donnez le 1er nomber :'))
b=int(input('donnez le 2eme nomber :'))
d=b
if a<b :
	a,b=b,a
if b==0:
    print("le PGCD est ",a)
else :

    while b!=0:
    	t=b;n=a%b;b=n;
print("\n le PGCD est",t)
q=a*d/t
print("\n le PPCM est",int(q))
