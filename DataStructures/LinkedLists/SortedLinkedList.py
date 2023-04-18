from LinkedList import Node
from LinkedList import LinkedList

class SortedLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        """
        Append a value to the Linked List in ascending sorted order

        Args:
           value(int): Value to add to Linked List
        """
        
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            if current.value > value:
                self.head = Node(value)
                self.head.next = current
                return
            while current.next is not None and current.next.value < value:
                current = current.next
            if current.next:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
            else:
                current.next = Node(value)

# Test cases
linked_list = SortedLinkedList()
linked_list.append(3)
print ("Pass" if (linked_list.head.value == 3) else "Fail")

linked_list.append(2)
print ("Pass" if (linked_list.head.value == 2) else "Fail")

linked_list.append(4)
node = linked_list.head.next.next
print ("Pass" if (node.value == 4) else "Fail")

def sort(array):
    """
    Given an array of integers, use SortedLinkedList to sort them and return a sorted array.

    Args:
       array(array): Array of integers to be sorted
    Returns:
       array: Return sorted array
    """
    sorted_array = []
    
    linked_list = SortedLinkedList()
    for value in array:
        linked_list.append(value)
    
    # Convert sorted linked list to a normal list/array
    node = linked_list.head
    while node:
        sorted_array.append(node.value)
        node = node.next
    return sorted_array

print ("Pass" if (sort([4, 8, 2, 1, -3, 1, 5]) == [-3, 1, 1, 2, 4, 5, 8]) else "Fail")
