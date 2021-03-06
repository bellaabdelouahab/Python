from pyglet import graphics,window,clock,app,options,shapes,text
from Track import set_track,Set_car
from math import cos,sin,pi
from Gols import SetGoals
import numpy as np
from agent import DDQNAgent
from collections import deque
import random, math
##################### set game env ##################


TOTAL_GAMETIME = 1000 # Max game time for one episode
N_EPISODES = 10001
Episodes_counter = 0
REPLACE_TARGET = 50 
GameTime = 0 
GameHistory = []
ddqn_agent = DDQNAgent(alpha=0.0005, gamma=0.99, n_actions=3, epsilon=1.0, batch_size=64, input_dims=10)
#ddqn_agent = DDQNAgent(alpha=0.0005, gamma=0.99, n_actions=6, epsilon=0.5, epsilon_end=0.01,batch_size=64, input_dims=10)
# if you want to load the existing model uncomment this line.
# careful an existing model might be overwritten
ddqn_agent.load_model()
ddqn_agent.update_network_parameters()

ddqn_scores = []
eps_history = []
observation = []
list_of_actions=[]
renderFlag=False
#game state
learnning_started=False
#####################################################

windows = window.Window(1000,500)
options['debug_gl'] = False
keyboard = window.key.KeyStateHandler()
windows.push_handlers(keyboard)
rotation_angel=1
batch = graphics.Batch()
button = graphics.Batch()
Tcrack_lines=set_track(batch)
Track_gols=SetGoals(batch)
Car=Set_car()
default_distance=Car.set_default_distance(Car.lines)
start_button=shapes.BorderedRectangle(0, 460, 150, 40, color=(20, 200, 20),border_color=(200,20,20),batch=button)
start_button.opacity=150
button_text=text.Label('start learning',font_name='Times New Roman',font_size=16,x=10, y=475,batch=button,color=(255,255,255,255))
move_up=shapes.BorderedRectangle(782,464,30,30,color=(156,34,199),batch=button)
move_down=shapes.BorderedRectangle(782,428,30,30,color=(156,134,199),batch=button)
move_left=shapes.BorderedRectangle(746,428,30,30,color=(156,34,199),batch=button)
move_right=shapes.BorderedRectangle(818,428,30,30,color=(156,34,199),batch=button)
#################################
def on_mouse_press(x,y, button, modifier):
    global learnning_started
    #print current mouse position
    if 0<x<150 and 460<y<500 :
        learnning_started=not learnning_started
    if learnning_started:
        button_text.text='Stop learning'
    else :
        button_text.text='Start learning'
    print(x,y)
#################################
windows.on_mouse_press=on_mouse_press

def car(carX,carY):
    global Car
    Car.sprite.rotation+=carX/(rotation_angel*7)
    Car.Carx+=carY/10*cos((-Car.sprite.rotation+90)*pi/180)
    Car.Cary+=carY/10*sin((-Car.sprite.rotation+90)*pi/180)
    if abs(-Car.sprite.rotation+90)>=360:
        Car.sprite.rotation=90
    Car.update(Car.sprite.rotation,Car.sprite)
    return (Car.sprite.rotation,Car.Carx,Car.Cary)
def hover(line,x4,y4,x3,y3,x2,y2,x1,y1):
    if ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))==0:
        return False
    uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
    uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
    if uA >= 0 and uA <= 1 and uB >= 0 and uB <= 1:
        if line:
            line[2]=False
            line[1].x = x1 + (uA * (x2-x1))
            line[1].y = y1 + (uA * (y2-y1))
            line[3].text=str(format(((uA * (x2-x1))**2+(uA * (y2-y1)**2))**0.5, ".2f"))
            return ((uA * (x2-x1))**2+(uA * (y2-y1)**2))**0.5
        else:
            return x1 + (uA * (x2-x1)),y1 + (uA * (y2-y1))
    else:
        return False  
def on_draw():
    windows.clear()
    Car.car.draw()
    batch.draw()
    button.draw()
