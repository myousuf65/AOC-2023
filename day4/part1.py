with open("./input.txt") as file:
    # each line is an item in the list
    lines = file.readlines()



data = []
for item in lines:

    clean_item = item.strip('\n')
    g , i = clean_item.split(':')
    # g = Card 1 
    # i = 9 5 6 7 | 9 7 5
    data.append(i)



master_winningPoints = 0

# item = 9 5 6 7 | 9 7 5
for item in data:

    foundWinning = []
    
    # winning in one array
    # numbers in one array
    winning , numbers = item.split('|')
    
    # split  by space
    winningArray = winning.split()
    numbersArray = numbers.split()

    

    for num in numbersArray:
        # if found in winning array
        if num in winningArray:
            foundWinning.append(num)



    winingPoints = 0
    counter = 1

    '''
        scoring: 
            1st item = 1 point
            2nd item = 1 point
            3rd item = 1 X 2 points = 2
            4th item = 2 X 2 points = 4
            5th item = 4 X 2 points = 8

        total points  = sum of all the individual points
    ''' 

    for i, item in enumerate(foundWinning):

        
        # one point only
        if i == 0 or i == 1:
            winingPoints += counter

        # double points
        else:
            counter *= 2 
            winingPoints += counter
    
    # sumation of points
    master_winningPoints += winingPoints


print(master_winningPoints)



