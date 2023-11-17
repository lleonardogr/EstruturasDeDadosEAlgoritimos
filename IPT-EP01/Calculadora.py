# Nó (Node): Primeiramente, precisamos entender o conceito de nó. 
# Cada nó em uma lista ligada é composto por dois elementos: 
# um valor armazenado e uma referência ao próximo nó na lista.
class Node:
    def __init__(self, value=0):
        self.value = value  # Valor do nó
        self.next = None  # Referência ao próximo nó na lista
    
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
    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    # Cria uma lista linkada a partir de um array
    # para isso ele simplesmente faz um for dentro da lista e faz um append dentro da lista
    @staticmethod
    def from_list(lst):
        """Cria uma LinkedList a partir de uma lista."""
        linked_list = LinkedList()
        for value in lst:
            linked_list.append(value)
        return linked_list

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
    def to_list(linkedlist):
        lst = []
        current = linkedlist.head
        while current:
            lst.append(current.value)
            current = current.next
        return lst
    
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
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    # isCircular: 
    # Determine whether the Linked List is circular or not
    def iscircular(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
    
    # str: imprime a lista em string
    # Retorna a representação em string da lista.
    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return ''.join(values)

    @staticmethod
    def add_lists(l1, l2):
        dummy = Node()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            sum = carry
            if l1:
                sum += l1.value
                l1 = l1.next
            if l2:
                sum += l2.value
                l2 = l2.next
            carry = sum // 10
            current.next = Node(sum % 10)
            current = current.next

        return dummy.next
    
    @staticmethod
    def multiply_lists(l1, l2):
        result_list = LinkedList()
        result_tail = Node(0)
        result_list.head = result_tail

        while l2:
            temp_sum = Node(0)
            for _ in range(l2.value):
                temp_sum = LinkedList.add_lists(temp_sum, l1)

            result_tail.next = LinkedList.add_lists(result_tail.next, temp_sum)
            result_tail = result_tail.next
            l2 = l2.next

        result_list.head = result_list.head.next  # Skip the initial dummy node
        result_list.reverse()
        return result_list

# Lê um arquivo e cria uma lista ligada com os dígitos do número no arquivo
def read_file_and_create_linkedlist(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read().strip()  # O arquivo precisa apenas conter um número
        linked_list = LinkedList()
        for digit in data:
            linked_list.append(int(digit))
        print("número lido, criando lista \r\n")
        return linked_list
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e} \r\n")
        return None

def multiply_linked_lists_iterable(ll1, ll2):
    multiply = int(str(ll2))

    result = LinkedList()
    result.append(0)
    for _ in range(multiply+1):
        result.head = LinkedList.add_lists(result.head, ll1.head)
        print(f"step: {_} result: {result}")

    return result

def save_result_to_file(filename, linked_list):
    """Salva o valor da lista ligada em um arquivo."""
    try:
        with open(filename, 'w') as file:
            number_str = str(linked_list)  # Convertendo a lista ligada em uma string
            file.write(number_str)
        print("Salvando arquivo...")
        print("Valor salvo com sucesso!\r\n")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}\r\n")

def execute_tests():
    v1 = read_file_and_create_linkedlist('input1.txt')
    v2 = read_file_and_create_linkedlist('input2.txt')
    v1.reverse()
    v2.reverse()
    v3_expected = '9907154872715583'
    v3 = LinkedList()
    v3.head = LinkedList.add_lists(v1.head, v2.head)
    v3.reverse()
    assert v3.__str__() == v3_expected, f"Erro: esperava {v3_expected}, obteve {v3}"
    print("Soma testada!!!!\r\n")

    v3_expected = '311241462701567071001451192'
    v3 = LinkedList.multiply_lists(v1.head, v2.head)
    assert v3.__str__() == v3_expected, f"Erro: esperava {v3_expected}, obteve {v3}"
    print('Multiplicação testado\r\n')

    v1 = read_file_and_create_linkedlist('input1.txt')
    v2 = read_file_and_create_linkedlist('input2.txt')
    v1.reverse()
    v2.reverse()
    v3 = LinkedList()
    v3.head = LinkedList.add_lists(v1.head, v2.head)
    v3.reverse()
    filename = 'output.txt'
    save_result_to_file(filename, v3)
    with open(filename, 'r') as file:
        result = file.read().strip()
    v3_expected = '9907154872715583'
    assert result == v3_expected, f"Erro: esperava {v3_expected}, obteve {result}\r\n"

# Executando os testes
if __name__ == "__main__":
    execute_tests()
    print("Todos os testes passaram.\r\n")
    
    # Exemplo de uso:
    while True:
        print("1. Ler o primeiro valor do arquivo (V1)")
        print("2. Ler o segundo valor do arquivo (V2)")
        print("3. Somar V1 com V2 e gerar um terceiro valor (V3)")
        print("4. Multiplicar V1 por V2 e gerar um terceiro valor (V3)")
        print("5. Salvar o resultado (V3) em um arquivo")
        print("6. Sair da calculadora")
        print("========================================================= \r\n")

        choice = input("Escolha uma opção: ")
        if choice == '1':
            filename = input("Entre com o nome do arquivo: ")
            v1 = read_file_and_create_linkedlist(filename)
            v1.reverse()
        elif choice == '2':
            filename = input("Entre com o nome do arquivo: ")
            v2 = read_file_and_create_linkedlist(filename)
            v2.reverse()
        elif choice == '3':
            v3 = LinkedList()
            v3.head = LinkedList.add_lists(v1.head, v2.head)
            v3.reverse()
            print(f'{v1} + {v2} = {v3}')
        elif choice == '4':
            v3 = LinkedList.multiply_lists(v1.head, v2.head)
            print(f'{v1} × {v2} = {v3.__str__()}')
        elif choice == '5':
            filename = input("Entre com o nome do arquivo: ")
            save_result_to_file(filename, v3)
        elif choice == '6':
            print("Saindo da calculadora...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")