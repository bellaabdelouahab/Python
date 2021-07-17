from pickle import*
f=open('hey.txt','wb')
def fe(x):
    return x**5+3*x**3+1
dump(fe,f)
dump([0,1,2,3],f)
f.close()
with open('hey.txt','rb') as fich:
    f=load(fich)
    l=load(fich)
    print(list(map(f,l)))