from random import randint,shuffle
T=[]
def add_questions(n):
    for i in range(n):
        Qcm=dict()
        a=(randint(0,500))
        b=(randint(0,500))
        Qcm.update({str(i)+'question':str(a)+'+'+str(b)+'?','r_answer':a+b,'w_answer':[a+b+i-randint(-100,100)for i in range(3)]})
        T.append(Qcm)
    return T

def show_Qcm(a):
    t=[str(a['r_answer']),str(a['w_answer'][0]),str(a['w_answer'][1]),str(a['w_answer'][2])]
    shuffle(t)
    b=int(input('the question: \n'+a['question']+'\n'+t[0]+'\n'+t[1]+'\n'+t[2]+'\n'+t[3]+'\n'))
    if(a['r_answer']==b):
        print('Good\n+1')
        return +1
    elif(b in a['w_answer']):
        print("Too bad\n-1")
        return -1
    else:
        print("you've made a mistake !!!!\n try again")
        return (show_Qcm(a))
a=int(input('how many Questions you want to answer :'))
add_questions(a)
x=0

for i in range(len(T)):
    x+=show_Qcm(T[i])
print("Your score is :",x/a*100)