windows.on_draw=on_draw
def move():
    global Car,rotation_angel
    if keyboard[window.key.MOTION_DOWN]:
        car(0,Car.velocity)
        if Car.velocity>-20 :
            Car.velocity-=1
    if keyboard[window.key.MOTION_UP]:
        car(0,Car.velocity)
        if Car.velocity<20:
            Car.velocity+=1
    if keyboard[window.key.MOTION_LEFT]:
        car(-Car.velocity,0)
        if rotation_angel>1:
            rotation_angel-=1
    if keyboard[window.key.MOTION_RIGHT]:
        car(Car.velocity,0)
        if rotation_angel>1:
            rotation_angel-=1
def resetgame():
    global default_distance,rotation_angel
    Car.Carx=752
    Car.Cary=102
    Car.sprite.rotation=-90
    Car.velocity=0
    rotation_angel=1
    default_distance=Car.set_default_distance(Car.lines)
    for _ in range(len(Track_gols)):
        Track_gols[_][1]=False
    Track_gols[23][1]=True
    for _ in keyboard:
        keyboard[_]=False
    for _ in range(len(Track_gols)):
        if Track_gols[_][1]:
            Track_gols[_][0].color=(20,200,20)
        else:
            Track_gols[_][0].color=(200,20,20)
def on_text_motion(bytf=False):
    global Car,rotation_angel
    reward=0
    done=False
    for keys in keyboard:
        if keyboard[keys]:
            move()
    if not keyboard[window.key.MOTION_UP] and Car.velocity>0 :
        Car.velocity-=0.5
        car(0,Car.velocity)
    if not keyboard[window.key.MOTION_DOWN] and Car.velocity<0:
        Car.velocity+=0.5
        car(0,Car.velocity)
    if (not keyboard[window.key.MOTION_LEFT] and not keyboard[window.key.MOTION_RIGHT]) and rotation_angel<11:
        rotation_angel+=5
    distence=default_distance
    for i in range(0,len(Tcrack_lines)):
        for j in range(0,len(Car.lines)):
            x=(hover(Car.lines[j],Tcrack_lines[i].x2,Tcrack_lines[i].y2,Tcrack_lines[i].x,Tcrack_lines[i].y,\
                Car.lines[j][0].x2,Car.lines[j][0].y2,Car.lines[j][0].x,Car.lines[j][0].y))
            if x!=False:
                if distence[j] and x<distence[j] or not distence[j]:
                    distence[j]=x
        for j in range(len(Car.car_shape)):
            if(hover(False,Tcrack_lines[i].x2,Tcrack_lines[i].y2,Tcrack_lines[i].x,Tcrack_lines[i].y,\
                Car.car_shape[j].x2,Car.car_shape[j].y2,Car.car_shape[j].x,Car.car_shape[j].y)):
                if not done:
                    reward-=1
                    done = True
                    print('-1',end="")
    x=True
    for _ in range(len(Track_gols)):
        for i in range(len(Car.car_shape)):
            if (hover(False,Track_gols[_][0].x2,Track_gols[_][0].y2,Track_gols[_][0].x,Track_gols[_][0].y,\
                Car.car_shape[i].x2,Car.car_shape[i].y2,Car.car_shape[i].x,Car.car_shape[i].y)) and Track_gols[_][1]:
                Track_gols[_][1]=False
                if x:
                    print('+1',end="")
                    reward+=1
                    x=False
                if _+1==len(Track_gols):
                    Track_gols[0][1]=True
                else:
                    Track_gols[_+1][1]=True
                break;
    for _ in range(len(Track_gols)):
        if Track_gols[_][1]:
            Track_gols[_][0].color=(20,200,20)
        else:
            Track_gols[_][0].color=(200,20,20)
    for i in range(0,len(distence)):
        if distence[i]==default_distance[i]:
            Car.lines[i][2]=True
    distence=[(1000-distence[i])/1000 for i in range(len(distence))]
    if done:
        distence = None
    if(bytf):
        return distence,reward,done
    else:
        return done
