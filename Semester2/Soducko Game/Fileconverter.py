from tkinter import Tk,Label,Entry,Button
from pickle import load,dump
from pandas import read_csv,DataFrame,ExcelWriter
wind=Tk()
wind.title("Traitment des fichier")
def codeI():
    n=(a.get())
    x=(b.get())
    c_=[]
    try:
        with open('output.dat','rb') as ch:
            while True:
                try:
                    b_=load(ch)
                    c_.append(list(b_))
                except EOFError:
                    break
    except FileNotFoundError:
        c_=[]
    if [x] in c_:
        lebt=Label(wind,text="Votre fichier a n'ete traite")
        lebt.grid(row=3,column=1)
    else:
        print(c_)
        try:
            dict_from_csv =read_csv(x,squeeze=True,delimiter=';').to_dict()
            t=list(dict_from_csv)
            if n!='':
                c=[t[i] for i in list(map(int,n.split('-')))]
                for i in t:
                    if(i not in c):
                        c.append(i)
                print(c)
                dict_from_csv = {k : dict_from_csv[k] for k in c}
                print(dict_from_csv)
            df = DataFrame(data=dict_from_csv)
            writer = ExcelWriter('output.xlsx')
            df.to_excel(writer)
            writer.save()
            dictionary = {x:dict_from_csv}
            with open('output.dat','wb') as ch:
                dump(dictionary,ch )
            lebt=Label(wind,text="Votre fichier a ete traite avec succes")
            lebt.grid(row=3,column=1) 
        except FileNotFoundError:
            lebt=Label(wind,text="file not found")
            lebt.grid(row=3,column=1) 
wind.geometry("400x400")
Labelmsg=Label(wind,text="donnez le nome")
Labelmsg.grid(row=0,column=0)
b= Entry(wind)
b.grid(row=0,column=1)
Labelmsg=Label(wind,text="donnez l'order")
Labelmsg.grid(row=1,column=0)
a= Entry(wind)
a.grid(row=1,column=1)
btn=Button(wind,text="Traiter",command=codeI)
btn.grid(row=2,column=1)
lebt=Label(wind,text="Example d'order: 4-5-9-7-6-3")
lebt.grid(row=4,column=1) 
wind.mainloop()