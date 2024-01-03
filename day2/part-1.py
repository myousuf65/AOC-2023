import re

with open('./input.txt') as file:
    data = file.read().strip().split('\n')


id = 0
for i, line in enumerate(data):
    gs = line.split(':')[1].strip('\n')

    ts = gs.split(';')
    for t in ts:
        map = {'red' : 0,'blue' : 0, 'green' :0 }
        cubes = t.split(',')
        for cube in cubes:
            score, color = cube.split()
        
            map[color] = int(score)

        if map['red'] > 12 or map['blue'] > 14 or map['green'] > 13:
            break

    else:
        id += (i+1)

print(id)








            
  # game_val = re.findall(r'\d+', data[0])
    # print("game number: ",game_val[0])

    # for item in data[1:]:
    #     print(item)
    #     g = line.split(';')
    #     for t in g:
    #         t

#     # g = [turn1 , turn2 , turn3 ]
#     numbers = re.findall(r'\d+', game[0])
#     print("game", numbers)
#     for turn in g:
        
#         # ball = [ 12blue, 15green, 19yellow]
#         # for ball in turn.split(','):
#         #         print(ball)
        

# # for line in data.split('\n'):
 #     print(line)
