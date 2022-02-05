from tkinter import filedialog
from tkinter import *

def browse_button():
    filename = filedialog.askdirectory()
    print(filename)
    return filename


root = Tk()
v = StringVar()
button2 = Button(text="Browse", command=browse_button).grid(row=0, column=3)

mainloop()