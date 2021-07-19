from pyglet import shapes,resource,sprite,graphics
from math import cos,sin,pi
def set_track(batch):
    return [
        shapes.Line(100 , 350,470 , 452 ,width=1, color=(20, 200, 20), batch=batch),
        shapes.Line(175 , 291,489 , 372 ,width=1, color=(20, 200, 20), batch=batch),
        shapes.Line(100 , 350, 98 , 196 ,width=1, color=(20, 200, 20), batch=batch),
        shapes.Line(175 , 291,175 , 192 ,width=1, color=(20, 200, 20), batch=batch),
        shapes.Line( 98 , 196,  4 , 119 ,width=1, color=(20, 200, 20), batch=batch),
        shapes.Line(175 , 192, 97 , 119 ,width=1, color=(20, 200, 20), batch=batch),
        shapes.Line(  4 , 119, 83 ,   2 ,width=1, color=(20, 200, 20), batch=batch),
        shapes.Line( 97 , 119,137 ,  70 ,width=1, color=(20, 200, 20), batch=batch),
        shapes.Line( 83 ,   2,830 ,   2 ,width=1, color=(20, 20, 200), batch=batch),
        shapes.Line(137 ,  70,780 ,  70 ,width=1, color=(20, 200, 20), batch=batch),
        shapes.Line(830 ,   2,855 ,  30 ,width=1, color=(20, 200, 20), batch=batch),
        shapes.Line(855 ,  30,855 , 110 ,width=1, color=(20, 200, 20), batch=batch),
        shapes.Line(855 , 110,830 , 140 ,width=1, color=(20, 200, 20), batch=batch),
        shapes.Line(830 , 140,200 , 140 ,width=1, color=(20, 200, 20), batch=batch),
        shapes.Line(470 , 452,558 , 452 ,width=1, color=(20, 200, 20), batch=batch),
        shapes.Line(558 , 452,825 , 220 ,width=1, color=(20, 200, 20), batch=batch),
        shapes.Line(489 , 372,717 , 218 ,width=1, color=(20, 200, 20), batch=batch),
        shapes.Line(826 , 222,829 , 141 ,width=1, color=(20, 200, 20), batch=batch),
        shapes.Line(175 , 191,716 , 218 ,width=1, color=(20, 200, 20), batch=batch)]

class Set_car:
    car = graphics.Batch()
    image=resource.image('unnamed.png')
    Carx=371
    Cary=102
    image.width=20
    image.height=40
    image.anchor_x = 10
    image.anchor_y = 20
    sprite = sprite.Sprite(image, x = Carx, y = Cary,batch=car)
    sprite.rotation=270
    sprite.opacity=100
    lines=[
    [shapes.Line(Carx-20 , Cary+10,Carx-90 , Cary+10,width=1, color=(255,255,255), batch=car),shapes.Circle(Carx-90 , Cary+10, 3, color=(50, 225, 30), batch=car),True],
    [shapes.Line(Carx-20 , Cary-10,Carx-90 , Cary-10,width=1, color=(255,255,255), batch=car),shapes.Circle(Carx-90 , Cary-10, 3, color=(50, 225, 30), batch=car),True],
    [shapes.Line(Carx-20 , Cary+10,Carx-60 , Cary+60,width=1, color=(255,255,255), batch=car),shapes.Circle(Carx-60 , Cary+60, 3, color=(50, 225, 30), batch=car),True],
    [shapes.Line(Carx-20 , Cary-10,Carx-60 , Cary-60,width=1, color=(255,255,255), batch=car),shapes.Circle(Carx-60 , Cary-60, 3, color=(50, 225, 30), batch=car),True],
    [shapes.Line(Carx+20 , Cary+10,Carx+90 , Cary+10,width=1, color=(255,255,255), batch=car),shapes.Circle(Carx+90 , Cary+10, 3, color=(50, 225, 30), batch=car),True],
    [shapes.Line(Carx+20 , Cary-10,Carx+90 , Cary-10,width=1,color=(255,255,255),  batch=car),shapes.Circle(Carx+90 , Cary-10, 3, color=(50, 225, 30), batch=car),True],
    [shapes.Line(Carx+20 , Cary+10,Carx+60 , Cary+60,width=1, color=(255,255,255), batch=car),shapes.Circle(Carx+60 , Cary+60, 3, color=(50, 225, 30), batch=car),True],
    [shapes.Line(Carx+20 , Cary-10,Carx+60 , Cary-60,width=1, color=(255,255,255), batch=car),shapes.Circle(Carx+60 , Cary-60, 3, color=(50, 225, 30), batch=car),True],
    [shapes.Line(Carx+ 5 , Cary+10,Carx+ 5 , Cary+60,width=1, color=(255,255,255), batch=car),shapes.Circle(Carx+ 5 , Cary+60, 3, color=(50, 225, 30), batch=car),True],
    [shapes.Line(Carx+ 5 , Cary-10,Carx+ 5 , Cary-60,width=1, color=(255,255,255), batch=car),shapes.Circle(Carx+ 5 , Cary-60, 3, color=(50, 225, 30), batch=car),True]
    ]
    for line in lines:
        line[1].opacity=0
        line[0].opacity=0
    lines_coord=[[line[0].x-370,line[0].y-102,line[0].x2-370,line[0].y2-102] for line in lines]
    def __init__(self):
        self.velocity=0
    def update(self,rotation,sprite):
        sprite.update(x=self.Carx,y=self.Cary,rotation=rotation)
        for i in range(0,len(self.lines_coord)):
            self.move_lines(self.lines[i],self.lines_coord[i][0],self.lines_coord[i][1],self.lines_coord[i][2],self.lines_coord[i][3],rotation)
    def move_lines(self,line,a,b,c,d,rotation):
        line[0].x=self.Carx+(a)*cos(-(rotation-270)*pi/180)-(b)*sin(-(rotation-270)*pi/180)
        line[0].y=self.Cary+(a)*sin(-(rotation-270)*pi/180)+(b)*cos(-(rotation-270)*pi/180)
        line[0].x2=self.Carx+(c)*cos(-(rotation-270)*pi/180)-(d)*sin(-(rotation-270)*pi/180)
        line[0].y2=self.Cary+(c)*sin(-(rotation-270)*pi/180)+(d)*cos(-(rotation-270)*pi/180)
        if line[2]:
            line[1].opacity=0
            line[1].x=line[0].x2
            line[1].y=line[0].y2
