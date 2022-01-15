class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        # if a first element is present
        if self.head:
            # iterate through list while there is another elements
            while current.next:
                # current object will be set to next elements until there are no more elements
                current = current.next
            # when there are no more elements, new element will set to current.next
            current.next = new_element
        # if there is no more elements in list, then automatically make first element the new element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # declares counters
        counter = 1
        current = self.head
        # end case, when the position given is a num < 1
        if position < 1:
            return None
        # while current element index and counter are below position, iterate through 
        while current and counter <= position:
            # if the counter is equal to the position, return the element
            if counter == position:
                return current
            # as list is being iterated through, set current element to next element
            current = current.next
            counter += 1
        # otherwise return none
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        current = self.head
        # if the position is 1, make the new element the first element of the list
        if position == 1:
            new_element.next = self.head
            # set self.head as the new element
            self.head = new_element
        # if position is greater than 1, start iterating through
        elif position > 1:
            # iterate through if current and counter are less than inputted position
            while current and counter < position:
                # conditional check to insert new element between position and previous
                if counter == position - 1:
                    # new element will link to the next element
                    new_element.next = current.next
                    # new element will be linked to the current element
                    current.next = new_element
                # iterate through list making current the next element each time
                current = current.next
                counter += 1

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        # iterate through list
        while current.value != value and current.next:
            previous = current
            current = current.next

        if current.value == value:
            # if previous is present
            if previous:
                # previous's next element will be assigned to current's next element
                previous.next = current.next
            else:
                # otherwise, first element's next element will the current's next element
                self.head = current.next