# -*- coding: utf-8 -*-

import numpy as np



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



for timestep in range(1000):
    for i, j in ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)):
        for k in range(3):
            if positions[i][k] > positions[j][k]:
                velocities[i][k] -= 1
                velocities[j][k] += 1
            elif positions[i][k] < positions[j][k]:
                velocities[i][k] += 1
                velocities[j][k] -= 1
                
    positions += velocities
    

    
potential_energy = np.sum(abs(positions), axis=1)
kinetic_energy = np.sum(abs(velocities), axis=1)
total_energy = sum(potential_energy * kinetic_energy)

print(total_energy)