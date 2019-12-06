# -*- coding: utf-8 -*-

file = open("Day 6 Input.txt", "r")
orbit_maps = dict(line[:-1].split(")")[::-1] for line in file)
file.close()

total_orbits = 0

for satellite in orbit_maps.keys():
    while satellite != "COM":
        total_orbits += 1
        satellite = orbit_maps[satellite]
        
print(total_orbits)