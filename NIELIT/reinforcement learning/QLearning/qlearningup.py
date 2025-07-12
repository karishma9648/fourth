import numpy as np
import random
# Initialize parameters
alpha = 0.1   # Learning rate
#alpha (Learning Rate): Controls how much the Q-value is updated in each step.
#A small value (e.g., 0.1) makes learning gradual(slow), while a high value (1.0)
#updates immediately.
gamma = 0.9   # Discount factor
#gamma (Discount Factor): Determines how much future rewards influence current Q-values.
#gamma (Discount Factor): Determines how much future rewards influence current Q-values.
#A value close to 1 (e.g., 0.9) prioritizes long-term rewards.
epsilon = 0.1 # Exploration probability
#Sets the probability of exploring random actions in an ϵ-greedy strategy.
#With probability epsilon, selects a random action (exploration).
#Otherwise, selects the best known action (exploitation).
num_states = 10
num_actions = 4
#35
 #35
#Define the total number of states and actions in the 
#environment
Q = np.zeros((num_states, num_actions))
#Q-table (Q): A 10 × 4 matrix initialized with zeros
#Rows represent states (0 to 9).
#Columns represent actions (0 to 3).
#why?:Initially, the agent has no knowledge of the environment,
#so all Q-values start at 0.
#update
print(Q)

 #3




def q_learning_update(state, action, reward, next_state):
#Defines a function to update the Q-value for a given (state, action, reward, next_state)
#This function follows the Q-learning update rule:
#Q(s,a)←Q(s,a)+α[R+γ maxQ(s',a')-Q(s,a)]
    best_next_action = np.argmax(Q[next_state, :])

#Find the Best Next Action.Finds the action with the highest Q-value in next_state.
#why?:Q-learning is an off-policy algorithm that assumes the agent will follow the best policy
#in the future.
    print(best_next_action)

#Apply the Q-Learning Update Rule
    Q[state, action] += alpha * (reward + gamma * Q[next_state, best_next_action] - Q[state, action])
    print(Q[state, action])#0
#Q(2,1) += 0.1 * (10 + 0.9 * 0 - 0)
#Q(2,1) = 1.0
#The difference between these values is multiplied by alpha (learning rate) to
#update the Q-value gradually.
# Example update step
# Example update step
state, action, reward, next_state = 2, 1, 10, 3
q_learning_update(state, action, reward, next_state)
print(Q)#Prints the final Q-table after one update
