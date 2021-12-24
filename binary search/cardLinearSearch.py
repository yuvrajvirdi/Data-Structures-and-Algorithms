'''

Alice has some cards with numbers written on them. 
She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. 
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. 
Write a function to help Bob locate the card.

'cards' is a list of numbers in decreasing order
'query' is the position in the array that is to be determined
'position' is the position of 'query' in the list 'cards'

'''

def findCard(cards,query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

