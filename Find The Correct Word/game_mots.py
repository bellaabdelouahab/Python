from random import randint
from copy import copy
with open('mots.txt','r') as f:
    a=[i.rstrip() for i in f]
    word= list(a[randint(0,len(a)-1)])
    answer=''.join(copy(word))
    n=len(word)
    def game(word,n):
        x=randint(0,len(word)-1)
        b=[]
        for i in range(len(word)):
            if i!=x:
                b.append('-')
            else:
                b.append(word[i])
                word[i]=' '
        c=n
        while True:
            a=' '
            print(''.join(b),'\n You have ',c,'more chances')
            while a==' ':
                a=input("insert a letter: ").upper()
            if a in word :
                b[word.index(a)]=a
                word[word.index(a)]=' '
            else:
                print('Try again\n')
                c-=1
            if(c==0)and ('-' in b):
                return False
            elif '-' not in b:
                return True
        return True
    if(game(word,n)):
        print('The word is :',answer)
        print('You won')
    else:
        print('You lost')
        print('The word is :',answer)