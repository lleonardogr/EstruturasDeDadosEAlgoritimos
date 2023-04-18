class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def to_list(self):
        lst = []
        current_node = self.head
        while current_node:
            lst.append(current_node.value)
            current_node = current_node.next
        return lst

def union(llist_1, llist_2):
    # Combine the elements of the two linked lists into a set
    elements = set(llist_1.to_list() + llist_2.to_list())
    # Create a new linked list from the set of elements
    result = LinkedList()
    for element in elements:
        result.append(element)
    return result

def intersection(llist_1, llist_2):
    # Convert the elements of the first linked list to a set
    # for fast membership checking
    set_1 = set(llist_1.to_list())
    # Create a new linked list from the elements that are in
    # both linked lists
    result = LinkedList()
    current_node = llist_2.head
    while current_node:
        if current_node.value in set_1:
            result.append(current_node.value)
        current_node = current_node.next
    return result


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test case 3
# Union of [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8] should be [1, 2, 3, 4, 5, 6, 7, 8]
llist_1 = LinkedList()
llist_1.append(1)
llist_1.append(2)
llist_1.append(3)
llist_1.append(4)
llist_1.append(5)

llist_2 = LinkedList()
llist_2.append(4)
llist_2.append(5)
llist_2.append(6)
llist_2.append(7)
llist_2.append(8)

union_llist = union(llist_1, llist_2)
assert union_llist.to_list() == [1, 2, 3, 4, 5, 6, 7, 8]

# Test case 4
# Intersection of [1, 2, 3] and [4, 5, 6] should be []
llist_1 = LinkedList()
llist_1.append(1)
llist_1.append(2)
llist_1.append(3)

llist_2 = LinkedList()
llist_2.append(4)
llist_2.append(5)
llist_2.append(6)

intersection_llist = intersection(llist_1, llist_2)
assert intersection_llist.to_list() == []

# Test case 5
# Union of [1, 1, 2, 2] and [2, 2, 3, 3] should be [1, 2, 3]
llist_1 = LinkedList()
llist_1.append(1)
llist_1.append(1)
llist_1.append(2)
llist_1.append(2)

llist_2 = LinkedList()
llist_2.append(2)
llist_2.append(2)
llist_2.append(3)
llist_2.append(3)

union_llist = union(llist_1, llist_2)
assert union_llist.to_list() == [1, 2, 3]

#Test 6
llist_1 = LinkedList()
llist_2 = LinkedList()
llist_2.append(1)
llist_2.append(7)
llist_2.append(8)
llist_2.append(9)
llist_2.append(11)
llist_2.append(21)
llist_2.append(1)
union_llist = union(llist_1, llist_2)
assert union_llist.to_list() == [1, 7, 8, 9, 11, 21]


#Test 7
llist_1 = LinkedList()
llist_1.append(1)
llist_1.append(1)
llist_1.append(1)
llist_1.append(2)
llist_1.append(2)
llist_1.append(2)
llist_1.append(2)
llist_1.append(3)
llist_1.append(3)
llist_1.append(3)
llist_2 = LinkedList()
llist_2.append(3)
llist_2.append(3)
llist_2.append(1)
llist_2.append(1)
llist_2.append(2)
llist_2.append(2)
union_llist = union(llist_1, llist_2)
assert union_llist.to_list() == [1, 2, 3]
