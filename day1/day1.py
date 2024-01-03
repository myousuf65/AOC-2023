
#-------------Part 1-------------------
with open('./input.txt', 'r')  as file:
    total = 0
    for line in file:
        temp_val = []
        for char in line:
            if char.isdigit():
                temp_val.append(char)
        to_be_printed = temp_val[0]+temp_val[-1]
        total += int(to_be_printed)

    print(total)


#-------------Part 1-------------------
with open('./input.txt', 'r') as file:
    line = file.readlines()

lines = [line.rstrip() for line in line]

ans = 0
for line in lines:
    temp_val = []
    for index, char in enumerate(line):
        if char.isdigit():
            temp_val.append(char)
        for d, value in enumerate(('one', 'two','three', 'four','five','six','seven','eight','nine','ten')):
            if line[index:].startswith(value):
                temp_val.append(d+1)
    temp = str(temp_val[0]) + '' + str(temp_val[-1])
    ans += int(temp)

print(ans)





