with open('./input.txt') as file:
    r_lines = file.readlines()
    
sum_ids = 0

for i, line in enumerate(r_lines):
    green = []
    blue = []
    red = []
    count = True

    parts = line.strip('\n').split(':', 1)
    
    turns = parts[1].split(';')
    
    for index, item in enumerate(turns):
        
        cubes = item.split(',')
        for cube in cubes:
            if cube.__contains__('green'):
                green.append(cube)
            elif cube.__contains__('blue'):
                blue.append(cube)
            elif cube.__contains__('red'):
                red.append(cube)
        
    
    for i in range(len(green)):
        n , gc = green[i].split()
        green[i] = int(n)

  
    for i in range(len(blue)):
        n , bc = blue[i].split()
        blue[i] = int(n)

    
    for i in range(len(red)):
        n , bc = red[i].split()
        red[i] = int(n)

    sum_ids += sorted(green)[-1] * sorted(blue)[-1] * sorted(red)[-1]

print(sum_ids)
    

