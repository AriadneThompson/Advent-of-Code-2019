# -*- coding: utf-8 -*-

amplifier_program = [3,8,1001,8,10,8,105,1,0,0,21,30,55,76,97,114,195,276,357,438,99999,3,9,102,3,9,9,4,9,99,3,9,1002,9,3,9,1001,9,5,9,1002,9,2,9,1001,9,2,9,102,2,9,9,4,9,99,3,9,1002,9,5,9,1001,9,2,9,102,5,9,9,1001,9,4,9,4,9,99,3,9,1001,9,4,9,102,5,9,9,101,4,9,9,1002,9,4,9,4,9,99,3,9,101,2,9,9,102,4,9,9,1001,9,5,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99]
#amplifier_program = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]



def run(program, inputs):
    # Instruction pointer
    i = 0
    
    # Inputs pointer
    j = 0
    
    outputs = []
    
    # Don't want to edit the original program! 
    program = program.copy()
    
    while True:
        opcode = program[i] % 100
        
        if opcode in (1, 2, 4, 5, 6, 7, 8):
            # Has at least one parameter that might be in immediate mode:
            if (program[i] % 1000) // 100:
                param1 = program[i+1]
            else:
                param1 = program[program[i+1]]
                
            if opcode != 4:
                # Has a second parameter that might be in immediate mode:
                if (program[i] % 10000) // 1000:
                    param2 = program[i+2]
                else:
                    param2 = program[program[i+2]]
        
        if opcode == 1:
            program[program[i+3]] = param1 + param2
            i += 4
            
        elif opcode == 2:
            program[program[i+3]] = param1 * param2 
            i += 4
            
        elif opcode == 3:
            program[program[i+1]] = inputs[j]
            j += 1
            i += 2
            
        elif opcode == 4:
            outputs.append(param1)
            i += 2
            
        elif opcode == 5:
            if param1:
                i = param2
            else:
                i += 3
                
        elif opcode == 6:
            if not param1:
                i = param2
            else:
                i += 3
                
        elif opcode == 7:
            program[program[i+3]] = int(param1 < param2)
            i += 4
            
        elif opcode == 8:
            program[program[i+3]] = int(param1 == param2)
            i += 4
            
        elif opcode == 99:
            return outputs
        
        else:
            raise RuntimeError("Found unknown opcode " + str(program[i]) + " at position " + str(i) + ".")
        
        
        
phases = {0, 1, 2, 3, 4}

max_signal = 0

for i in phases:
    for j in phases - {i}:
        for k in phases - {i, j}:
            for l in phases - {i, j, k}:
                for m in phases - {i, j, k, l}:
                    
                    signal = 0
                    phase_sequence = (i, j, k, l, m)
                    
                    for n in range(5):
                        signal = run(amplifier_program, (phase_sequence[n], signal))[0]
                        
                    if signal > max_signal:
                        max_signal = signal
        
print(max_signal)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        