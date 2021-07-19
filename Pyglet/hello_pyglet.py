from pyglet import graphics,window,clock,app
from Track import set_track,Set_car
from math import cos,sin,pi
windows = window.Window(1000,500)
keyboard = window.key.KeyStateHandler()
windows.push_handlers(keyboard)
rotation_angel=1
batch = graphics.Batch()
Tcrack_lines=set_track(batch)
Car=Set_car()
windows.set_icon(Car.image)


@windows.event
def on_mouse_press(x,y,button,modifiers):
    print(x,',',y)
def car(carX,carY):
    global Car
    Car.sprite.rotation+=carX/(rotation_angel*7)
    Car.Carx+=carY/10*cos((-Car.sprite.rotation+90)*pi/180)
    Car.Cary+=carY/10*sin((-Car.sprite.rotation+90)*pi/180)
    if abs(-Car.sprite.rotation+90)>=360:
        Car.sprite.rotation=90
    Car.update(Car.sprite.rotation,Car.sprite)
def hover(line,x4,y4,x3,y3,x2,y2,x1,y1):
    if ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))==0:
        return False
    uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
    uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
    if uA >= 0 and uA <= 1 and uB >= 0 and uB <= 1:
        line[2]=False
        line[1].opacity=1000
        line[1].x = x1 + (uA * (x2-x1))
        line[1].y = y1 + (uA * (y2-y1))
        return line[1].x,line[1].y
    else:
        return False
    
def on_draw():
    windows.clear()
    Car.car.draw()
    batch.draw()
windows.on_draw=on_draw
def on_text():
    global Car,rotation_angel
    if keyboard[key.MOTION_DOWN]:
        car(0,Car.velocity)
        if Car.velocity>-20 :
            Car.velocity-=1
    if keyboard[key.MOTION_UP]:
        car(0,Car.velocity)
        if Car.velocity<20:
            Car.velocity+=1
    if keyboard[key.MOTION_LEFT]:
        car(-Car.velocity,0)
        if rotation_angel>1:
            rotation_angel-=1
    if keyboard[key.MOTION_RIGHT]:
        car(Car.velocity,0)
        if rotation_angel>1:
            rotation_angel-=1

def update(dt):
    global Car,rotation_angel
    for keys in keyboard:
        if keyboard[keys]:
            on_text()
    if not keyboard[key.MOTION_UP] and Car.velocity>0 :
        Car.velocity-=0.5
        car(0,Car.velocity)
    if not keyboard[key.MOTION_DOWN] and Car.velocity<0:
        Car.velocity+=0.5
        car(0,Car.velocity)
    if (not keyboard[key.MOTION_LEFT] and not keyboard[key.MOTION_RIGHT]) and rotation_angel<10:
        rotation_angel+=5
    distence=[False]*len(Car.lines)
    for i in range(0,len(Tcrack_lines)):
        for j in range(0,len(Car.lines)):
            x=(hover(Car.lines[j],Tcrack_lines[i].x2,Tcrack_lines[i].y2,Tcrack_lines[i].x,Tcrack_lines[i].y,\
                Car.lines[j][0].x2,Car.lines[j][0].y2,Car.lines[j][0].x,Car.lines[j][0].y))
            if x!=False:
                distence[j]=x
    #print(distence,'\n')
    for i in range(0,len(distence)):
        if distence[i]==False:
            Car.lines[i][2]=True
clock.schedule_interval(update, 1/60)

app.run()
