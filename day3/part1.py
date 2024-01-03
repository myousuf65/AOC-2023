with open('./input.txt') as file:
    # each line is an item in the list
    lines = file.readlines()


# initialize the grid
_2D_array = []


#creating a grid to store data like a matrix
for row in lines:
    #list of lists
    column_list = []

    r = row.strip('\n')
    for char in r:
        column_list.append(char)
    _2D_array.append(column_list)


first_digit_coordinates = set()


for row_i, row in enumerate(_2D_array):
    for column_i, char in enumerate(row):

        # dont loop unless its a symbol
        if char.isdigit() or char == '.':
            continue

        #check 8 directions of a symbol for digit
        for rr in [row_i+1, row_i,row_i-1]:
            for cc in [column_i+1, column_i, column_i-1]:

                # preventing out of bound checking
                # if not digit >> break
                if rr < 0 or cc < 0 or cc >= len(_2D_array[rr]) or rr >= len(_2D_array) or not _2D_array[rr][cc].isdigit():
                    continue


                # find coordinate of first num
                while cc > 0 and _2D_array[rr][cc - 1].isdigit():
                    cc -= 1

                # add the coordinate to the set
                first_digit_coordinates.add((rr,cc))


master_sum = 0


for r,c  in first_digit_coordinates: 

    partnumber = ''
    
    # move right to get the entire whole number
    while c < len(_2D_array[r]) and _2D_array[r][c].isdigit():
        # append the digit
        partnumber += _2D_array[r][c]
        # append c of that specific item
        c += 1
    
    master_sum += int(partnumber)

print(master_sum)





