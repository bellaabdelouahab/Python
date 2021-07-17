a=input('do you want to code or decode ?')
if a=='code' :
	a= input('write your letter : ')
	for i in range(len(a)) :
		print(bin(ord(a[i])),end='\n')
elif a=='decode' :
	a= (input('write your code :\nmake an enter between each 8 bits \nto finish enter 0\n'))
	b=(chr(int(a,2)))
	while True:
		a=input()
		if a=='0': 
			break
		b=b+(chr(int(a,2)))
	print(b)