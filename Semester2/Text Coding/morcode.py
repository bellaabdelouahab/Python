from tkinter import *
import enchant
d=enchant.Dict("en_US")
wind=Tk()
wind.title("coding ")
def codeI():
	n=(a.get())
	x=(b.get())
	c=list(n)
	print(n,len(n))
	for i in range(len(n)):
		d=0
		if c[i]!=' ':
			if (ord(c[i])+int(x))>=122:
				d=-26
			elif (ord(c[i])+int(x))<97:
				d=26
			c[i]=(chr(ord(c[i])+int(x)+d))
	c="".join(c)
	print(c)
	s.set(c)
def decodeI():
	n=(a.get())
	x=(b.get())
	c=list(n)
	for i in range(len(n)):
		c[i]=(chr(ord(c[i])-int(x)))
	c="".join(c)
	s.set(c)
def auto_decodeI():
	lebt=Label(wind,text='                                          ')
	lebt.grid(row=5,column=1)
	n=(a.get())
	n=n.split()
	wor_d=n[:]
	t=5
	for x in range(27):
		c=0
		for i in range(len(n)):
			v=list(n[i])
			print(x)
			print(v)
			for j in range(len(v)):
				h=0
				if (ord(v[j])-x)<97:
					h=26
				v[j]=(chr(ord(v[j])-x+h))
			v="".join(v)
			if d.check(v):
				c+=1
			wor_d[i]=v
		if c/len(n)*100>50:
			c=c/len(n)*100
			lebt=Label(wind,text="%"+str(int(c))+str(wor_d))
			lebt.grid(row=t,column=0)
			t+=1
	if t==5:
		lebt=Label(wind,text="your message can not be decoded")
		lebt.grid(row=t+1,column=0)
wind.geometry("400x400")
Labelmsg=Label(wind,text="coding type number")
Labelmsg.grid(row=0,column=0)
s=StringVar()
b= Entry(wind)
b.grid(row=0,column=1)
Labelmsg=Label(wind,text="give your massege")
Labelmsg.grid(row=1,column=0)
a= Entry(wind,textvariable=s)
a.grid(row=1,column=1)
btn=Button(wind,text="code",command=codeI)
btn.grid(row=2,column=1)
btn=Button(wind,text="decode",command=decodeI)
btn.grid(row=3,column=1)
btn=Button(wind,text="auto-decode",command=auto_decodeI)
btn.grid(row=4,column=1)
wind.mainloop()