# -*- coding: utf-8 -*-

file = open("Day 6 Input.txt", "r")
orbit_maps = dict(line[:-1].split(")")[::-1] for line in file)
file.close()

def orbits_to_com(satellite):
    orbits = set()
    
    while satellite != "COM":
        orbits.add(orbit_maps[satellite])
        satellite = orbit_maps[satellite]
        
    return orbits

print(len(orbits_to_com("YOU") ^ orbits_to_com("SAN"))) 