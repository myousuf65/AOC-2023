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


size = len(data) + 1
card_count = [1]*size

print(card_count)

# item = 9 5 6 7 | 9 7 5
for card_num , item in enumerate(data, start=1):


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

    
    counter = len(foundWinning)
    print(counter)    
    for i in range(len(foundWinning)):
        # print("card_count", card_num )
        card_count[card_num+counter] += card_count[card_num] 
        counter -= 1
        print(card_count)





    # for num in range(len(foundWinning)):
    #     card_count[card_num+num+1] = card_count.get(card_num)
    #     print(card_num+num)
    #     print(card_count.get(card_num+num+1))

    print("="*8)
print(sum(card_count[1:]))
#         if num == 0:
#             continue           
#         card_count[card_num+num] = card_count.get(card_num+num,0) + 1
#         print(card_count.get(card_num+num))


# print(card_count)
# print(sum(card_count.values()))
