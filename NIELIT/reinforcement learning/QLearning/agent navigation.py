import numpy as np 
import random
#define enviorment
num_states = 6
num_actions = 2
#define reward table
rewards = np.array([-1,-1,-1,-1,-1,10])

#define q table(initially zeros)
Q = np.zeros([num_states,num_actions])
print(Q)

#hyperparameters
alpha = 0.1
gamma = 0.9
epsilon = 0.2
def get_next_state(state,action):
    if action== 0: #move left
        return max(0,num_states -1)
    else:
        return min(num_states-1,states+1)
num_episodes=1000
for episodes in range(num_episodes):
    states = 0
while states !=num_states-1:
    if random.uniform(0,1)<epsilon:
        action= random.choice([0,1])
    else:
        action = np.argmax(Q[states])
    next_states = get_next_state(states,action)
    reward=rewards[next_states]
    Q[states,action] = Q[states,action] + alpha *(reward +gamma *np.max(Q[next_states , action]))
    states=next_states
    print('Trained Q table')
    print(Q)