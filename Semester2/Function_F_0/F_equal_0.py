from sympy import var
from sympy import sympify
a = input('Enter Your function where "x" is the variable\n F(x)= ')
enterval_A=eval(input('enter a and b ([a,b])\na='))
enterval_B=eval(input('b='))
acuracy=int(input('how mush acurate you want 0-100 :'))
variavle_=var('x')
expr= sympify(a)
#expr.subs(variavle_,value...)  
def fun(a,b,acu):
    '''if acu==0 :
        print('noooooooo')
        return a
    if expr.subs(variavle_,a)*expr.subs(variavle_,b)<0:
        return fun(a,(a+b)/2,acu-1)
    else:
        return fun((a+b)/2,b,acu-1)'''
    while not -1<expr.subs(variavle_,(a+b)/2)<1:
        if expr.subs(variavle_,a)*expr.subs(variavle_,b)<0:
            b=(a+b)/2
        else:
            a=(a+b)/2
        acu=acu-1
        print(acu)
        if acu==0:
            print('=====>',a,b,(a+b)/2)
            break
print(10**(acuracy%6))
print(fun(enterval_A,enterval_B,5000))
