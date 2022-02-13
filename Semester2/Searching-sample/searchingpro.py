import os 
rep='/home/bella/Documents/Python'
ext='txt'
def search_file(rep,ext):
    liste=os.listdir(rep)
    for i in liste:
        if os.path.isfile(i):
            if i[-3:]==ext:
                print(rep+'/'+i)
        else:
            search_file(rep+'/'+i,ext)
search_file(rep,ext)