from random import randint,shuffle
def win(sudo):
    
    for i in range(9):

        for j in range(9):

            if [sudo[i][x]for x in range(9)].count(j+1)!=1:
                
                return False

            if [sudo[x][i]for x in range(9)].count(j+1)!=1:
                
                return False

            i1=i-i%3

            j1=j-j%3
            
            s=0
            
            for x in range(3):

                for y in range(3):

                    if sudo[x+i1][y+j1]==j+1:
                        
                        s+=1
            
            if(s>1):
            
                return False
    
    return True

def check_if_valide(sudo,i,j,nbr,n):

    for x in range(n):

        if sudo[i][x]==nbr:

            return False

    for x in range(n):

        if sudo[x][j]==nbr:

            return False

    i1=i-i%3

    j1=j-j%3

    for x in range(3):

        for y in range(3):

            if sudo[x+i1][y+j1]==nbr:

                return False

    return True

sudo=[[0]*9 for i in range(9)]

n=9

def solve_sudo(sudo,i,j,n):

    if i==n-1 and j==n:

        return True

    if j==n:

        i+=1

        j=0

    if sudo[i][j]>0:

        return solve_sudo(sudo,i,j+1,n)
    f=[i for i in range(1,10)]
    shuffle(f)
    for nbr in f:
        
        if check_if_valide(sudo,i,j,nbr,n):

            sudo[i][j]=nbr

            if solve_sudo(sudo,i,j+1,n):

                return True

        sudo[i][j]=0

    return False


if solve_sudo(sudo,0,0,n):

    print('solved')

    for i in range(9):

        print(sudo[i])

else:

    print('cant be solved')

for i in range(60):
    sudo[randint(0,8)][randint(0,8)]=''

###############################################################################################33

from tkinter import Tk,StringVar,Button

wind = Tk()

a=[1]*81