def step(action,bytf=False):
    global move_up,move_down,move_left,move_right
    if action==5:
        keyboard[window.key.MOTION_UP]=True
        keyboard[window.key.MOTION_DOWN]=False
        move_up.color=(200,20,20)
        move_down.color=(156,134,199)
    elif action==4:
        keyboard[window.key.MOTION_DOWN]=True
        keyboard[window.key.MOTION_UP]=False
        move_down.color=(200,20,20)
        move_up.color=(156,34,199)
    elif action==0:
        keyboard[window.key.MOTION_LEFT]=True
        keyboard[window.key.MOTION_RIGHT]=False
        keyboard[window.key.MOTION_UP]=True
        move_left.color=(200,20,20)
        move_right.color=(156,34,199)
    elif action==1:
        keyboard[window.key.MOTION_RIGHT]=True
        keyboard[window.key.MOTION_LEFT]=False
        keyboard[window.key.MOTION_UP]=True
        move_right.color=(200,20,20)
        move_left.color=(156,34,199)
    elif action==2:
        keyboard[window.key.MOTION_RIGHT]=False
        keyboard[window.key.MOTION_LEFT]=False
        move_right.color=(156,34,199)
        move_left.color=(156,34,199)
    elif action==5:
        keyboard[window.key.MOTION_DOWN]=False
        keyboard[window.key.MOTION_UP]=False
        move_down.color=(156,134,199)
        move_up.color=(200,20,20)
    return on_text_motion(bytf)
def Train(dt):
    if learnning_started:
        global list_of_actions,renderFlag
        if not renderFlag:
            global Episodes_counter
            Episodes_counter+=1
            resetgame() #reset env 
            done = False
            score = 0
            counter = 0
            
            observation_= [(1000-i)/1000 for i in default_distance]
            observation = np.array(observation_)

            gtime = 0 # set game time back to 0
            
            renderFlag = True # if you want to render every episode set to true

            if Episodes_counter % 5 == 0 and Episodes_counter > 0: # render every 5 episodes
                renderFlag = True

            while not done:
                
                action = ddqn_agent.choose_action(observation)
                observation_, reward, done = step(action,True)
                observation_ = np.array(observation_)

                # This is a countdown if no reward is collected the car will be done within 100 ticks
                if reward == 0:
                    counter += 1
                    if counter > 100:
                        done = True
                else:
                    counter = 0

                score += reward

                ddqn_agent.remember(observation, action, reward, observation_, int(done))
                observation = observation_
                ddqn_agent.learn()
                
                gtime += 1

                if gtime >= TOTAL_GAMETIME:
                    done = True

                if renderFlag:
                    list_of_actions.append(action)

            eps_history.append(ddqn_agent.epsilon)
            ddqn_scores.append(score)
            avg_score = np.mean(ddqn_scores[max(0, Episodes_counter-100):(Episodes_counter+1)])

            if Episodes_counter % REPLACE_TARGET == 0 and Episodes_counter > REPLACE_TARGET:
                ddqn_agent.update_network_parameters()

            if Episodes_counter % 10 == 0 and Episodes_counter > 10:
                ddqn_agent.save_model()
                print("save model")
                
            print('episode: ', Episodes_counter,'score: %.2f' % score,
                ' average score %.2f' % avg_score,
                ' epsolon: ', ddqn_agent.epsilon,
                ' memory size', ddqn_agent.memory.mem_cntr % ddqn_agent.memory.mem_size) 
            if renderFlag:
                resetgame() 
            print('\n-------------------------------Render START--------------------------------------')
        else:
            done=False
            done=step(list_of_actions[0],False)
            if done:
                list_of_actions=[]
                resetgame()
                done=False
                renderFlag=False
                print('\n-------------------------------Render END----------------------------------------')
                return
            list_of_actions.pop(0)
            if list_of_actions==[]:
                resetgame()
                print('\n-------------------------------Render END--------------------------------------')
                renderFlag=False
                    

clock.schedule_interval(Train, 1/60)

def run_game():
    app.run()

###############################################################################################        
@windows.event
def on_mouse_press(x,y,button,modifiers):
    global learnning_started
    if not learnning_started:
        learnning_started=False
run_game()
