"""
AJUA environment
Created on October 23 2019
RL strategy for african board games
"""
import numpy as np


class AJUA():

    def __init__(self):
        self.state = np.zeros(18)
        self.current_player = 0
        self.done = False
        self.previous_num_stones = 0
        self.moves = 0
        self.agent_1_reward = 0
        self.agent_2_reward = 0
        for i in range(1,9):
            self.state[i]=3
        for i in range(10,18):
            self.state[i]=3

    def reset(self):
        '''
        Resets environment to start state
        '''
        self.state = np.zeros(18)
        self.current_player = 0
        self.done = False
        self.moves = 0
        self.agent_1_reward = 0
        self.agent_2_reward = 0
       
        for i in range(1,9):
            self.state[i]=3
        for i in range(10,18):
            self.state[i]=3
        return self.state


    def render(self):
        '''
        This function renders the environment
        '''
        state = self.state
        print("Stones:   ",str(state[0])+" : "+str(state[9]))
        print([(i+1, x )for i, x in enumerate(state[1:9])])
        print([(i+10, x )for i, x in enumerate(state[10:])])
 
    def step(self, action):
        '''
        This function takes an action in the environment
        '''
        self.moves += 1
        reward = 0
        current_index = action
        number_stones = int(self.state[current_index])
        if current_index == 0 or current_index ==9:
            pass
        else:
            # if move is valid
            if number_stones > 0:
                self.previous_num_stones = self.state[self.current_player]
                if self.current_player == 9:
                    self.current_player = 0
                else:
                    self.current_player = 9
                self.state[current_index] = 0
                for i in range(number_stones):
                    current_index += 1
                    if current_index == 18:
                        current_index = 0
                    if current_index == self.current_player:
                        #reward += 1
                        pass
                    self.state[current_index] +=1
            else:
                #invalid move
                reward = 0
        # if episode is finished
        if sum(self.state[1:9])==0 and sum(self.state[10:])==0:
            self.done = True 
        if self.moves > 300:
            self.done = True 
        if self.done:
            if self.state[0] > self.state[9]:
                self.agent_1_reward = 1
            if self.state[0] < self.state[9]:
                self.agent_2_reward = 1

        return self.state, reward,  self.done, ""

    def get_reward(self):
        '''
        This function gets the reward for the current player
        '''
        return self.state[self.current_player] - self.previous_num_stones