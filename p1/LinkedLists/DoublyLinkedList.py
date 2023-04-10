class DoubleNode:
# DuploNó (DoublyNode): Possuí a mesma representação do
# nó, mas agora ele é bidirecional de ter próximo e anterior
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# Dupla lista ligada (DoublyLinkedList) segue os nós duplos
# mas agora tendo um item inicial e um item final
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
        else:
            self.tail.next = DoubleNode(value)
            self.tail.previous = self.tail
            self.tail = self.tail.next

