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

    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'
            
    return genericBinarySearch(0,len(cards)-1, condition)
    
def genericBinarySearch(low,high,condition):
    while low <= high:
        mid = (low + high) // 2
        if condition(mid) == 'found':
            return mid
        elif condition(mid) == 'left':
            high = mid - 1
        elif condition(mid) == 'right':
            low = mid + 1


