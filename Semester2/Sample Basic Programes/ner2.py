from random import randint
c=0
for i in range (0,10):
	a=randint(1,6)
	b=randint(1,6)
	print(a)
	print(b)
	if a==b:
		c=c+1
		print('win')
	else:
		print('lose')


print("wnning percentage",(c/10)*100)



