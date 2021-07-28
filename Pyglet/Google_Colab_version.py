




from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.models import Sequential, load_model
from collections import deque
from tensorflow.keras import optimizers
import numpy as np
import tensorflow as tf
tf.config.experimental.enable_mlir_graph_optimization()
import os
os.environ["MLIR_CRASH_REPRODUCER_DIRECTORY"]='enable'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'
class ReplayBuffer(object):
    def __init__(self, max_size, input_shape, n_actions, discrete=False):
        self.mem_size = max_size
        self.mem_cntr = 0
        self.discrete = discrete
        self.state_memory = np.zeros((self.mem_size, input_shape))
        self.new_state_memory = np.zeros((self.mem_size, input_shape))
        dtype = np.int8 if self.discrete else np.float32
        self.action_memory = np.zeros((self.mem_size, n_actions), dtype=dtype)
        self.reward_memory = np.zeros(self.mem_size)
        self.terminal_memory = np.zeros(self.mem_size, dtype=np.float32)

    def store_transition(self, state, action, reward, state_, done):
        index = self.mem_cntr % self.mem_size
        self.state_memory[index] = state
        self.new_state_memory[index] = state_
        # store one hot encoding of actions, if appropriate
        if self.discrete:
            actions = np.zeros(self.action_memory.shape[1])
            actions[action] = 1.0
            self.action_memory[index] = actions
        else:
            self.action_memory[index] = action
        self.reward_memory[index] = reward
        self.terminal_memory[index] = 1 - done
        self.mem_cntr += 1

    def sample_buffer(self, batch_size):
        max_mem = min(self.mem_cntr, self.mem_size)
        batch = np.random.choice(max_mem, batch_size)

        states = self.state_memory[batch]
        actions = self.action_memory[batch]
        rewards = self.reward_memory[batch]
        states_ = self.new_state_memory[batch]
        terminal = self.terminal_memory[batch]

        return states, actions, rewards, states_, terminal

class DDQNAgent(object):
    def __init__(self, alpha, gamma, n_actions, epsilon, batch_size,input_dims, epsilon_dec=0.999995,  epsilon_end=0.10,mem_size=25000, fname='ddqn_model.h5', replace_target=25):
        self.action_space = [i for i in range(n_actions)]
        self.n_actions = n_actions
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_dec = epsilon_dec
        self.epsilon_min = epsilon_end
        self.batch_size = batch_size
        self.model_file = fname
        self.replace_target = replace_target
        self.memory = ReplayBuffer(mem_size, input_dims, n_actions, discrete=True)

        self.brain_eval = Brain(input_dims, n_actions, batch_size)
        self.brain_target = Brain(input_dims, n_actions, batch_size)


    def remember(self, state, action, reward, new_state, done):
        self.memory.store_transition(state, action, reward, new_state, done)

    def choose_action(self, state):

        state = np.array(state)
        state = state[np.newaxis, :]

        rand = np.random.random()
        if rand < self.epsilon:
            action = np.random.choice(self.action_space)
        else:
            actions = self.brain_eval.predict(state)
            action = np.argmax(actions)

        return action

    def learn(self):
        if self.memory.mem_cntr > self.batch_size:
            state, action, reward, new_state, done = self.memory.sample_buffer(self.batch_size)

            action_values = np.array(self.action_space, dtype=np.int8)
            action_indices = np.dot(action, action_values)

            q_next = self.brain_target.predict(new_state)
            q_eval = self.brain_eval.predict(new_state)
            q_pred = self.brain_eval.predict(state)

            max_actions = np.argmax(q_eval, axis=1)

            q_target = q_pred

            batch_index = np.arange(self.batch_size, dtype=np.int32)

            q_target[batch_index, action_indices] = reward + self.gamma*q_next[batch_index, max_actions.astype(int)]*done

            _ = self.brain_eval.train(state, q_target)

            self.epsilon = self.epsilon*self.epsilon_dec if self.epsilon > self.epsilon_min else self.epsilon_min


    def update_network_parameters(self):
        self.brain_target.copy_weights(self.brain_eval)

    def save_model(self):
        self.brain_eval.model.save(self.model_file,save_format='h5')
        
    def load_model(self):
        self.brain_eval.model = load_model(self.model_file)
        self.brain_target.model = load_model(self.model_file)
        if self.epsilon == 0.0:
            self.update_network_parameters()

