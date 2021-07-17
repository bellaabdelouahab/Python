from loguru import logger
@logger.catch
def clac(a,b):
    if(b!=0):
        c=-b/a
        print("x=",c)
    else:
    	print("x=",c)
a=int(input("Enter a."))
b=int(input("Enter b."))
c=0
clac(a,b)
