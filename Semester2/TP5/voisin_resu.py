A =	[[0,1,1,1,0,0,0,0],[1,0,1,0,1,0,0,0],[1,1,0,1,1,0,0,0],[1,0,1,0,1,0,1,1],[0,1,1,1,0,1,1,0],[0,0,0,0,1,0,1,1],[0,0,0,1,1,1,0,1],[0,0,0,1,0,1,1,0]]
for a in A:print(a,'\n')
petite        = lambda l,x  : sum([1 for i in range(len(l)) if l[i]<x])
grand         = lambda l,x  : sum([1 for i in range(len(l)) if l[i]>x])
midian        = lambda l    : [l[i] for i in range(len(l)) if grand(l,l[i])<=(len(l)/2) and petite(l,l[i])<=(len(l)/2)]
voisin        = lambda i,j,a: a[i][j]==1
list_voisin   = lambda i,a  : [j for j in range(len(a)) if a[i][j]]
degre         = lambda i,a  : sum([1 for j in range(len(a)) if a[i][j]])
list_deger    = lambda a    : [(i,degre(i,a))for i in range(len(a))]
tri_deger     = lambda c    : [sorted([c[i][::-1] for i in range(len(c))])[i][::-1] for i in range(len(c))][::-1]
tri_ville     = lambda c    : [x for x,y in c ]
chemin_valide = lambda c, a : len(c)>2 and True in [a[c[i]][c[i+1]]==1 for i in range(len(c)-1)]
chemin_simple = lambda c, a : True not  in [c[i]==c[j] for i in range(len(c)) for j in range(len(c)) if i!=j]
c=tuple(map(int,(input("give a tuple \n nb:\n 0<=T[i]<=7\n tuple must containe at least two values \n -->")).split(' ')))
print('le grand est  : ',grand([25,12,6,17,3,10,20,12,15,38],20),"\n",\
	  'le petite est :',petite([25,12,6,17,3,10,20,12,15,38],20),"\n",\
	  'les midians sont :',midian([25,12,6,17,3,10,20,12,15,38]),"\n",\
	  '3 est voisin de 1 :',voisin(3,1,A),"\n",\
	  'list des voisin de 3 :',list_voisin(3,A),"\n",\
	  'le nombre de villes voisines à la ville  3 :',degre(3,A),"\n",\
	  'list des voisin et sont degre :',list_deger(A),"\n",\
	  'tri de les villes apartire de sont degre :',tri_deger(list_deger(A)),"\n",\
	  "liste des villes triées dans l ordre décroissant des degrés des villes : ",tri_ville(tri_deger(list_deger(A))),"\n",\
	  'Deux villes consécutives dans T sont voisines : ',chemin_valide(c,A),"\n",\
	  'T est un chemin qui passe une seule fois par la même ville : ',chemin_simple(c,A))