class Brain:
    def __init__(self, NbrStates, NbrActions, batch_size = 256):
        self.NbrStates = NbrStates
        self.NbrActions = NbrActions
        self.batch_size = batch_size
        self.model = self.createModel()
        
    
    def createModel(self):
        model=tf.keras.Sequential()
        model.add(tf.keras.layers.Dense(256, activation=tf.nn.relu)) #prev 256 
        model.add(tf.keras.layers.Dense(self.NbrActions, activation=tf.nn.softmax))
        model.compile(loss = "categorical_crossentropy", optimizer='sgd',metrics=['accuracy'])
        model.build((512, 10))
        model.summary()
        return model
    
    def train(self, x, y, epoch = 1, verbose = 0):
        self.model.fit(x, y, batch_size = self.batch_size , verbose = verbose)

    def predict(self, s):
        return self.model.predict(s)

    def predictOne(self, s):
        return self.model.predict(tf.reshape(s, [1, self.NbrStates])).flatten()
    
    def copy_weights(self, TrainNet):
        variables1 = self.model.trainable_variables
        variables2 = TrainNet.model.trainable_variables
        for v1, v2 in zip(variables1, variables2):
            v1.assign(v2.numpy())














from pyglet import graphics,window,clock,app,options
from math import cos,sin,pi
import numpy as np
from collections import deque
import random, math

##################### set game env ##################

TOTAL_GAMETIME = 1000 # Max game time for one episode
N_EPISODES = 5001
Episodes_counter = 0
REPLACE_TARGET = 50 
GameTime = 0 
GameHistory = []
ddqn_agent = DDQNAgent(alpha=0.0005, gamma=0.99, n_actions=5, epsilon=1.00, epsilon_end=0.10, epsilon_dec=0.9995, replace_target= REPLACE_TARGET, batch_size=512, input_dims=10)

# if you want to load the existing model uncomment this line.
# careful an existing model might be overwritten
#ddqn_agent.load_model()

ddqn_scores = []
eps_history = []
observation = []
#game state
done=True
reward=0
score = 0
counter = 0
gtime = 0 
first_game=True
learnning_started=False
from pyglet import text
from math import cos,sin,pi
def set_track():
    return [
        Line(100 , 350,470 , 452 ,width=1, color=(20, 200, 20)),
        Line(175 , 291,489 , 372 ,width=1, color=(20, 200, 20)),
        Line(100 , 350, 98 , 196 ,width=1, color=(20, 200, 20)),
        Line(175 , 291,175 , 192 ,width=1, color=(20, 200, 20)),
        Line( 98 , 196,  4 , 119 ,width=1, color=(20, 200, 20)),
        Line(175 , 192, 97 , 119 ,width=1, color=(20, 200, 20)),
        Line(  4 , 119, 83 ,   2 ,width=1, color=(20, 200, 20)),
        Line( 97 , 119,137 ,  70 ,width=1, color=(20, 200, 20)),
        Line( 83 ,   2,830 ,   2 ,width=1, color=(20, 20, 200)),
        Line(137 ,  70,780 ,  70 ,width=1, color=(20, 200, 20)),
        Line(830 ,   2,855 ,  30 ,width=1, color=(20, 200, 20)),
        Line(855 ,  30,855 , 110 ,width=1, color=(20, 200, 20)),
        Line(855 , 110,830 , 140 ,width=1, color=(20, 200, 20)),
        Line(830 , 140,200 , 140 ,width=1, color=(20, 200, 20)),
        Line(470 , 452,558 , 452 ,width=1, color=(20, 200, 20)),
        Line(558 , 452,825 , 220 ,width=1, color=(20, 200, 20)),
        Line(489 , 372,717 , 218 ,width=1, color=(20, 200, 20)),
        Line(826 , 222,829 , 141 ,width=1, color=(20, 200, 20)),
        Line(175 , 191,716 , 218 ,width=1, color=(20, 200, 20))]
