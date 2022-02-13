#partie I
reseau  = [ 8,[ [0,1], [1,3], [3,2], [2,0], [0,3], [2,1], [4,5],[5,7], [7,6], [6,4], [7,4], [6,5], [2,4], [5,3] ]]
reseauA = [ 5,[ [0,1], [2,0], [0,3], [2,1], [3,2] ]]
reseauB = [ 5,[ [0,1], [1,2], [2,3], [3,4], [4,2], [3,1] ]]
def creerReseauVide(n):
	return [n,[]]
def estUnLienEntre(paire,i,j):
	return ((i in paire) and (j in paire))
def sontAmis(reseau,i,j):
	return [i,j] in reseau[1] or [j,i] in reseau[1]
def declareAmis(reseau,i,j):
	return reseau[1]+[[i,j] for x in range(1) if not sontAmis(reseau,i,j)]
def listeDesAmisDe(reseau,i):
	return [[x,y] for x,y in reseau[1] if i==x or i==y]
print(listeDesAmisDe(reseau,7))
filiale = [6, 9, 3, 3, 3, 5, 5, 5, 1, 9, 10, 1, 4, 9, 11, 9]
filialeA = [6,1,1,3,4,5,1,5,5,7]
filialeB = [3,9,0,3,9,4,4,7,1,9]
#partie II
def creerPartitionEnSingletons(n):
	return [i for i in range(n)]
def representantI(parent,i):
	if parent[i]==i:
		return i 
	else :
		return representantI(parent,parent[i])
def representantII(parent,i):
	t=[]
	while parent[i]!=i:
		t+=[i]
		i=parent[i]
	for j in  t:
		parent[j]=i
	return parent
def fusion(parent,i,j):
	if parent[i]==i and parent[j]==j:
		parent[j]=i 
	else :
		print("i or j is not a parent")
	return parent
def listeDesGroupes(parent):
	for i in range(len(parent)):
		representant(parent,i)
	return [[i for i in range(len(parent)) if parent[i]==j]for j in [i for i in range(len(parent))if parent[i]==i]]
#partie III
from random import randint
def coupeMinimumRandomisee(reseau):
	parent=creerPartitionEnSingletons(reseau[0])
	i=0
	while True:
		t=[randint(0,reseau[0]),randint(0,reseau[0])]
		if sontAmis(reseau,t[0],t[1])and representantI(parent,t[0])==t[0]and representantI(parent,t[1])==t[1]:
			parent[t[0]]=t[1]
			reseau[1].pop(t[0])
		if i==50:
			break;
		i+=1
	return parent
print(coupeMinimumRandomisee(reseau))
