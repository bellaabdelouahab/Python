class Node:
    def __init__(self,data):
        #left child
        self.left=None
        #right child
        self.right=None
        #node's value
        self.data=data
    def printtrre(self):
        if self.left:
            self.left.printtrre()
        print(self.data)
        if self.right:
            self.right.printtrre()
    def insert(self,newdata):
        if self.data:
            if newdata<self.data:
                if not self.left:
                    self.left=Node(newdata)
                else:
                    self.left.insert(newdata)
            elif newdata>self.data:
                if not self.right:
                    self.right=Node(newdata)
                else:
                    self.right.insert(newdata)             
        else :
            self.data=newdata
    def finder(self,val):
            if val<self.data:
                if not self.left:
                    return 'value not found'
                else:
                    self.left.finder(val)
            elif val>self.data:
                if not self.right:
                    return 'value not found'
                else:
                    self.right.finder(val)
            else:
                return 'value founded :'+str(val)
root=Node(27)
from random import randint
for  i in range(10):
    root.insert(randint(1,500))
root.printtrre()