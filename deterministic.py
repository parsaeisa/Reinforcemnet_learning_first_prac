# for defining environmets and rewards 
GRID_HEIGHT = 5
GRID_WIDTH = 5
TERMINAL_REWARD = 10 

# for value iteration 
GAMMA = 1.0
TETHA = 1e-10

class GridWorld :
    def __init__(self,grid_size , items, grid_height , grid_width) -> None:
        
        self.constant_reward = -1 
        # I think this is minus
        # because moving to another state 
        # exhaust us and is bad .

        self.grid_height = grid_height
        self.grid_width = grid_width
        self.items = items
        self.states = list(range(self.grid_width * self.grid_height))
        self.actions = ['Up' , 'Down', 'Left', 'Right']    

        self.next_state = {'Up': -self.grid_width , 'Down': self.grid_width, 'Left':-1, 'Right':1}

    def get_P (self):
        self.P = {}

        # define rewards and next states  , for each state and each action in that space 
        for state in range(self.grid_width * self.grid_height) :            
            for action in self.actions : 
                # compute next state
                next_state = state + self.next_state[action]

                # compute reward
                # based on base reward and fire or water states 
                reward = self.constant_reward
                if next_state in self.items["fire"]["loc"] :
                    reward -= self.items["fire"]["reward"]

                if next_state in self.items["water"]["loc"] :
                    reward += self.items["water"]["reward"]
    
                # adding it to P 
                self.P[(state , action)] = (next_state , reward )
        return self.P

def compute_policy ():
    # find best action 
    # till conversion 


    # find best policy 
    pass

if __name__ == '__main__' :
    grid_size = (GRID_HEIGHT , GRID_WIDTH)
    items = {
        'fire' : {'reward': -1 * TERMINAL_REWARD , 'loc' : [12]},
        'water' : {'reward': TERMINAL_REWARD , 'loc' : [18]},
    }

    environment = GridWorld(grid_size , items )