# -*- coding: utf-8 -*-

import numpy as np

raw_asteroids = open("Day 10 Input.txt", "r").readlines()

HEIGHT = len(raw_asteroids)
WIDTH = len(raw_asteroids[0]) - 1 # Ignore the \n. 

# Position of the station
X, Y = 20, 18
#X, Y = 11, 13

EPSILON = 0.000001
            
            
def angle_to(x, y):
    return np.angle(y - Y + (x - X) * 1j)



asteroids = np.empty((HEIGHT, WIDTH), dtype=bool)

for y in range(HEIGHT):
    for x in range(WIDTH):
        if raw_asteroids[y][x] == "#":
            asteroids[y][x] = True
        else:
            asteroids[y][x] = False

# Don't count the station itself. 
asteroids[Y][X] = False
                


asteroid_data = []

for y in range(HEIGHT):
    for x in range(WIDTH):
        if asteroids[y][x]:
            # Data is angle from station, Manhattan distance to station, and coordinates. 
            # Use minus angle to order in the right direction. 
            asteroid_data.append((- angle_to(x, y), abs(X-x) + abs(Y-y), (x, y)))

# Sorts by angle first; on ties, sorts by Manhattan distance. 
asteroid_data.sort()



vapourised = 0
current_angle = 0

while vapourised < 200:
    surviving = []
    for asteroid in asteroid_data:
        if abs(asteroid[0] - current_angle) < EPSILON:
            surviving.append(asteroid)
        else:
            current_angle = asteroid[0]
            vapourised += 1
            #print("Vapourised asteroid #" + str(vapourised) + " at " + str(asteroid[-1]) + "!")
            if vapourised == 200:
                print(str(asteroid[-1]))
                break
            
    asteroid_data = surviving
            
    
                        

                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            