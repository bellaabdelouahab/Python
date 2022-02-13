def newton(fonction,derivee,a,e):
    delta = 1
    while delta > e:
        x = -fonction(a)/derivee(a) + a
        delta = abs(x - a)
        a = x
    return x , delta
        
        
def secont(function,a,b,e):
    delta = 1
    while delta>e:
        print(a,b)
        x=-(function(a)*(a-b))/(function(a)-function(b))+a
        delta=abs(x-a)
        b=a
        a=x
    return x,delta
        

print( newton(lambda x: 3*x-9 , lambda x: 3 , 0 , 0.001) )
print( secont(lambda x: 3*x-9 , 10 ,-5, 0.001) )
    

