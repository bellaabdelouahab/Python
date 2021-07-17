from pyglet import shapes,graphics,window,sprite,clock,app
from pyglet.window import key
from pyglet.window import event
from Track import set_track,Set_car
import numpy as np
import control as ct
from math import cos,sin,pi
windows = window.Window(1000,500)
keyboard = key.KeyStateHandler()
windows.push_handlers(keyboard)
rotation_angel=1
batch = graphics.Batch()
Tcrack_lines=set_track(batch)
Car=Set_car(50,0,371,102)
windows.set_icon(Car.image)


@windows.event
def on_mouse_press(x,y,button,modifiers):
    print(x,',',y)

def car(carX,carY):
    global Car
    Car.sprite.rotation+=carX/(rotation_angel*12)
    Car.Carx+=carY/10*cos((-Car.sprite.rotation+90)*pi/180)
    Car.Cary+=carY/10*sin((-Car.sprite.rotation+90)*pi/180)
    if abs(-Car.sprite.rotation+90)==360:
        rotation=90
    Car.update(Car.Carx,Car.Cary,Car.sprite.rotation,Car.sprite)
def hover(line,a,b):
    for i in a:
        if i in b:
            line.color=(200,20,20)
            return i
    line.color=(20,200,20)
    return False
def coords(x,x1,y,y1):
    if x1==x:
        return [[x,i] for i in range(y,y1+1)]
    else:
        b=(y1-y)/(x1-x)
        c=y-b*x
        if abs(x1-x)>abs(y1-y):
            return ([[i,int(b*i+c)] for i in range(x,x1+1)])
        else:
            return ([[int((i-c)/b),i] for i in range(y,y1+1)])
    
def on_draw():
    windows.clear()
    Car.car.draw()
    batch.draw()
windows.on_draw=on_draw
def on_text():
    global Car,rotation_angel
    if keyboard[key.MOTION_DOWN]:
        car(0,Car.velocity)
        if Car.velocity>-40 :
            Car.velocity-=1
    if keyboard[key.MOTION_UP]:
        car(0,Car.velocity)
        if Car.velocity<40:
            Car.velocity+=1
    if keyboard[key.MOTION_LEFT]:
        car(-Car.velocity,0)
        if rotation_angel>1:
            rotation_angel-=0.5
    if keyboard[key.MOTION_RIGHT]:
        car(Car.velocity,0)
        if rotation_angel>1:
            rotation_angel-=0.5
    '''if keyboard[key.MOTION_UP] and keyboard[key.MOTION_LEFT]:
        car(-Car.velocity,Car.velocity/350)
    if keyboard[key.MOTION_UP] and keyboard[key.MOTION_RIGHT]:
        car(Car.velocity,Car.velocity/350)
    if keyboard[key.MOTION_DOWN] and keyboard[key.MOTION_LEFT]:
        car(-Car.velocity,Car.velocity/350)
    if keyboard[key.MOTION_DOWN] and keyboard[key.MOTION_RIGHT]:
        car(Car.velocity,Car.velocity/350)'''

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
    #distence= hover(Tcrack_lines[0],coords(Tcrack_lines[0].x,Tcrack_lines[0].x2,Tcrack_lines[0].y,Tcrack_lines[0].y2),coords(lineA_3.x,lineA_3.x2,lineA_3.y,lineA_3.y2))
clock.schedule_interval(update, 1/60)

app.run()