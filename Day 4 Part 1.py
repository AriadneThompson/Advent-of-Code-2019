# -*- coding: utf-8 -*-

def is_valid(password):
    double_digit = False
    
    for i in range(5):
        if password[i] == password[i+1]:
            double_digit = True
        if password[i] > password[i+1]:
            return False
        
    return double_digit
    
    

total_valid = 0

for i in range(248345, 746315):
    if is_valid(str(i)):
        total_valid += 1
        
print(total_valid)