'''

Alice has some cards with numbers written on them. 
She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. 
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. 
Write a function to help Bob locate the card.

'cards' is a list of numbers in decreasing order
'query' is the position in the array that is to be determined
'position' is the position of 'query' in the list 'cards'

'''

def locateCard(cards,query):
    low = 0
    high = len(cards) - 1

    while low <= high:

        middle = (low+high) // 2
        middleNum = cards[middle]

        if middleNum == query:
            return middle

        elif middle < query:
            high = middle - 1

        elif middle > query:
            low = middle + 1

    return -1

arr = [19,5,3,1]
num = 5
print(locateCard(arr,num))
