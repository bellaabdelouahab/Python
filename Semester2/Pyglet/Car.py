from pyglet import shapes,resource,sprite,graphics,text
from math import cos,sin,pi
class Set_car:
    car = graphics.Batch()
    image=resource.image('unnamed.png')
    Carx=752
    Cary=102
    image.width=20
    image.height=40
    image.anchor_x = 10
    image.anchor_y = 20
    sprite = sprite.Sprite(image, x = Carx, y = Cary,batch=car)
    sprite.rotation=-90
    sprite.opacity=100
    lines=[
    [shapes.Line(Carx-20 , Cary+10,Carx-119 , Cary+10,width=1, color=(255,255,255), batch=car),shapes.Circle(Carx-90 , Cary+10, 3, color=(50, 225, 30), batch=car),True,text.Label('',font_name='Times New Roman',font_size=15,x=948, y=485,batch=car)],
    [shapes.Line(Carx-20 , Cary-10,Carx-119 , Cary-10,width=1, color=(255,255,255), batch=car),shapes.Circle(Carx-90 , Cary-10, 3, color=(50, 225, 30), batch=car),True,text.Label('',font_name='Times New Roman',font_size=15,x=948, y=470,batch=car)],
    [shapes.Line(Carx-20 , Cary+10,Carx-60 , Cary+60,width=1, color=(255,255,255), batch=car),shapes.Circle(Carx-60 , Cary+60, 3, color=(50, 225, 30), batch=car),True,text.Label('',font_name='Times New Roman',font_size=15,x=948, y=455,batch=car)],
    [shapes.Line(Carx-20 , Cary-10,Carx-60 , Cary-60,width=1, color=(255,255,255), batch=car),shapes.Circle(Carx-60 , Cary-60, 3, color=(50, 225, 30), batch=car),True,text.Label('',font_name='Times New Roman',font_size=15,x=948, y=440,batch=car)],
    [shapes.Line(Carx+20 , Cary+10,Carx+119 , Cary+10,width=1, color=(255,255,255), batch=car),shapes.Circle(Carx+90 , Cary+10, 3, color=(50, 225, 30), batch=car),True,text.Label('',font_name='Times New Roman',font_size=15,x=948, y=425,batch=car)],
    [shapes.Line(Carx+20 , Cary-10,Carx+119 , Cary-10,width=1, color=(255,255,255), batch=car),shapes.Circle(Carx+90 , Cary-10, 3, color=(50, 225, 30), batch=car),True,text.Label('',font_name='Times New Roman',font_size=15,x=948, y=410,batch=car)],
    [shapes.Line(Carx+20 , Cary+10,Carx+60 , Cary+60,width=1, color=(255,255,255), batch=car),shapes.Circle(Carx+60 , Cary+60, 3, color=(50, 225, 30), batch=car),True,text.Label('',font_name='Times New Roman',font_size=15,x=948, y=395,batch=car)],
    [shapes.Line(Carx+20 , Cary-10,Carx+60 , Cary-60,width=1, color=(255,255,255), batch=car),shapes.Circle(Carx+60 , Cary-60, 3, color=(50, 225, 30), batch=car),True,text.Label('',font_name='Times New Roman',font_size=15,x=948, y=380,batch=car)],
    [shapes.Line(Carx+ 5 , Cary+10,Carx+ 5 , Cary+60,width=1, color=(255,255,255), batch=car),shapes.Circle(Carx+ 5 , Cary+60, 3, color=(50, 225, 30), batch=car),True,text.Label('',font_name='Times New Roman',font_size=15,x=948, y=365,batch=car)],
    [shapes.Line(Carx+ 5 , Cary-10,Carx+ 5 , Cary-60,width=1, color=(255,255,255), batch=car),shapes.Circle(Carx+ 5 , Cary-60, 3, color=(50, 225, 30), batch=car),True,text.Label('',font_name='Times New Roman',font_size=15,x=948, y=350,batch=car)]
    ]
    car_shape=[
        shapes.Line( 353+382  ,  111 , 389+382  , 111  ,width=1, color=(20, 200, 20), batch=car),
        shapes.Line( 353+382  ,   96 , 389+382  , 96  ,width=1, color=(20, 200, 20), batch=car),
        shapes.Line( 354+382  ,  108 , 352+382  , 97  ,width=1, color=(20, 200, 20), batch=car),
        shapes.Line( 389+382  ,  109 , 389+382  , 96  ,width=1, color=(20, 200, 20), batch=car)
    ]
    for line in lines:
        line[1].opacity=1000
        line[0].opacity=1000
        line[3].color = (100, 255, 100, 255)
        line[3].text=str(format(((line[0].x2-(line[0].x))**2 + (line[0].y2-(line[0].y))**2)**0.5, ".2f"))
    for line in car_shape:
        line.opacity=0
    lines_coord=[[line[0].x-752,line[0].y-102,line[0].x2-752,line[0].y2-102] for line in lines]
    car_body=[[line.x-752,line.y-102,line.x2-752,line.y2-102] for line in car_shape]
    def __init__(self):
        self.velocity=0
    def update(self,rotation,sprite):
        sprite.update(x=self.Carx,y=self.Cary,rotation=rotation)
        for i in range(0,len(self.lines_coord)):
            self.move_lines(self.lines[i],self.lines_coord[i][0],self.lines_coord[i][1],self.lines_coord[i][2],self.lines_coord[i][3],rotation)
        for i in range(len(self.car_body)):
            self.move_lines([self.car_shape[i],0,False],self.car_body[i][0],self.car_body[i][1],self.car_body[i][2],self.car_body[i][3],rotation)
    def move_lines(self,line,a,b,c,d,rotation):
        line[0].x=self.Carx+(a)*cos(-(rotation-270)*pi/180)-(b)*sin(-(rotation-270)*pi/180)
        line[0].y=self.Cary+(a)*sin(-(rotation-270)*pi/180)+(b)*cos(-(rotation-270)*pi/180)
        line[0].x2=self.Carx+(c)*cos(-(rotation-270)*pi/180)-(d)*sin(-(rotation-270)*pi/180)
        line[0].y2=self.Cary+(c)*sin(-(rotation-270)*pi/180)+(d)*cos(-(rotation-270)*pi/180)
        if line[2]:
            line[1].opacity=1000
            line[1].x=line[0].x2 
            line[1].y=line[0].y2
    def set_default_distance(self,x):
        x[0][3].text=str(format(((x[0][0].x2-(x[0][0].x))**2 + (x[0][0].y2-(x[0][0].y))**2)**0.5, ".2f"))
        x[1][3].text=str(format(((x[1][0].x2-(x[1][0].x))**2 + (x[1][0].y2-(x[1][0].y))**2)**0.5, ".2f"))
        x[2][3].text=str(format(((x[2][0].x2-(x[2][0].x))**2 + (x[2][0].y2-(x[2][0].y))**2)**0.5, ".2f"))
        x[3][3].text=str(format(((x[3][0].x2-(x[3][0].x))**2 + (x[3][0].y2-(x[3][0].y))**2)**0.5, ".2f"))
        x[4][3].text=str(format(((x[4][0].x2-(x[4][0].x))**2 + (x[4][0].y2-(x[4][0].y))**2)**0.5, ".2f"))
        x[5][3].text=str(format(((x[5][0].x2-(x[5][0].x))**2 + (x[5][0].y2-(x[5][0].y))**2)**0.5, ".2f"))
        x[6][3].text=str(format(((x[6][0].x2-(x[6][0].x))**2 + (x[6][0].y2-(x[6][0].y))**2)**0.5, ".2f"))
        x[7][3].text=str(format(((x[7][0].x2-(x[7][0].x))**2 + (x[7][0].y2-(x[7][0].y))**2)**0.5, ".2f"))
        x[8][3].text=str(format(((x[8][0].x2-(x[8][0].x))**2 + (x[8][0].y2-(x[8][0].y))**2)**0.5, ".2f"))
        x[9][3].text=str(format(((x[9][0].x2-(x[9][0].x))**2 + (x[9][0].y2-(x[9][0].y))**2)**0.5, ".2f"))
        return [int(float(x[i][3].text)) for i in range(len(x))]
    
class Set_car2:
    car1 = graphics.Batch()
    image=resource.image('unnamed.png')
    Carx=752
    Cary=102
    image.width=20
    image.height=40
    image.anchor_x = 10
    image.anchor_y = 20
    sprite = sprite.Sprite(image, x = Carx, y = Cary,batch=car1)
    sprite.rotation=-90
    sprite.opacity=100