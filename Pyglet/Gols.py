from pyglet import shapes
def SetGoals(batch):
    return [
        [shapes.Line( 310  ,  139 , 310  , 72  ,width=1, color=(200,20, 20), batch=batch),True],
        [shapes.Line( 208  ,  139 , 205  , 72  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 198  ,  143 , 176  , 192  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 377  ,  143 , 372  , 201  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 547  ,  142 , 537  , 210  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 672  ,  142 , 656  , 216  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 716  ,  219 , 828  , 187  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 633  ,  276 , 692  , 335  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 512  ,  356 , 560  , 449  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 438  ,  360 , 428  , 439  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 256  ,  314 , 231  , 387  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 174  ,  291 , 100  , 353  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 173  ,  193 , 98  , 196  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 96  ,  120 , 6  , 119  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 136  ,  70 , 85  , 4  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 284  ,  69 , 284  , 7  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 443  ,  70 , 441  , 5  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 571  ,  71 , 571  , 5  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 715  ,  69 , 715  , 2  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 782  ,  71 , 854  , 72  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 709  ,  141 , 709  , 74  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 607  ,  139 , 607  , 73  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 473  ,  141 , 473  , 70  ,width=1, color=(200,20, 20), batch=batch),False],
        [shapes.Line( 376  ,  139 , 375  , 72  ,width=1, color=(200,20, 20), batch=batch),False],
    ]
'''class Goal:
    def isActive(self, win):
        shapes.Line(self.x2, self.y2,self.x1, self.y1 ,width=1,color=(255,255,255))
        if self.isactiv:
            shapes.Line(self.x2, self.y2,self.x1, self.y1 ,width=1,color=(255,25,255))'''
