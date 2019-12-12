# -*- coding: utf-8 -*-

import numpy as np



raw_program = [3,8,1005,8,328,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,28,1,1003,10,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,54,2,1103,6,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,80,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,102,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,124,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,147,1006,0,35,1,7,3,10,2,106,13,10,2,1104,9,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,183,2,7,16,10,2,105,14,10,1,1002,12,10,1006,0,13,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,220,1006,0,78,2,5,3,10,1006,0,92,1006,0,92,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,1001,8,0,255,1006,0,57,2,1001,11,10,1006,0,34,2,1007,18,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1002,8,1,292,2,109,3,10,1,1103,14,10,2,2,5,10,2,1006,3,10,101,1,9,9,1007,9,997,10,1005,10,15,99,109,650,104,0,104,1,21101,932700762920,0,1,21101,0,345,0,1105,1,449,21102,1,386577306516,1,21102,356,1,0,1106,0,449,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,179355975827,0,1,21101,403,0,0,1106,0,449,21102,1,46413220903,1,21102,1,414,0,1106,0,449,3,10,104,0,104,0,3,10,104,0,104,0,21101,988224959252,0,1,21102,1,437,0,1106,0,449,21101,717637968660,0,1,21101,0,448,0,1106,0,449,99,109,2,22101,0,-1,1,21102,40,1,2,21101,480,0,3,21101,470,0,0,1106,0,513,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,475,476,491,4,0,1001,475,1,475,108,4,475,10,1006,10,507,1102,1,0,475,109,-2,2105,1,0,0,109,4,2102,1,-1,512,1207,-3,0,10,1006,10,530,21102,1,0,-3,22102,1,-3,1,22101,0,-2,2,21102,1,1,3,21101,0,549,0,1105,1,554,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,577,2207,-4,-2,10,1006,10,577,21202,-4,1,-4,1106,0,645,21202,-4,1,1,21201,-3,-1,2,21202,-2,2,3,21102,1,596,0,1106,0,554,21201,1,0,-4,21101,1,0,-1,2207,-4,-2,10,1006,10,615,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,637,21201,-1,0,1,21101,0,637,0,105,1,512,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]

program = {i: raw_program[i] for i in range(len(raw_program))}



def run(inputs, program_state):
    # Instruction pointer
    i = program_state["i"]
    
    program = program_state["program"]
    
    relative_base = program_state["relative base"]
    
    # Inputs pointer
    j = 0
    
    # Don't want to edit the original program! 
    program = program.copy()
    
    while True:
        opcode = program[i] % 100
        
        # Since we can now access memory outside the original program, it's 
        # easier just to calculate all three parameters, even if the opcode
        # has fewer. 
        # e.g. parameter 3 for opcode 4 will never be used, but we can still
        # calculate what it would be. 
        
        # First, get the index of each parameter. 
        param_indices = {}
        
        for k in (1, 2, 3):
            mode = (program[i] % 10 ** (k+2)) // (10 ** (k+1))
            
            if mode == 0:
                # Position mode
                param_indices[k] = program.get(i+k, 0)
                
            elif mode == 1:
                # Immediate mode
                param_indices[k] = i+k
                
            elif mode == 2:
                # Relative mode
                param_indices[k] = program.get(i+k, 0) + relative_base
                
            else:
                raise RuntimeError("Found unknown mode " + str(mode) + " at position " + str(i) + ".")
                
        # Then, get the parameter itself.
        params = {}
                
        for k in (1, 2, 3):
            params[k] = program.get(param_indices[k], 0)
            
        
        if opcode == 1:
            program[param_indices[3]] = params[1] + params[2]
            i += 4
            
        elif opcode == 2:
            program[param_indices[3]] = params[1] * params[2]
            i += 4
            
        elif opcode == 3:
            if type(inputs) == int:
                program[param_indices[1]] = inputs
            else:
                program[param_indices[1]] = inputs[j]
                j += 1
            
            i += 2
            
        elif opcode == 4:
            return params[1], {"program":program, "i":i + 2, "relative base":relative_base}
            i += 2
            
        elif opcode == 5:
            if params[1]:
                i = params[2]
            else:
                i += 3
                
        elif opcode == 6:
            if not params[1]:
                i = params[2]
            else:
                i += 3
                
        elif opcode == 7:
            program[param_indices[3]] = int(params[1] < params[2])
            i += 4
            
        elif opcode == 8:
            program[param_indices[3]] = int(params[1] == params[2])
            i += 4
            
        elif opcode == 9:
            relative_base += params[1]
            i += 2
            
        elif opcode == 99:
            return None
        
        else:
            raise RuntimeError("Found unknown opcode " + str(program[i]) + " at position " + str(i) + ".")
            
            

hull = {(0, 0): 1}

directions = np.array(((0, 1), (1, 0), (0, -1), (-1, 0)))
#                        up    right    down     left
direction_index = 0
coords = np.array([0, 0])

program_state = {"program": program, "i": 0, "relative base": 0}

while True:
    output = run(hull.get(tuple(coords), 0), program_state)
    
    if output is None:
        break
    
    colour, program_state = output
    
    turn_right, program_state = run(None, program_state)
    
    hull[tuple(coords)] = colour
    
    if turn_right:
        direction_index = (direction_index + 1) % 4
    else:
        direction_index = (direction_index - 1) % 4
        
    coords += directions[direction_index]
        
        
        
x_min = min(coord[0] for coord in hull.keys())
x_max = max(coord[0] for coord in hull.keys())
y_min = min(coord[1] for coord in hull.keys())
y_max = max(coord[1] for coord in hull.keys())

for y in range(y_max + 2, y_min - 1, -1):
    for x in range(x_min - 1, x_max + 2):
        if hull.get((x, y), False):
            print("#", end="")
        else:
            print(".", end="")
    print()
    
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            