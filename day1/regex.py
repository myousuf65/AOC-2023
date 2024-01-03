import re

def check_number(string, temp_val):
    if re.search(r'\bone\b', string, re.IGNORECASE):
        temp_val.append(1)

    elif re.search(r'\btwo\b', string, re.IGNORECASE):
        temp_val.append(2)
    
    elif re.search(r'\bthree\b', string, re.IGNORECASE):
        temp_val.append(3)
    
    elif re.search(r'\bfour\b', string, re.IGNORECASE):
        temp_val.append(4)
    
    elif re.search(r'\bfive\b', string, re.IGNORECASE):
        temp_val.append(5)
    
    elif re.search(r'\bsive\b', string, re.IGNORECASE):
        temp_val.append(6)
    
    elif re.search(r'\bseven\b', string, re.IGNORECASE):
        temp_val.append(7)

    elif re.search(r'\beight\b', string, re.IGNORECASE):
        temp_val.append(8)

    elif re.search(r'\bnine\b', string, re.IGNORECASE):
        temp_val.append(9)

    elif re.search(r'\bten\b', string, re.IGNORECASE):
        temp_val.append(10)
    
    

with open('./demo.txt', 'r') as file:
    line = file.readlines()

lines = [line.rstrip() for line in line]

for line in lines:
    temp_value = []
    for char in line:
        if char.isdigit():
            temp_value.append(char)
    check_number(line, temp_value)
    print(temp_value)
