import sys
sys.path.insert(0, 'C:/Users/lleon/OneDrive/Documentos/Udacity/DataStructuresAndAlgorithims/Projeto 1/p1/LinkedLists')

from LinkedList import Node, LinkedList

class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def is_empty(self):
        return self.head is None
    
    def size(self):
        return self.num_elements

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None

        value = self.head.value
        self.head = self.head.next
        self.num_elements += -1
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.head.value


def testStack():
    # Exemplo de uso da LinkedListStack:
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Topo da pilha:", stack.peek())  # Saída: Topo da pilha: 3

    print("Pop:", stack.pop())  # Saída: Pop: 3

    print("Topo da pilha:", stack.peek())  # Saída: Topo da pilha: 2

    # Setup
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)

    # Test size
    print ("Pass" if (stack.size() == 5) else "Fail")

    # Test pop
    print ("Pass" if (stack.pop() == 50) else "Fail")

    # Test push
    stack.push(60)
    print ("Pass" if (stack.pop() == 60) else "Fail")
    print ("Pass" if (stack.pop() == 40) else "Fail")
    print ("Pass" if (stack.pop() == 30) else "Fail")
    stack.push(50)
    print ("Pass" if (stack.size() == 3) else "Fail")

