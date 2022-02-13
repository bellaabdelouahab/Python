class voi:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def counte(self):
        return (self.x**2+self.y**2)**0.5
v1=voi(3,-1)
print(v1.counte())
class chat:
    def __init__(self,nom,age):
        self.name=nom
        self.ages=age
    def get_age(self):
        return self.ages
    def Parle(self):
        return "Moew"
v2=chat('bisbis',2)
print(v2.get_age(),'\n',v2.Parle())
class rec:
    def __init__(self):
        self.long=int(input("donnez la longeur"))
        self.larg=eval(input("donnez la largeur"))
    def per(self):
        return (self.long + self.larg)*2
    def Aire(self):
        return self.long*self.larg
    def estcarre(self):
        if (self.larg==self.long):
            print("oui est carre")
    def affi(self):
        print('ceci est in rectangle de demontion ',self.larg,'*',self.long)
v3=rec()
print(v3.per())
v3.affi()
print(v3.Aire())
v3.estcarre()