class Line:
    def __init__(self,x,y,x2,y2,width,color):
        self.x=x
        self.y=y
        self.x2=x2
        self.y2=y2
        self.width=width
        self.color=color
class Circle:
    def __init__(self,x,y,o,color):
        self.x=x
        self.y=y
        self.o=o
        self.color=color
class Image:
    width=0
    height=0
    anchor_x=0
    anchor_y=0
    def __init__(self,src):
        self.src=src
class Sprite:
    rotation=270
    opacity=100
    def __init__(self,src,x,y):
        self.src=src
        self.x=x
        self.y=y
    def update(self,x,y,rotation):
        self.x=x
        self.y=y
        self.rotation=rotation
class text:
    def __init__(self,text,font_name,font_size,x, y):
        self.text=text
        self.font_name=font_name
        self.font_size=font_size
        self.x=x
        self.y=y
class Set_car:
    image=Image('unnamed.png')
    Carx=371
    Cary=102
    image.width=20
    image.height=40
    image.anchor_x = 10
    image.anchor_y = 20
    sprite = Sprite(image, x = Carx, y = Cary)
    sprite.rotation=270
    sprite.opacity=100
    lines=[
    [Line(Carx-20 , Cary+10,Carx-119 , Cary+10,width=1, color=(255,255,255)),Circle(Carx-90 , Cary+10, 3, color=(50, 225, 30)),True,text('',font_name='Times New Roman',font_size=15,x=948, y=485)],
    [Line(Carx-20 , Cary-10,Carx-119 , Cary-10,width=1, color=(255,255,255)),Circle(Carx-90 , Cary-10, 3, color=(50, 225, 30)),True,text('',font_name='Times New Roman',font_size=15,x=948, y=470)],
    [Line(Carx-20 , Cary+10,Carx-60 , Cary+60,width=1, color=(255,255,255)),Circle(Carx-60 , Cary+60, 3, color=(50, 225, 30)),True,text('',font_name='Times New Roman',font_size=15,x=948, y=455)],
    [Line(Carx-20 , Cary-10,Carx-60 , Cary-60,width=1, color=(255,255,255)),Circle(Carx-60 , Cary-60, 3, color=(50, 225, 30)),True,text('',font_name='Times New Roman',font_size=15,x=948, y=440)],
    [Line(Carx+20 , Cary+10,Carx+119 , Cary+10,width=1, color=(255,255,255)),Circle(Carx+90 , Cary+10, 3, color=(50, 225, 30)),True,text('',font_name='Times New Roman',font_size=15,x=948, y=425)],
    [Line(Carx+20 , Cary-10,Carx+119 , Cary-10,width=1, color=(255,255,255)),Circle(Carx+90 , Cary-10, 3, color=(50, 225, 30)),True,text('',font_name='Times New Roman',font_size=15,x=948, y=410)],
    [Line(Carx+20 , Cary+10,Carx+60 , Cary+60,width=1, color=(255,255,255)),Circle(Carx+60 , Cary+60, 3, color=(50, 225, 30)),True,text('',font_name='Times New Roman',font_size=15,x=948, y=395)],
    [Line(Carx+20 , Cary-10,Carx+60 , Cary-60,width=1, color=(255,255,255)),Circle(Carx+60 , Cary-60, 3, color=(50, 225, 30)),True,text('',font_name='Times New Roman',font_size=15,x=948, y=380)],
    [Line(Carx+ 5 , Cary+10,Carx+ 5 , Cary+60,width=1, color=(255,255,255)),Circle(Carx+ 5 , Cary+60, 3, color=(50, 225, 30)),True,text('',font_name='Times New Roman',font_size=15,x=948, y=365)],
    [Line(Carx+ 5 , Cary-10,Carx+ 5 , Cary-60,width=1, color=(255,255,255)),Circle(Carx+ 5 , Cary-60, 3, color=(50, 225, 30)),True,text('',font_name='Times New Roman',font_size=15,x=948, y=350)]
    ]
    car_shape=[
        Line( 353  ,  111 , 389  , 111  ,width=1, color=(20, 200, 20)),
        Line( 353  ,  96 , 389  , 96  ,width=1, color=(20, 200, 20)),
        Line( 354  ,  108 , 352  , 97  ,width=1, color=(20, 200, 20)),
        Line( 389  ,  109 , 389  , 96  ,width=1, color=(20, 200, 20))
    ]
    for line in lines:
        line[1].opacity=0
        line[0].opacity=0
        line[3].color = (100, 255, 100, 255)
    for line in car_shape:
        line.opacity=0
    lines_coord=[[line[0].x-370,line[0].y-102,line[0].x2-370,line[0].y2-102] for line in lines]
    car_body=[[line.x-371,line.y-102,line.x2-370,line.y2-102] for line in car_shape]
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
            line[1].opacity=0
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
        return [float(x[i][3].text) for i in range(len(x))]
