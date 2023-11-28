import numpy as np
from player import Player 

class QLearningAgent(Player):

    def __init__(self, state_space_size, action_space_size=2, learning_rate=0.1, discount_factor=0.9, exploration_prob=0.1):
        self.state_space_size = state_space_size
        self.action_space_size = action_space_size
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_prob = exploration_prob
        self.q_table = np.zeros((state_space_size, action_space_size))

    def choose_action(self, state):
        # Explore
        if np.random.rand() < self.exploration_prob:
            return np.random.choice(self.action_space_size)
        
        # Exploit
        else:    
            return np.argmax(self.q_table[state, :])
        
    def update_q_table(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state, :])
        q_value = self.q_table[state, action]
        next_q_value = self.q_table[next_state, best_next_action]
        updated_q_value = q_value + self.learning_rate * (reward + self.discount_factor * next_q_value - q_value)
        self.q_table[state, action] = updated_q_value

def simulate_environment(current_state, action):
    # Perform the selected action in the current state and observe the consequences

    # Simulate the consequences of the action
    next_state = perform_action(current_state, action)

    # Get the reward based on the new state
    reward = calculate_reward(next_state)

    # Check if the game is over based on the new state (adapt to your specific Clue game logic)
    game_over = is_game_over(next_state)

    return next_state, reward, game_over

def perform_action(current_state, action):
    # Define how the environment changes based on the chosen action
    
    next_state = current_state + action # perform action "accuse" or "suggest" and update state

    return next_state

def calculate_reward(state):
    # Define how the agent is rewarded based on the current state
    # positive rewards for correct moves
    # negative rewards for incorrect ones

    # SPECIFY IN MROE DETAIL
    if state == goal_state: # WON
        return 1.0  # Positive reward for reaching the goal state
    else: # LOST
        return 0.0  # No reward for other states

def is_game_over(state):
    # Define the conditions for the game to be over based on the current state
    return state == terminal_state # how does the state/hand look when won 
   

q_agent = QLearningAgent(state_space_size=2)
#state_space_size = all possible configurations or situations game can be in -- maybe each player's hands? 
#action_space_size = 2? becuase can jsut accuse or suggest 

for episode in range(1000):
    
    state = 0 #reset game -- done in game implementation 

    while not game_over: # while no one has won (make more explicit) 
        
        action = q_agent.choose_action(state)

        # Simulate the environment and get the next state and reward
        next_state, reward, game_over = simulate_environment(state, action)

        # Update the Q-table
        q_agent.update_q_table(state, action, reward, next_state)

        # Move to the next state
        state = next_state

