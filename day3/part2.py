with open('./input.txt') as file:
    # each line is an item in the list
    lines = file.readlines()


# initialize the grid
_2D_array = []

for row in lines:
    column_list = []
    r = row.strip('\n')
    for char in r:
        column_list.append(char)
    _2D_array.append(column_list)



master_coordinates = []

for row_i, row in enumerate(_2D_array):
    for column_i, char in enumerate(row):
        
        # we need symbols only
        if char.isdigit() or  char == '.':
            continue

        # in symbols, we need * only
        if char == '*':
            first_digit_coordinates = set()
            
            # check 8 directions of *
            for rr in [row_i+1, row_i,row_i-1]:
                for cc in [column_i+1, column_i, column_i-1]:

                    # prevent out of bound operation
                    # break if not digit in one of 8 directions
                    if cc < 0 or rr < 0 or cc >= len(_2D_array[rr]) or rr >= len(_2D_array) or not _2D_array[rr][cc].isdigit():
                        continue

                    # if digit >> find first digit coordinates
                    while _2D_array[rr][cc - 1].isdigit():
                        cc -= 1
                    
                    first_digit_coordinates.add((rr, cc))
            
            # check if we have more than one coordinates
            if len(first_digit_coordinates) >= 2:
                #append coordinates to list as item related to a single *
                master_coordinates.append(first_digit_coordinates)
        
        # if not * >> break
        else :
            continue



product_sum = []

# loop over list >> each item related to one *
for item in master_coordinates:


    product = 0
    two_nums = []
    
    for r, c in item:
        s = ''
    
        cplus = c
        # move right to find the whole number
        while cplus< len(_2D_array[r]) and _2D_array[r][cplus].isdigit():
            s += _2D_array[r][cplus]
            cplus += 1
        
        two_nums.append(int(s))
    
    # multiply the numbers related to one *
    product = two_nums[0]*two_nums[1]
    # append them to the list for summation
    product_sum.append(product)


# sum of all the numbers in the list is printed
print(sum(product_sum))