def SetGoals():
    return [
        [Line( 310  ,  139 , 310  , 72  ,width=1, color=(200,20, 20)),True],
        [Line( 250  ,  139 , 250  , 72  ,width=1, color=(200,20, 20)),False],
        [Line( 208  ,  139 , 205  , 72  ,width=1, color=(200,20, 20)),False],
        [Line( 198  ,  143 , 176  , 192  ,width=1, color=(200,20, 20)),False],
        [Line( 377  ,  143 , 372  , 201  ,width=1, color=(200,20, 20)),False],
        [Line( 547  ,  142 , 537  , 210  ,width=1, color=(200,20, 20)),False],
        [Line( 672  ,  142 , 656  , 216  ,width=1, color=(200,20, 20)),False],
        [Line( 716  ,  219 , 828  , 187  ,width=1, color=(200,20, 20)),False],
        [Line( 633  ,  276 , 692  , 335  ,width=1, color=(200,20, 20)),False],
        [Line( 512  ,  356 , 560  , 449  ,width=1, color=(200,20, 20)),False],
        [Line( 438  ,  360 , 428  , 439  ,width=1, color=(200,20, 20)),False],
        [Line( 256  ,  314 , 231  , 387  ,width=1, color=(200,20, 20)),False],
        [Line( 174  ,  291 , 100  , 353  ,width=1, color=(200,20, 20)),False],
        [Line( 173  ,  193 , 98  , 196  ,width=1, color=(200,20, 20)),False],
        [Line( 96  ,  120 , 6  , 119  ,width=1, color=(200,20, 20)),False],
        [Line( 136  ,  70 , 85  , 4  ,width=1, color=(200,20, 20)),False],
        [Line( 284  ,  69 , 284  , 7  ,width=1, color=(200,20, 20)),False],
        [Line( 443  ,  70 , 441  , 5  ,width=1, color=(200,20, 20)),False],
        [Line( 571  ,  71 , 571  , 5  ,width=1, color=(200,20, 20)),False],
        [Line( 715  ,  69 , 715  , 2  ,width=1, color=(200,20, 20)),False],
        [Line( 782  ,  71 , 854  , 72  ,width=1, color=(200,20, 20)),False],
        [Line( 709  ,  141 , 709  , 74  ,width=1, color=(200,20, 20)),False],
        [Line( 607  ,  139 , 607  , 73  ,width=1, color=(200,20, 20)),False],
        [Line( 473  ,  141 , 473  , 70  ,width=1, color=(200,20, 20)),False],
        [Line( 376  ,  139 , 375  , 72  ,width=1, color=(200,20, 20)),False],
    ]

