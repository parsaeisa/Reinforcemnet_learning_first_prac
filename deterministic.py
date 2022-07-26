# for defining environmets and rewards 
GRID_HEIGHT = 5
GRID_WIDTH = 5
TERMINAL_REWARD = 10 

# for value iteration 
GAMMA = 1.0
TETHA = 1e-10

class GridWorld :
    def __init__(self,grid_size , items) -> None:
        
        self.constant_reward = -1 
        # I think this is minus
        # because moving to another state 
        # exhaust us and is bad .

        self.grid_size = grid_size
        self.items = items


    def get_P (self):
        self.P = {}

        # define rewards and next states 

def compute_policy ():
    # find best action 
    # till conversion 


    # find best policy 


if __name__ == '__main__' :
    grid_size = (GRID_HEIGHT , GRID_WIDTH)
    items = {
        'fire' : {'reward': -1 * TERMINAL_REWARD , 'loc' : (2,2)},
        'water' : {'reward': TERMINAL_REWARD , 'loc' : (3,3)},
    }

    environment = GridWorld(grid_size , items )