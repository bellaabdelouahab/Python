
def p(tab):
    print('Table:\n',tab,'\nlenght:',len(tab),'\nSize:',tab.size,'\nType:',type(tab),'\nDimontion:',tab.ndim,'\nshape:',tab.shape,'\nDtype:',tab.dtype)
import numpy as np
tab=np.array([1,2,3,4,5,6,7,8,9,10,11,12],ndmin=3,dtype='i4')
p(tab)
tab=tab.astype("i8").reshape(-1,3)
tab1=np.full((3,3),150,dtype='i8')
tab2=np.full_like(tab1,-1,dtype='i8')
tab3=np.zeros(10)
tab4=np.identity(10).reshape(-1,4)*2
p(tab)
p(tab1)
p(tab2)
p(tab @ tab2)
p(np.sqrt(tab.dot(tab2)))
p(tab3)
p(tab4)
for x in np.nditer(tab4):
    print(x)
p(tab5)