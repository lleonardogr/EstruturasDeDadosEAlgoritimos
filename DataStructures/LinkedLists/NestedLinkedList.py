from LinkedList import Node
from LinkedList import LinkedList

class NestedLinkedList:
    def __init__(self):
        self.head = None

    def append(self, linked_list):
        if self.head is None:
            self.head = Node(linked_list)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(linked_list)

    def merge_pair(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.value < list2.value:
            result = list1
            result.next = self.merge_pair(list1.next, list2)
        else:
            result = list2
            result.next = self.merge_pair(list1, list2.next)
        
        return result

    def merge_all(self):
        if self.head is None or self.head.next is None:
            return self.head
        
        current = self.head
        new_head = Node(self.merge_pair(current.value.head, current.next.value.head))
        current = current.next.next

        while current is not None:
            new_head.next = Node(self.merge_pair(current.value.head, current.next.value.head))
            current = current.next.next
            new_head = new_head.next

        return NestedLinkedList.from_head(new_head)

    @classmethod
    def from_head(cls, head):
        nested_linked_list = cls()
        nested_linked_list.head = head
        return nested_linked_list

list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

nested_linked_list = NestedLinkedList()
nested_linked_list.append(list1)
nested_linked_list.append(list2)

merged_list = nested_linked_list.merge_all()