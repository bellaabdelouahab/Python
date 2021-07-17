from pyglet import shapes,resource,sprite,graphics
from pyglet.math import Vector2
from math import sin, radians, degrees, copysign
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
        shapes.Line( 83 ,   2,830 ,   2 ,width=1, color=(20, 200, 20), batch=batch),
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
    rotation_angel=1
    line1=shapes.Line(350 , 110,390 , 110 ,width=1, color=(200, 20, 20), batch=car)
    def __init__(self,max_steering,max_acceleration,velocity,Carx,Cary):
        self.position = Vector2(Carx, Cary)
        self.max_acceleration = max_acceleration
        self.max_steering = max_steering
        self.velocity = Vector2(0.0, 0.0)
        self.acceleration = 0.0
        self.steering = 0.0
        self.brake_deceleration = 10
        self.free_deceleration = 2
    def update(self,Carx,Cary,rotation,sprite):
        sprite.update(x=Carx, y=Cary,rotation=rotation)
    def update(self, dt):
        self.velocity += (self.acceleration * dt, 0)
        self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))

        if self.steering:
            turning_radius = self.length / sin(radians(self.steering))
            angular_velocity = self.velocity.x / turning_radius
        else:
            angular_velocity = 0

        self.position += self.velocity.rotate(-self.angle) * dt
        self.angle += degrees(angular_velocity) * dt
