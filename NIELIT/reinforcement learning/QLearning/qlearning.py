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
Q = np.zeros((num_states, num_actions))
#Q-table (Q): A 10 × 4 matrix initialized with zeros
#Rows represent states (0 to 9).
#Columns represent actions (0 to 3).
#why?:Initially, the agent has no knowledge of the environment,
#so all Q-values start at 0.
print(Q)