for i in range(81):
    
    a[i] = StringVar(value=sudo[i//9][i%9])

wind.geometry("590x600")

def luckyou(s):
    
    if s.get()=='':
        
        A=0
    
    else:
    
        A=int(s.get())
    
    if A==9:
        
        A=0
        
    s.set(A+1)
    
    for i in range(81):
        
        if a[i].get()=='':
            
            sudo[i//9][i%9]=0
    
        else:
    
            sudo[i//9][i%9]=int(a[i].get())
    
    if win(sudo):
    
        print("youwin")

btn=[None]*81

btn[ 0 ] = Button(wind , textvariable = a[ 0 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 0 ])) 

btn[ 0 ].grid(row =  0  //9, column =  0 %9)

btn[ 1 ] = Button(wind , textvariable = a[ 1 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 1 ])) 

btn[ 1 ].grid(row =  1  //9, column =  1 %9)

btn[ 2 ] = Button(wind , textvariable = a[ 2 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 2 ])) 

btn[ 2 ].grid(row =  2  //9, column =  2 %9)

btn[ 3 ] = Button(wind , textvariable = a[ 3 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 3 ])) 

btn[ 3 ].grid(row =  3  //9, column =  3 %9)

btn[ 4 ] = Button(wind , textvariable = a[ 4 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 4 ])) 

btn[ 4 ].grid(row =  4  //9, column =  4 %9)

btn[ 5 ] = Button(wind , textvariable = a[ 5 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 5 ])) 

btn[ 5 ].grid(row =  5  //9, column =  5 %9)

btn[ 6 ] = Button(wind , textvariable = a[ 6 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 6 ])) 

btn[ 6 ].grid(row =  6  //9, column =  6 %9)

btn[ 7 ] = Button(wind , textvariable = a[ 7 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 7 ])) 

btn[ 7 ].grid(row =  7  //9, column =  7 %9)

btn[ 8 ] = Button(wind , textvariable = a[ 8 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 8 ])) 

btn[ 8 ].grid(row =  8  //9, column =  8 %9)

btn[ 9 ] = Button(wind , textvariable = a[ 9 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 9 ])) 

btn[ 9 ].grid(row =  9  //9, column =  9 %9)

btn[ 10 ] = Button(wind , textvariable = a[ 10 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 10 ])) 

btn[ 10 ].grid(row =  10  //9, column =  10 %9)

btn[ 11 ] = Button(wind , textvariable = a[ 11 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 11 ])) 

btn[ 11 ].grid(row =  11  //9, column =  11 %9)

btn[ 12 ] = Button(wind , textvariable = a[ 12 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 12 ])) 

btn[ 12 ].grid(row =  12  //9, column =  12 %9)

btn[ 13 ] = Button(wind , textvariable = a[ 13 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 13 ])) 

btn[ 13 ].grid(row =  13  //9, column =  13 %9)

btn[ 14 ] = Button(wind , textvariable = a[ 14 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 14 ])) 

btn[ 14 ].grid(row =  14  //9, column =  14 %9)

btn[ 15 ] = Button(wind , textvariable = a[ 15 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 15 ])) 

btn[ 15 ].grid(row =  15  //9, column =  15 %9)

btn[ 16 ] = Button(wind , textvariable = a[ 16 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 16 ])) 

btn[ 16 ].grid(row =  16  //9, column =  16 %9)

btn[ 17 ] = Button(wind , textvariable = a[ 17 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 17 ])) 

btn[ 17 ].grid(row =  17  //9, column =  17 %9)

btn[ 18 ] = Button(wind , textvariable = a[ 18 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 18 ])) 

btn[ 18 ].grid(row =  18  //9, column =  18 %9)

btn[ 19 ] = Button(wind , textvariable = a[ 19 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 19 ])) 

btn[ 19 ].grid(row =  19  //9, column =  19 %9)

btn[ 20 ] = Button(wind , textvariable = a[ 20 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 20 ])) 

btn[ 20 ].grid(row =  20  //9, column =  20 %9)

btn[ 21 ] = Button(wind , textvariable = a[ 21 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 21 ])) 

btn[ 21 ].grid(row =  21  //9, column =  21 %9)

btn[ 22 ] = Button(wind , textvariable = a[ 22 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 22 ])) 

btn[ 22 ].grid(row =  22  //9, column =  22 %9)

btn[ 23 ] = Button(wind , textvariable = a[ 23 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 23 ])) 

btn[ 23 ].grid(row =  23  //9, column =  23 %9)

btn[ 24 ] = Button(wind , textvariable = a[ 24 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 24 ])) 

btn[ 24 ].grid(row =  24  //9, column =  24 %9)

btn[ 25 ] = Button(wind , textvariable = a[ 25 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 25 ])) 

btn[ 25 ].grid(row =  25  //9, column =  25 %9)

btn[ 26 ] = Button(wind , textvariable = a[ 26 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 26 ])) 

btn[ 26 ].grid(row =  26  //9, column =  26 %9)

btn[ 27 ] = Button(wind , textvariable = a[ 27 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 27 ])) 

btn[ 27 ].grid(row =  27  //9, column =  27 %9)

btn[ 28 ] = Button(wind , textvariable = a[ 28 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 28 ])) 

btn[ 28 ].grid(row =  28  //9, column =  28 %9)

btn[ 29 ] = Button(wind , textvariable = a[ 29 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 29 ])) 

btn[ 29 ].grid(row =  29  //9, column =  29 %9)

btn[ 30 ] = Button(wind , textvariable = a[ 30 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 30 ])) 

btn[ 30 ].grid(row =  30  //9, column =  30 %9)

btn[ 31 ] = Button(wind , textvariable = a[ 31 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 31 ])) 

btn[ 31 ].grid(row =  31  //9, column =  31 %9)

btn[ 32 ] = Button(wind , textvariable = a[ 32 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 32 ])) 

btn[ 32 ].grid(row =  32  //9, column =  32 %9)

btn[ 33 ] = Button(wind , textvariable = a[ 33 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 33 ])) 

btn[ 33 ].grid(row =  33  //9, column =  33 %9)

btn[ 34 ] = Button(wind , textvariable = a[ 34 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 34 ])) 

btn[ 34 ].grid(row =  34  //9, column =  34 %9)

btn[ 35 ] = Button(wind , textvariable = a[ 35 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 35 ])) 

btn[ 35 ].grid(row =  35  //9, column =  35 %9)

btn[ 36 ] = Button(wind , textvariable = a[ 36 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 36 ])) 

btn[ 36 ].grid(row =  36  //9, column =  36 %9)

btn[ 37 ] = Button(wind , textvariable = a[ 37 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 37 ])) 

btn[ 37 ].grid(row =  37  //9, column =  37 %9)

btn[ 38 ] = Button(wind , textvariable = a[ 38 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 38 ])) 

btn[ 38 ].grid(row =  38  //9, column =  38 %9)

btn[ 39 ] = Button(wind , textvariable = a[ 39 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 39 ])) 

btn[ 39 ].grid(row =  39  //9, column =  39 %9)

btn[ 40 ] = Button(wind , textvariable = a[ 40 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 40 ])) 

btn[ 40 ].grid(row =  40  //9, column =  40 %9)

btn[ 41 ] = Button(wind , textvariable = a[ 41 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 41 ])) 

btn[ 41 ].grid(row =  41  //9, column =  41 %9)

btn[ 42 ] = Button(wind , textvariable = a[ 42 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 42 ])) 

btn[ 42 ].grid(row =  42  //9, column =  42 %9)

btn[ 43 ] = Button(wind , textvariable = a[ 43 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 43 ])) 

btn[ 43 ].grid(row =  43  //9, column =  43 %9)

btn[ 44 ] = Button(wind , textvariable = a[ 44 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 44 ])) 

btn[ 44 ].grid(row =  44  //9, column =  44 %9)

btn[ 45 ] = Button(wind , textvariable = a[ 45 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 45 ])) 

btn[ 45 ].grid(row =  45  //9, column =  45 %9)

btn[ 46 ] = Button(wind , textvariable = a[ 46 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 46 ])) 

btn[ 46 ].grid(row =  46  //9, column =  46 %9)

btn[ 47 ] = Button(wind , textvariable = a[ 47 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 47 ])) 

btn[ 47 ].grid(row =  47  //9, column =  47 %9)

btn[ 48 ] = Button(wind , textvariable = a[ 48 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 48 ])) 

btn[ 48 ].grid(row =  48  //9, column =  48 %9)

btn[ 49 ] = Button(wind , textvariable = a[ 49 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 49 ])) 

btn[ 49 ].grid(row =  49  //9, column =  49 %9)

btn[ 50 ] = Button(wind , textvariable = a[ 50 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 50 ])) 

btn[ 50 ].grid(row =  50  //9, column =  50 %9)

btn[ 51 ] = Button(wind , textvariable = a[ 51 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 51 ])) 

btn[ 51 ].grid(row =  51  //9, column =  51 %9)

btn[ 52 ] = Button(wind , textvariable = a[ 52 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 52 ])) 

btn[ 52 ].grid(row =  52  //9, column =  52 %9)

btn[ 53 ] = Button(wind , textvariable = a[ 53 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 53 ])) 

btn[ 53 ].grid(row =  53  //9, column =  53 %9)

btn[ 54 ] = Button(wind , textvariable = a[ 54 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 54 ])) 

btn[ 54 ].grid(row =  54  //9, column =  54 %9)

btn[ 55 ] = Button(wind , textvariable = a[ 55 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 55 ])) 

btn[ 55 ].grid(row =  55  //9, column =  55 %9)

btn[ 56 ] = Button(wind , textvariable = a[ 56 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 56 ])) 

btn[ 56 ].grid(row =  56  //9, column =  56 %9)

btn[ 57 ] = Button(wind , textvariable = a[ 57 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 57 ])) 

btn[ 57 ].grid(row =  57  //9, column =  57 %9)

btn[ 58 ] = Button(wind , textvariable = a[ 58 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 58 ])) 

btn[ 58 ].grid(row =  58  //9, column =  58 %9)

btn[ 59 ] = Button(wind , textvariable = a[ 59 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 59 ])) 

btn[ 59 ].grid(row =  59  //9, column =  59 %9)

btn[ 60 ] = Button(wind , textvariable = a[ 60 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 60 ])) 

btn[ 60 ].grid(row =  60  //9, column =  60 %9)

btn[ 61 ] = Button(wind , textvariable = a[ 61 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 61 ])) 

btn[ 61 ].grid(row =  61  //9, column =  61 %9)

btn[ 62 ] = Button(wind , textvariable = a[ 62 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 62 ])) 

btn[ 62 ].grid(row =  62  //9, column =  62 %9)

btn[ 63 ] = Button(wind , textvariable = a[ 63 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 63 ])) 

btn[ 63 ].grid(row =  63  //9, column =  63 %9)

btn[ 64 ] = Button(wind , textvariable = a[ 64 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 64 ])) 

btn[ 64 ].grid(row =  64  //9, column =  64 %9)

btn[ 65 ] = Button(wind , textvariable = a[ 65 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 65 ])) 

btn[ 65 ].grid(row =  65  //9, column =  65 %9)

btn[ 66 ] = Button(wind , textvariable = a[ 66 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 66 ])) 

btn[ 66 ].grid(row =  66  //9, column =  66 %9)

btn[ 67 ] = Button(wind , textvariable = a[ 67 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 67 ])) 

btn[ 67 ].grid(row =  67  //9, column =  67 %9)

btn[ 68 ] = Button(wind , textvariable = a[ 68 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 68 ])) 

btn[ 68 ].grid(row =  68  //9, column =  68 %9)

btn[ 69 ] = Button(wind , textvariable = a[ 69 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 69 ])) 

btn[ 69 ].grid(row =  69  //9, column =  69 %9)

btn[ 70 ] = Button(wind , textvariable = a[ 70 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 70 ])) 

btn[ 70 ].grid(row =  70  //9, column =  70 %9)

btn[ 71 ] = Button(wind , textvariable = a[ 71 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 71 ])) 

btn[ 71 ].grid(row =  71  //9, column =  71 %9)

btn[ 72 ] = Button(wind , textvariable = a[ 72 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 72 ])) 

btn[ 72 ].grid(row =  72  //9, column =  72 %9)

btn[ 73 ] = Button(wind , textvariable = a[ 73 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 73 ])) 

btn[ 73 ].grid(row =  73  //9, column =  73 %9)

btn[ 74 ] = Button(wind , textvariable = a[ 74 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 74 ])) 

btn[ 74 ].grid(row =  74  //9, column =  74 %9)

btn[ 75 ] = Button(wind , textvariable = a[ 75 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 75 ])) 

btn[ 75 ].grid(row =  75  //9, column =  75 %9)

btn[ 76 ] = Button(wind , textvariable = a[ 76 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 76 ])) 

btn[ 76 ].grid(row =  76  //9, column =  76 %9)

btn[ 77 ] = Button(wind , textvariable = a[ 77 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 77 ])) 

btn[ 77 ].grid(row =  77  //9, column =  77 %9)

btn[ 78 ] = Button(wind , textvariable = a[ 78 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 78 ])) 

btn[ 78 ].grid(row =  78  //9, column =  78 %9)

btn[ 79 ] = Button(wind , textvariable = a[ 79 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 79 ])) 

btn[ 79 ].grid(row =  79  //9, column =  79 %9)

btn[ 80 ] = Button(wind , textvariable = a[ 80 ] , height = 3 , width = 8 , command= lambda : luckyou(a[ 80 ])) 

btn[ 80 ].grid(row =  80  //9, column =  80 %9)

wind.mainloop()