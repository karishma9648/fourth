import numpy as np#numpy is used fornumerical operations (e.g., creatingand updating the Q-table)
import random#random is used for exploration (choosing random actions).
class QLearningAgent:#Define the Q-learning Agent Class
 #The agent will learn which actions to take in different states based on rewards.
 def __init__(self, state_size, 
action_size, learning_rate=0.1, 
discount_factor=0.99, 
exploration_rate=1.0, 
min_exploration=0.01, 
decay_rate=0.995):
  self.state_size = state_size
  self.action_size = action_size
  self.learning_rate =learning_rate
  self.discount_factor = discount_factor
  self.exploration_rate = exploration_rate
  self.min_exploration = min_exploration
  self.decay_rate = decay_rate
  self.q_table = np.zeros((state_size, action_size))
        #This is the constructor method that initializes the agent’s attributes.
'''
        state_size: Number of possible states.
        action_size: Number of possible actions.
        learning_rate (α): Controls how much new knowledge overrides old knowledge.
        discount_factor (γ):
        Determines how much future rewards matter.
        exploration_rate (ε): Probability of taking a random action (used in exploration vs. exploitation).
        min_exploration: The lowest value that exploration_rate can decay to.
        decay_rate: The rate at which exploration_rate decreases over time.
        The Q-table is a 2D array (size: state_size × action_size).
        It stores values for each (state, action) pair, initially set to 0.
        The Q-values will be updatedduring learning.
        '''
def choose_action(self, state):
        if random.uniform(0, 1) <self.exploration_rate:
      return 
random.choice(range(self.action_size ))  # Explore
        else: 
             return 
np.argmax(self.q_table[state])  # Exploit
        #The state is converted intoa discrete val ue (to avoid indexing errors in q_table).
        #With probability exploration_rate, the agent picks a random action (trying new things).
        #This is important in the early stages when the agent has little knowledge
        #The agent selects the action with the highest Q-value in the current state.
        #This is done when the agent is more confident in its knowledge
def learn(self, state, action, 
reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + self.discount_factor * self.q_table[next_state][best_next_a ction]
        self.q_table[state][action] += self.learning_rate * (td_target self.q_table[state][action])
        self.exploration_rate = max(self.min_exploration, self.exploration_rate * self.decay_rate)
        #Learn from Experience (Update Q-table)
        #Convert states into valid discrete indices (to avoid out-of-bounds errors)
        #Find the best next action by selecting the action with the highest Q-value in next_state
 #  Define agent AFTER class is defined
 #Defines state_size and action_size and creates an instance of QLearningAgent.
state_size = 10
action_size = 4
agent = QLearningAgent(state_size, action_size)  # No error now!
state = 0  # Example state (must be within the state space range)
action = agent.choose_action(state) 
# Get action
print("Chosen Action:", action)
 #tests the choose_action method by providing a state (3.7).
 #Since state is continuous, it is 
converted into a valid integer 
before being used.
 #The chosen action is printed.
 #Summary
 #Agent stores Q-values for different
 (state, action) pairs in a table.
 #Uses exploration (random) vs. 
exploitation (best known action) to 
choose actions.
 #Updates Q-values using the Bellman 
equation after receiving rewards.
 #Gradually shifts from exploring to 
exploiting by decaying 
exploration_rate