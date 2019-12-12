# -*- coding: utf-8 -*-

import numpy as np
from math import gcd



positions = np.array([[-14, -4, -11],
                      [-9,   6,  -7],
                      [ 4,   1,   4],
                      [ 2, -14,  -9]], 
                      dtype=np.int32)

#positions = np.array([[-1,   0,  2],
#                      [ 2, -10, -7],
#                      [ 4,  -8,  8],
#                      [ 3,   5, -1]], 
#                      dtype=np.int32)

velocities = np.zeros_like(positions)



def lcm2(x, y):
    """
    Least common multiple of two numbers. 
    """
    return x * y // gcd(x, y)
    

def lcm3(x, y, z):
    """
    Least common multiple of three numbers. 
    """
    return lcm2(x, lcm2(y, z))



time_to_repeat = []

for k in range(3):

    previous_states = set()
    
    while str(positions[:,k]) + str(velocities[:,k]) not in previous_states:
        previous_states.add(str(positions[:,k]) + str(velocities[:,k]))
        
        for i, j in ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)):
            if positions[i][k] > positions[j][k]:
                velocities[i][k] -= 1
                velocities[j][k] += 1
            elif positions[i][k] < positions[j][k]:
                velocities[i][k] += 1
                velocities[j][k] -= 1
                
        positions += velocities
        
    time_to_repeat.append(len(previous_states))
    
    
    
print(lcm3(time_to_repeat[0], time_to_repeat[1], time_to_repeat[2]))
    




























