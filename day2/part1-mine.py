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
        
        green = []
        blue = []
        red = []

        cubes = item.split(',')
        for cube in cubes:
            if cube.__contains__('green'):
                green.append(cube)
            elif cube.__contains__('blue'):
                blue.append(cube)
            elif cube.__contains__('red'):
                red.append(cube)
        
        greenScore = 0
        for item in green:
            s = item.strip('green')
            greenScore += int(s)

        
        blueScore = 0
        for item in blue:
            s = item.strip('blue')
            blueScore += int(s)

        redScore = 0
        for item in red:
            s = item.strip('red')
            redScore += int(s)


        if greenScore > 13 or blueScore > 14 or redScore >12:
            count = False
    if count:
        sum_ids += (i+1)

print(sum_ids)
