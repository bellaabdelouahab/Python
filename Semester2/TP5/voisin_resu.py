a=	[[0,1,1,1,0,0,0,0],[1,0,1,0,1,0,0,0],[1,1,0,1,1,0,0,0],[1,0,1,0,1,0,1,1],
	[0,1,1,1,0,1,1,0],[0,0,0,0,1,0,1,1],[0,0,0,1,1,1,0,1],[0,0,0,1,0,1,1,0]]
for i in range(len(a)):print(a[i],'\n')
def petite(l,x):
	return sum([1 for i in range(len(l)) if l[i]<x])
def grand(l,x):
	return sum([1 for i in range(len(l)) if l[i]>x])
def midian(l):
	return [l[i] for i in range(len(l)) if grand(l,l[i])<=(len(l)/2) and petite(l,l[i])<=(len(l)/2)]
def voisin(i,j,a):
	return a[i][j]==1
def list_voisin(i,a):
	return [j for j in range(len(a)) if a[i][j]]
def degre(i,a):
	return sum([1 for j in range(len(a)) if a[i][j]])
def list_deger(a):
	return [(i,degre(i,a))for i in range(len(a))]
def tri_deger(c):#I could'nt make it in one line . nver mind i did it :)
	return [sorted([c[i][::-1] for i in range(len(c))])[i][::-1] for i in range(len(c))][::-1]
def tri_ville(c):
	return [x for x,y in c ]
def chemin_valide(c, a):
    return len(c)>2 and True in [a[c[i]][c[i+1]]==1 for i in range(len(c)-1)]
def chemin_simple(c,a):
    return True not  in [c[i]==c[j] for i in range(len(c)) for j in range(len(c)) if i!=j]
print('le grand est : ',grand([25,12,6,17,3,10,20,12,15,38],20))
print('le petite est :',petite([25,12,6,17,3,10,20,12,15,38],20))
print('les midians sont :',midian([25,12,6,17,3,10,20,12,15,38]))
print('3 est voisin de 1 :',voisin(3,1,a))
print('list des voisin de 3 :',list_voisin(3,a))
print('le nombre de villes voisines à la ville  3 :',degre(3,a))
print('list des voisin et sont degre :',list_deger(a))
print('tri de les villes apartire de sont degre :',tri_deger(list_deger(a)))
print("liste des villes triées dans l ordre décroissant des degrés des villes",tri_ville(tri_deger(list_deger(a))))
c=tuple(map(int,(input("give a tuple \n nb:\n 0<=T[i]<=7\n tuple must containe at least two values \n -->")).split(' ')))
print('Deux villes consécutives dans T sont voisines : ',chemin_valide(c,a))
print('T est un chemin qui passe une seule fois par la même ville',chemin_simple(c,a))
t=[1,2,9,3,4,5,6]
print(not sorted(t))