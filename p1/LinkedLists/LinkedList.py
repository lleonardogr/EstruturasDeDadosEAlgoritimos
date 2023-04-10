# Nó (Node): Primeiramente, precisamos entender o conceito de nó. 
# Cada nó em uma lista ligada é composto por dois elementos: 
# um valor armazenado e uma referência ao próximo nó na lista.
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

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
        print("None")

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