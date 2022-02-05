from pyglet import graphics,window,clock,app,options,shapes,text
from Track import set_track,SetGoals
from Car import Set_car,Set_car1
from math import cos,sin,pi
import numpy as np
from agent import DDQNAgent

##################### set game env ##################

TOTAL_GAMETIME = 1000 # Max game time for one episode
N_EPISODES = 5001
Episodes_counter = 0
REPLACE_TARGET = 50
GameHistory = []
ddqn_agent = DDQNAgent(alpha=0.0005, gamma=0.99, n_actions=6, epsilon=1.00, epsilon_end=0.10, epsilon_dec=0.9995, replace_target= REPLACE_TARGET, batch_size=64, input_dims=10,fname='ddqn_model.h5')
#ddqn_agent = DDQNAgent(alpha=0.0005, gamma=0.99, n_actions=6, epsilon=0.1, epsilon_end=0.01, epsilon_dec=0.999, replace_target= REPLACE_TARGET, batch_size=64, input_dims=10,fname='ddqn_model.h5')
# if you want to load the existing model uncomment this line.
# careful an existing model might be overwritten
'''ddqn_agent.load_model()
ddqn_agent.update_network_parameters()'''

ddqn_scores = []
eps_history = []



learnning_started=False
list_of_actions=[]
show_real_car=False

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
Car1=Set_car1()
default_distance=Car.set_default_distance(Car.lines)
start_button=shapes.BorderedRectangle(0, 460, 150, 40, color=(20, 200, 20),border_color=(200,20,20),batch=button)
start_button.opacity=150
button_text=text.Label('start learning',font_name='Times New Roman',font_size=16,x=10, y=475,batch=button,color=(255,255,255,255))
#################################
def on_mouse_press(x,y, button, modifier):
    global learnning_started
    if 0<x<150 and 460<y<500 :
        learnning_started=not learnning_started
    if learnning_started:
        button_text.text='Stop learning'
    else :
        button_text.text='Start learning'
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
    Car1.car1.draw()
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
    global rotation_angel,Car
    Car.Carx=371
    Car.Cary=102
    Car.sprite.rotation=-90
    Car.velocity=0
    rotation_angel=1
    Car=Set_car()
    Car.update(Car.sprite.rotation,Car.sprite)
    for _ in range(len(Track_gols)):
        Track_gols[_][1]=False
    Track_gols[0][1]=True
    for _ in keyboard:
        keyboard[_]=False
    for _ in range(len(Track_gols)):
        if Track_gols[_][1]:
            Track_gols[_][0].color=(20,200,20)
        else:
            Track_gols[_][0].color=(200,20,20)
    return Car.set_default_distance(Car.lines),0,False
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
                if bytf and not done:
                    reward-=1
                    done = True
                    print('Crush -1')
    x=True
    for _ in range(len(Track_gols)):
        for i in range(len(Car.car_shape)):
            if (hover(False,Track_gols[_][0].x2,Track_gols[_][0].y2,Track_gols[_][0].x,Track_gols[_][0].y,\
                Car.car_shape[i].x2,Car.car_shape[i].y2,Car.car_shape[i].x,Car.car_shape[i].y)) and Track_gols[_][1]:
                Track_gols[_][1]=False
                if bytf and x:
                    reward+=1
                    print('Reward +1')
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
    if done:
            distence = None
    return distence,reward,done
def step(action,bytf=False):
    if action==0:
        pass
    if action==1:
        keyboard[window.key.MOTION_UP]=True
        keyboard[window.key.MOTION_DOWN]=False
    elif action==2:
        keyboard[window.key.MOTION_DOWN]=True
        keyboard[window.key.MOTION_UP]=False
    elif action==3:
        keyboard[window.key.MOTION_LEFT]=True
        keyboard[window.key.MOTION_RIGHT]=False
    elif action==4:
        keyboard[window.key.MOTION_RIGHT]=True
        keyboard[window.key.MOTION_LEFT]=False
    elif action ==5:
        keyboard[window.key.MOTION_RIGHT]=False
        keyboard[window.key.MOTION_LEFT]=False
    elif action==6:
        keyboard[window.key.MOTION_DOWN]=False
        keyboard[window.key.MOTION_UP]=False
    return on_text_motion(bytf)




def run_agent(dt):
    global learnning_started,Episodes_counter,show_real_car,list_of_actions
    if learnning_started and Episodes_counter<N_EPISODES and not show_real_car:
        #hide the real car
        Car.sprite.opacity=0
        Car1.sprite.opacity=1000
        Episodes_counter+=1
        done = False
        score = 0
        counter = 0
        observation_, reward, done = resetgame()#reset env
        observation = np.array(observation_)
        gtime = 0   # set game time back to 0
        list_of_actions=[]#for the user to see the game in 60fps we store the action and dispaly them later on
        while not done:
            action = ddqn_agent.choose_action(observation)
            observation_, reward, done = step(action,True)
            observation_ = np.array(observation_)
            list_of_actions.append(action)
        # This is a countdown if no reward is collected the car will be done within 100 ticks
            if reward == 0:
                counter += 1
                if counter > 1000:
                    done = True
                    print('no reward has been collected')
            else:
                counter = 0
            score += reward

            ddqn_agent.remember(observation, action, reward, observation_, int(done))
            observation = observation_
            ddqn_agent.learn()
            
            gtime += 1

            if gtime >= TOTAL_GAMETIME:
                done = True
                print('timeout ')
        eps_history.append(ddqn_agent.epsilon)
        ddqn_scores.append(score)
        avg_score = np.mean(ddqn_scores[max(0, Episodes_counter-100):(Episodes_counter+1)])
        if Episodes_counter% REPLACE_TARGET == 0 and Episodes_counter> REPLACE_TARGET:
            ddqn_agent.update_network_parameters()
        if Episodes_counter% 10 == 0 and Episodes_counter> 10:
            ddqn_agent.save_model()
            print("model saved")
        print('episode: ', Episodes_counter,'score: %.2f' % score,\
                ' average score %.2f' % avg_score,' epsolon: ',\
                ddqn_agent.epsilon,' memory size',\
                ddqn_agent.memory.mem_cntr % ddqn_agent.memory.mem_size)
        print('-------------------------------------------------------------------------------')
        resetgame()
        show_real_car=True
def render_game(dt):
    global show_real_car,list_of_actions
    if show_real_car:
        Car.sprite.opacity=1000
        Car1.sprite.opacity=0
        d,b,done=step(list_of_actions[0],True)
        if done or  list_of_actions==[]:
            Car.sprite.opacity=0
            Car1.sprite.opacity=1000
            show_real_car=False
            print('-------------------------------------------------------------------------------')
        else:
            list_of_actions.pop(0)
clock.schedule_interval(render_game, 1/60)
clock.schedule_interval(run_agent, 1/60)

app.run()
