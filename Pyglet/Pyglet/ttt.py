from pyglet import graphics,window,clock,app,options,shapes,text
from Track import set_track,Set_car,Set_car2
from math import cos,sin,pi
from Gols import SetGoals
import numpy as np
from agent_dqn import DDQNAgent
from collections import deque
import random, math

TOTAL_GAMETIME = 1000 # Max game time for one episode
N_EPISODES = 5001
Episodes_counter = 0
REPLACE_TARGET = 50 
GameTime = 0 
GameHistory = []
ddqn_agent = DDQNAgent(alpha=0.0005, gamma=0.999995, n_actions=6, epsilon=1.0, epsilon_end=0.01, batch_size=96, input_dims=10)
#ddqn_agent = DDQNAgent(alpha=0.0005, gamma=0.99, n_actions=5, epsilon=0.02, epsilon_end=0.01, epsilon_dec=0.999, replace_target= REPLACE_TARGET, batch_size=64, input_dims=10,fname='ddqn_model.h5')
# if you want to load the existing model uncomment this line.
# careful an existing model might be overwritten
ddqn_agent.load_model()
ddqn_agent.update_network_parameters()

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
list_of_actions=[]
render_actions=[]

for i in range(N_EPISODES):
    done = False
    score = 0
    observation = np.array([i/10 for j in range(10)])
    while not done:
        action = ddqn_agent.choose_action(observation)
        observation_, reward, done = np.array([i/10 for i in range(10)]),1,random.choice([True,False,False])
        score += reward
        ddqn_agent.remember(observation, action, reward, observation_, int(done))
        observation = observation_
        ddqn_agent.learn()
    eps_history.append(ddqn_agent.epsilon)

    ddqn_scores.append(score)

    avg_score = np.mean(ddqn_scores[max(0, i-100):(i+1)])
    print('episode: ', i,'score: %.2f' % score,
            ' average score %.2f' % avg_score)

    if i % 10 == 0 and i > 0:
        ddqn_agent.save_model()