from math import cos,sin,pi
rotation_angel=1
Tcrack_lines=set_track()
Track_gols=SetGoals()
Car=Set_car()
default_distance=Car.set_default_distance(Car.lines)

def car(carX,carY):
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
            line[1].opacity=1000
            line[1].x = x1 + (uA * (x2-x1))
            line[1].y = y1 + (uA * (y2-y1))
            line[3].text=str(format(((uA * (x2-x1))**2+(uA * (y2-y1)**2))**0.5, ".2f"))
            return ((uA * (x2-x1))**2+(uA * (y2-y1)**2))**0.5
        else:
            return x1 + (uA * (x2-x1)),y1 + (uA * (y2-y1))
    else:
        return False
def resetgame():
    Car.Carx=371
    Car.Cary=102
    Car.sprite.rotation=270
    Car.set_default_distance(Car.lines)
    for _ in range(len(Track_gols)):
        Track_gols[_][1]=False
    Track_gols[0][1]=True  
def on_text(action):
    global rotation_angel
    if action==1:
        car(0,Car.velocity)
        if Car.velocity<20:
            Car.velocity+=1
    if action==2:
        car(0,Car.velocity)
        if Car.velocity>-20 :
            Car.velocity-=1
    if action==3:
        car(-Car.velocity,Car.velocity)
        if rotation_angel>1:
            rotation_angel-=1
    if action==4:
        car(Car.velocity,Car.velocity)
        if rotation_angel>1:
            rotation_angel-=1
def step(action):
    global Car,rotation_angel
    reward=0
    done=False
    if action==0:
        pass
    on_text(action)
    if action!=1 and Car.velocity>0 :
        Car.velocity-=0.5
        car(0,Car.velocity)
    if action!=2 and Car.velocity<0:
        Car.velocity+=0.5
        car(0,Car.velocity)
    if (action!=3 and action!=4) and rotation_angel<10:
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
                reward-=1
                print('crush')
                done = True
    
    for _ in range(len(Track_gols)):
        for i in range(len(Car.car_shape)):
            if (hover(False,Track_gols[_][0].x2,Track_gols[_][0].y2,Track_gols[_][0].x,Track_gols[_][0].y,\
                Car.car_shape[i].x2,Car.car_shape[i].y2,Car.car_shape[i].x,Car.car_shape[i].y)) and Track_gols[_][1]:
                Track_gols[_][1]=False
                reward+=1
                print('reward_added')
                if _+1==len(Track_gols):
                    Track_gols[0][1]=True
                else:
                    Track_gols[_+1][1]=True
                break;
    for i in range(0,len(distence)):
        if distence[i]==default_distance[i]:
            Car.lines[i][2]=True
    if done :
        distence=None
    return distence,reward,done
def run():
    global reward
    for e in range(N_EPISODES):
        
        resetgame() #reset env 
        done = False
        score = 0
        counter = 0
        reward=0
        observation_, reward, done = step(0)
        observation = np.array(observation_)
        gtime = 0 # set game time back to 0
        list_action=[]
        while not done:
            action = ddqn_agent.choose_action(observation)
            observation_, reward, done = step(action)
            observation_ = np.array(observation_)
            list_action.append(action)
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
        eps_history.append(ddqn_agent.epsilon)
        ddqn_scores.append(score)
        avg_score = np.mean(ddqn_scores[max(0, e-100):(e+1)])

        if e % REPLACE_TARGET == 0 and e > REPLACE_TARGET:
            ddqn_agent.update_network_parameters()

        if e % 10 == 0 and e > 10:
            ddqn_agent.save_model()
            print("save model")
            
        print('episode: ', e,'score: %.2f' % score,' average score %.2f' % avg_score,' epsolon: ', ddqn_agent.epsilon,' memory size', ddqn_agent.memory.mem_cntr % ddqn_agent.memory.mem_size)
run()


