a=int(input('give the numbers that you want to calculate thier moyene:\nNB:to finish enter 0\nnumber 1 :'))
x=0
i=2
while a!=0 :
	x+=a
	a=int(input(f'number {i} :'))
	i+=1
print('le moyenne est :',x/(i-2))