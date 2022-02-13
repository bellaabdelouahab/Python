from pickle import*
def identiques(a,b):
    return a.readlines()==b.readlines()
def fusion_fichiers(a,b):
    c=open('test3.txt','w')
    c.write(''.join(a.readlines())+''.join(b.readlines()))
    c.close()
def RecupererMatrice(c):
    ch=open(c,'r')
    b=[]
    for i in ch:
        b.append(i.rstrip().split(' '))
    print(' the list is :\n',b)
    ch.close()
    return(b)
def TransposeMatrice(c):
    b=RecupererMatrice(c)
    newmat=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    print(newmat)
    for i in range(9):
        for j in range(3):
            newmat[i][j]=b[j][i]
    print(newmat)
def saisir_un_etudiant():
    print('working')
    ch= open('concours.dat','ab')
    dicte={}
    dicte['CIN']=input("donne le CIN:")
    dicte['NOM']=input("donne le NOM:")
    dicte['PRENOM']=input("donner le PRENOM :")
    dicte['AGE']=input("donne l'AGE :")
    x=(input("donne les 3 notes enter 0 et 20:").split(' '))
    y=[int(x[i]) for i in range(len(x))]
    print(y)
    while len(y)!=3 or (False in [0<=y[i]and y[i] <=20 for i in range(len(y))]):
        x=(input("donne soulement 3 notes enter 0 et 20!!!!!:").split(' '))
        y=[int(x[i]) for i in range(len(x))]
    dicte['NOTE']=y
    dicte['moyG']=sum(dicte['NOTE'])/len(dicte['NOTE'])
    if dicte['moyG']>=12:
        dicte['decision']='admis'
    elif 6<=dicte['moyG']<12:
        dicte['decision']='refuse'
    else :
        dicte['decision']='ajourne'
    dump(dicte,ch)
    ch.close()
def saisir(n):
    for i in range(n):
        print('----- Condidat n°  ',i+1)
        saisir_un_etudiant()
def recherche_par_decision(decision):
    ch=open('concours.dat','rb')
    c=[]
    while True:
        try:
            b=load(ch)
            if b['decision']==decision:
                c.append(b)
        except EOFError:
            print(c)
            return c
def admis():
    ch=open('admis.txt' ,'w')
    c.sort(key=lambda x:x['moyG'],reverse=True)
    for i in range(len(c)):
        ch.write(str(i+1)+' '+str(c[i]['NOM'])+' ')
        ch.write(str(c[i]['PRENOM'])+' ')
        ch.write(str(format(c[i]['moyG'], '.2f'))+'\n')
a,b=open('test1.txt','w'),open('test2.txt','w')
b.write('hello ')
a.write('1 2 3 4 5 6 7 8 9\n9 8 7 6 5 4 3 2 1\n1 5 9 7 5 3 2 6 9')
a.close()
b.close()
a=open('test1.txt','r')
b=open('test2.txt','r')
print(identiques(a,b))
a.close()
b.close()
a=open('test1.txt','r')
b=open('test2.txt','r')
fusion_fichiers(b,a)
a.close()
b.close()
RecupererMatrice('test1.txt')
TransposeMatrice('test1.txt')
n=input('donnez le nomber des etudiant :')
saisir(n)
n=input("donne le decision :")
while n!='admis'or n!='refuse' or n!='ajourne':
    n=input("donne une valide le decision :")
c=recherche_par_decision(n)
admis()
