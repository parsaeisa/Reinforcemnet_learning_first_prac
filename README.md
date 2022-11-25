# Reinforcemnet_learning_first_prac

## Steps : 

Determine spaces and actions .

Define an environment which can give us (next_state , reward) based on
(state , action) .

Find value of each state . This step is an algorithm that must converge . 
The convergence happens when the difference between new value and old value
of a state (in two subsequent iterations) is lower than a threshold .
* The value of terminal states are 0 .
* In each iteration the value is computed like this : 

```python
for action in environment.actions:
    next_state, reward = info[(state, action)]
    values.append(reward + environment.gamma * v[next_state])

v[state] = np.array(values).max()
```
In a state , per each action we compute the value and then we choose
their max . 

At last based on these values we find policy , which is a dictionary . 