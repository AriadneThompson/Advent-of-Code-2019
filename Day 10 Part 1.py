# -*- coding: utf-8 -*-

import numpy as np

raw_asteroids = open("Day 10 Input.txt", "r").readlines()

HEIGHT = len(raw_asteroids)
WIDTH = len(raw_asteroids[0]) - 1 # Ignore the \n. 

asteroids = np.empty((HEIGHT, WIDTH), dtype=bool)

for y in range(HEIGHT):
    for x in range(WIDTH):
        if raw_asteroids[y][x] == "#":
            asteroids[y][x] = True
        else:
            asteroids[y][x] = False


            
def asteroids_visible_from(x, y):
    unique_angles = set()
    
    for j in range(HEIGHT):
        for i in range(WIDTH):
            if asteroids[j][i] and (i, j) != (x, y):
                unique_angles.add(np.angle(x - i + (y - j) * 1j))
                
    return len(unique_angles)



max_visible = 0
max_coords = None
            
for y in range(HEIGHT):
    for x in range(WIDTH):
        if asteroids[y][x]:
            visible = asteroids_visible_from(x, y)
            
            if visible > max_visible:
                max_visible = visible
                max_coords = (x, y)
                
print(str(max_coords) + ": " + str(max_visible))
                        

                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            