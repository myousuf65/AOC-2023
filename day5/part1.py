
content:str = ''


with open('./demo.txt') as file:
    content = file.read()


# first value is assign to seeds and the rest to list
# *list is for unpacking of the items of list into 2 dif variables

seeds, *blocks = content.split('\n\n')


seeds = seeds.split(':')[1].split()
print(seeds)


for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    print(ranges)



# ns, seeds = list[0].split(':')
# seedArray = seeds.split()

# # print(seedArray)


# nss, seed2soil = list[1].split(':')
# seed2soilArray = seed2soil.splitlines()
# seed2soilArray = [item for item in seed2soilArray if item !='']
# print(seed2soilArray)





# seed2soilArray = seed2soil.strip('\n').split()

# print(seed2soilArray)





# lines = [item for item in lines if item !='']
# print(lines)



