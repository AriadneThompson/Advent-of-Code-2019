# -*- coding: utf-8 -*-

amplifier_program = [3,8,1001,8,10,8,105,1,0,0,21,30,55,76,97,114,195,276,357,438,99999,3,9,102,3,9,9,4,9,99,3,9,1002,9,3,9,1001,9,5,9,1002,9,2,9,1001,9,2,9,102,2,9,9,4,9,99,3,9,1002,9,5,9,1001,9,2,9,102,5,9,9,1001,9,4,9,4,9,99,3,9,1001,9,4,9,102,5,9,9,101,4,9,9,1002,9,4,9,4,9,99,3,9,101,2,9,9,102,4,9,9,1001,9,5,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99]
#amplifier_program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]



def run(inputs, program_state):
    # Instruction pointer
    i = program_state["i"]
    
    program = program_state["program"]
    
    # Inputs pointer
    j = 0
    
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
            return param1, {"program":program, "i":i + 2}
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
            return None
        
        else:
            raise RuntimeError("Found unknown opcode " + str(program[i]) + " at position " + str(i) + ".")
        
        
        
phases = {5, 6, 7, 8, 9}

max_signal = 0

for i in phases:
    for j in phases - {i}:
        for k in phases - {i, j}:
            for l in phases - {i, j, k}:
                for m in phases - {i, j, k, l}:
                    
                    phase_sequence = (i, j, k, l, m)
                    program_states = [amplifier_program.copy(), amplifier_program.copy(), amplifier_program.copy(), amplifier_program.copy(), amplifier_program.copy()]
                    
                    signal = 0
                    
                    for n in range(5):
                        signal, program_states[n] = run(inputs=(phase_sequence[n], signal), program_state={"program":program_states[n], "i":0} )
                        
                    # Whether or not a program has exited with opcode 99. 
                    halted = False
                    
                    while not halted:
                        for n in range(5):
                            output = run(inputs=[signal], program_state=program_states[n])
                            if output is not None:
                                signal, program_states[n] = output
                            else:
                                halted = True
                        
                    if signal > max_signal:
                        max_signal = signal
        
print(max_signal)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        