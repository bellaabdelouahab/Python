from tkinter import *
window=Tk()
window.title("coding window")
window.geometry("400x400")
def codeI():
    n=list(a.get())
    m=list(b.get())
    print(n,' ',m)
    x=-1
    
    for i in range(len(n)):
        x+=1
        d=0
        if x>len(m)-1:
            x=0
        if n[i]!=' ':
            if (ord(n[i])+int(ord(m[x]))-97)>=122:
                d=-26
            elif (ord(n[i])+int(ord(m[x]))-97)<97:
                d=26
            n[i]=(chr(ord(n[i])+int(ord(m[x]))-97+d))
        else:
           x-=1
    n="".join(n)
    s.set(n)
def decode():
    n=list(a.get())
    m=list(b.get())
    print(n,' ',m)
    x=-1
    for i in range(len(n)):
        h=0
        x+=1
        d=0
        if x>len(m)-1:
            x=0
        if n[i]!=' ':
            if (ord(n[i])-int(ord(m[x])-97))<97:
                h=-26
                    
            n[i]=(chr(ord(n[i])-int(ord(m[x])-97+h)))
        else:
           x-=1 
    n="".join(n)
    s.set(n)  
Labelmsg=Label(window,text="The Key word")
Labelmsg.grid(row=0,column=0)
s=StringVar()
b= Entry(window)
b.grid(row=0,column=1)
Labelmsg=Label(window,text="Your message")
Labelmsg.grid(row=1,column=0)
a= Entry(window,textvariable=s)
a.grid(row=1,column=1)
btn=Button(window,text="code",command=codeI)
btn.grid(row=2,column=1)
btn1=Button(window,text="decode",command=decode)
btn1.grid(row=3,column=1)








window.mainloop()