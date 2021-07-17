a=input("donnez une chaine : ")
def voyelle(a):
	x1=0
	for x in range(len(a)):
		if a[x]=='a' or a[x]=='i' or a[x]=='e' or a[x]=='o' or a[x]=='u' :
			x1+=1
	return x1
print("le nomber de voyelle est :",voyelle(a))