from LinkedList import Node, LinkedList

#Criamos duas listas encadeadas separadas para armazenar elementos ímpares e elementos pares, respectivamente. Inicializamos as cabeças e as caudas de ambas as listas como None.
#Iteramos pela lista encadeada original, usando a variável current para manter o controle do nó atual que estamos processando.
#Verificamos se o valor do nó atual é ímpar ou par usando current.data % 2.
#Se o valor do nó atual for ímpar, verificamos se a lista de elementos ímpares está vazia. Se estiver vazia, atribuímos o nó atual como a cabeça e a cauda da lista ímpar. Caso contrário, adicionamos o nó atual ao final da lista ímpar, atualizando a cauda.
#Se o valor do nó atual for par, verificamos se a lista de elementos pares está vazia. Se estiver vazia, atribuímos o nó atual como a cabeça e a cauda da lista par. Caso contrário, adicionamos o nó atual ao final da lista par, atualizando a cauda.
#Avançamos para o próximo nó na lista original e repetimos os passos 3 a 5 até chegarmos ao final da lista.
#Após processar todos os nós, conectamos a lista par à lista ímpar, fazendo com que a cauda da lista ímpar aponte para a cabeça da lista par. Se a lista ímpar estiver vazia, atribuímos a cabeça da lista par como a nova cabeça da lista encadeada.
#Se a lista par não estiver vazia, certificamo-nos de que a cauda da lista par aponte para None, já que é o final da lista encadeada.
#Retornamos a cabeça da lista encadeada rearranjada (que é a cabeça da lista ímpar, ou a cabeça da lista par se não houver elementos ímpares).

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def even_after_odd(head):
    if head is None:
        return None

    odd_head = None
    odd_tail = None
    even_head = None
    even_tail = None
    current = head

    while current is not None:
        if current.data % 2 == 1:
            if odd_head is None:
                odd_head = current
                odd_tail = current
            else:
                odd_tail.next = current
                odd_tail = current
        else:
            if even_head is None:
                even_head = current
                even_tail = current
            else:
                even_tail.next = current
                even_tail = current

        current = current.next

    if odd_tail is not None:
        odd_tail.next = even_head
    else:
        odd_head = even_head

    if even_tail is not None:
        even_tail.next = None

    return odd_head

# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

def test_function(test_case):
    head = test_case[0]
    solution = test_case[1]
    
    node_tracker = dict({})
    node_tracker['nodes'] = list()
    temp = head
    while temp:
        node_tracker['nodes'].append(temp)
        temp = temp.next

    head = even_after_odd(head)    
    temp = head
    index = 0
    try:
        while temp:
            if temp.data != solution[index] or temp not in node_tracker['nodes']:
                print("Fail")
                return
            temp = temp.next
            index += 1
        print("Pass")            
    except Exception as e:
        print("Fail")

arr = [1, 2, 3, 4, 5, 6]
solution = [1, 3, 5, 2, 4, 6]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [1, 3, 5, 7]
solution = [1, 3, 5, 7]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [2, 4, 6, 8]
solution = [2, 4, 6, 8]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)