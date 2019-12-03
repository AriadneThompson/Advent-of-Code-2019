# -*- coding: utf-8 -*-

file = open("Day 1 Input.txt", "r")
modules = [line for line in file]
file.close()

def fuel_required(mass):
    return (mass // 3) - 2

total = 0

for module in modules:
    mass = int(module)
    
    while True:
        fuel = fuel_required(mass)
        
        if fuel <= 0:
            break
        
        total += fuel
        mass = fuel
    
print(total)