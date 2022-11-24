# for defining environmets and rewards 
import math
from operator import truediv
from os import stat
import numpy as np

GRID_HEIGHT = 5
GRID_WIDTH = 5
TERMINAL_REWARD = 10

# for value iteration 
GAMMA = 1.0
TETHA = 1e-10


class GridWorld:
    def __init__(self, grid_size, items, gamma=0, threshold=0) -> None:

        self.constant_reward = -1
        # I think this is minus
        # because moving to another state 
        # exhaust us and is bad .
        self.gamma = gamma
        self.threshold = threshold
        self.grid_height = grid_size[0]
        self.grid_width = grid_size[1]
        self.items = items
        self.states = list(range(self.grid_width * self.grid_height))
        self.actions = ['Up', 'Down', 'Left', 'Right']

        self.next_state = {'Up': -self.grid_width, 'Down': self.grid_width, 'Left': -1, 'Right': 1}

        # This P takes (state , action ) and returns (new_state ,reward )
        # P gives us an information about the environment
        self.P = self.get_P()

    def get_P(self):
        P = {}

        # define rewards and next states  , for each state and each action in that space 
        for state in range(self.grid_width * self.grid_height):
            for action in self.actions:
                # compute next state
                next_state = state + self.next_state[action]

                # compute reward
                # based on base reward and fire or water states 
                reward = self.constant_reward
                if next_state in self.items["fire"]["loc"]:
                    reward += self.items["fire"]["reward"]

                elif next_state in self.items["water"]["loc"]:
                    reward += self.items["water"]["reward"]

                elif self.is_out_of_environment(next_state):
                    next_state = state

                # adding it to P 
                P[(state, action)] = (next_state, reward)
        return P

    def check_terminal(self, state):
        for item in self.items:
            if state in self.items[item]["loc"]:
                return True

        return False

    def is_out_of_environment(self, next_state):
        if next_state not in self.states:
            return True


def compute_policy(environment):
    '''
    this method consists two loops where :
    the first one finds value of each state
    the second one finds the best policy

    :param environment:
    :return:
    '''

    info = environment.get_P()

    v = np.zeros(environment.grid_width * environment.grid_height)
    converged = False

    # find best action
    # till conversion
    while not converged:
        DELTA = 0
        for state in environment.states:
            # if state is terminal , value is 0 
            if environment.check_terminal(state):
                v[state] = 0
                continue

            # else , find best action 
            old_v = v[state]
            rewards = []

            # most_valuable_action = 'U'
            for action in environment.actions:
                next_state, reward = info[(state, action)]
                rewards.append(reward + environment.gamma * v[next_state])

            v[state] = np.array(rewards).max()

            # check conversion condition
            # If the difference between old value and new value of a state is lower than a
            # determined threshold , the algorithm is converged .
            DELTA = max(DELTA, abs(old_v - v[state]))
            # print("delta : ", DELTA)
            if DELTA < environment.threshold:
                converged = True

    # Find the best policy .
    # Policy is a map from state to action
    policy = np.full(environment.grid_width * environment.grid_width, 'n')

    for state in environment.states:
        new_v = []
        for action in environment.actions:
            (next_state, reward) = info[(state, action)]
            new_v.append(reward + environment.gamma * v[state])

        new_v = np.array(new_v)
        best_value = new_v.max()
        best_action_idx = np.where(new_v == best_value)[0]
        best_action = environment.actions[best_action_idx[0]]
        policy[state] = best_action

        matrix_plotter(policy)

    return policy


def matrix_plotter(m):
    for i in range(0, 25, 5):
        for j in m[i:i + 5]:
            print(j, end=" ")
        print("\n")
    print("===========================\n")


if __name__ == '__main__':
    grid_size = (GRID_HEIGHT, GRID_WIDTH)
    items = {
        'fire': {'reward': -1 * TERMINAL_REWARD, 'loc': [12]},
        'water': {'reward': TERMINAL_REWARD, 'loc': [18]},
    }

    environment = GridWorld(grid_size, items, gamma=1, threshold=1e-10)

    policy = compute_policy(environment)
