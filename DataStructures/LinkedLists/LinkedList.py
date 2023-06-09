# Nó (Node): Primeiramente, precisamos entender o conceito de nó. 
# Cada nó em uma lista ligada é composto por dois elementos: 
# um valor armazenado e uma referência ao próximo nó na lista.
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)

# Lista ligada (Linked List): 
# A lista ligada é uma estrutura de dados composta por uma sequência de 
# nós. Cada nó aponta para o próximo nó, formando uma cadeia.
class LinkedList:
    def __init__(self):
        self.head = None

# Adicionar elementos: 
# Para adicionar um elemento à lista ligada, 
# primeiro, criamos um novo nó com o valor desejado e depois, 
# atualizamos a referência do último nó para apontar para o novo nó.
    def append(self,value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)

    # Percorrer a lista: 
    # Para percorrer a lista ligada, começamos com o nó cabeça (head) e 
    # seguimos as referências até o final da lista.
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value, end=' -> ')
            current = current.next

    # Remover elementos: 
    # Para remover um elemento da lista ligada, 
    # primeiro, encontramos o nó anterior ao nó que desejamos remover e, 
    # em seguida, atualizamos sua referência para apontar para o nó após o 
    # nó que será removido.
    def remove(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.value == value:
                current.head = self.head.next
                return
            current = current.next

    # Transformar a linked list em um array:
    def toList(self):
        list_ = []
        if self.head is None:
            return list_
        list_.append(self.head.value)
        current = self.head
        while current.next is not None:
            list_.append(current.value)
            current = current.next
        return list_
    
    # Prepend: Adiciona um item no inicio da lista linkada
    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            second = self.head
            self.head = Node(value)
            self.head.next = second
    
    # Search: Procura um item na lista
    def search(self, value):
        if self.head is None:
            return None
        
        current = self.head
        if current.value == value:
            return current
        while current.next:
            current = current.next
            if current.value == value:
                return current
        return None
    
    # Pop: Pega o primeiro item da lista e remove da lista
    def pop(self):
        if self.head is None:
            return None
        
        node = self.head
        self.head = self.head.next
        return node.value
    
    # Insert value at pos position in the list. If pos is larger than the
    # length of the list, append to the end of the list.
    def insert(self, value, pos):
        if self.head is None:
            self.head = Node(value)

        if pos == 0:
            self.prepend(value)
            return
        else:
            item_pos = 1
            current = self.head
            while current.next:
                if item_pos == pos:
                    new_node = Node(value)
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next
                item_pos = item_pos + 1
            current.next = Node(value)

    # Return the size or length of the linked list.
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    # Iteração na lista linkada para fazer for ou foreach
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    # Imprimir uma lista de string da lista linkada
    def __repr__(self):
        return str([v for v in self])
    
    def reverse(self):
        new_list = LinkedList()
        prev_node = None
        for value in self:
            new_node = Node(value)
            new_node.next = prev_node
            prev_node = new_node

        new_list.head = prev_node
        return new_list
    
    # isCircular: Determine whether the Linked List is circular or not
    def iscircular(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False


# Exemplo

# Criando uma lista ligada vazia
my_linked_list = LinkedList()

# Adicionando elementos à lista ligada
my_linked_list.append(10)
my_linked_list.append(20)
my_linked_list.append(30)

# Exibindo os elementos da lista ligada
my_linked_list.traverse()  # Saída: 10 -> 20 -> 30 -> None

# Removendo um elemento da lista ligada
my_linked_list.remove(20)

# Exibindo os elementos da lista ligada após a remoção
my_linked_list.traverse()  # Saída: 10 -> 30 -> None

print(my_linked_list.head.value)
print(my_linked_list.head.next.value)
print(my_linked_list.head.next.next.value)

# Exibindo os elementos como lista
print(my_linked_list.toList())

# Criando uma lista ligada vazia
my_linked_list = LinkedList()

# Testando o método prepend
my_linked_list.prepend(30)
my_linked_list.prepend(20)
my_linked_list.prepend(10)
assert my_linked_list.head.value == 10

# Testando o método search
assert my_linked_list.search(20).value == 20
assert my_linked_list.search(40) is None

# Testando o método pop
assert my_linked_list.pop() == 10
assert my_linked_list.head.value == 20

# Testando o método insert
my_linked_list.insert(40, 2)
assert my_linked_list.search(40).value == 40

# Testando o método size
assert my_linked_list.size() == 3

print(my_linked_list.traverse())
print(my_linked_list.reverse())

# Crie uma lista ligada não circular
non_circular_list = LinkedList()
non_circular_list.prepend(30)
non_circular_list.prepend(20)
non_circular_list.prepend(10)

# Crie uma lista ligada circular
circular_list = LinkedList()
circular_list.prepend(30)
circular_list.prepend(20)
circular_list.prepend(10)
circular_list.head.next.next.next = circular_list.head

# Teste a função is_circular_linked_list
assert not non_circular_list.iscircular()
assert circular_list.iscircular()


# This function that it merges the two linked lists in a single, sorted linked list.
def merge(list1: LinkedList, list2: LinkedList):
    array_complete = list(set(list1.toList() + list2.toList()))
    linked_list = LinkedList()
    for item in array_complete:
        linked_list.append(item)
    return linked_list
    

list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

merged_list = merge(list1, list2)