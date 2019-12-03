# -*- coding: utf-8 -*-

file = open("Day 1 Input.txt", "r")
modules = [line for line in file]
file.close()

#def fuel(mass):
#    return (int(mass) // 3) - 2

print(sum(map(lambda x: (int(x) // 3) - 2, modules)))
    
    