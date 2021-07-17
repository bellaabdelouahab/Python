age=int(input("enter age ,"))
gender=str(input("enter gender:man/woman"))
if((gender=='man' and age >=20) or (gender=='woman' and (age<=35 and age>=18))):
	print("billes payment required")
else:	
	print("payment not required")	