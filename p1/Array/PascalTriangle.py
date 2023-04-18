def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    if n < 0:
        return []
    
    # Inicialize a primeira linha do triângulo
    result = [1]
    
    # Itere sobre as linhas do triângulo até chegar à linha desejada
    for _ in range(n):
        # Calcule a próxima linha usando a linha atual
        next_line = [1]  # O primeiro elemento da linha é sempre 1
        for i in range(1, len(result)):
            next_line.append(result[i - 1] + result[i])
        next_line.append(1)  # O último elemento da linha é sempre 1
        
        # Atualize a linha atual para ser a próxima linha
        result = next_line
        
    return result

def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = nth_row_pascal(n)
    if solution == output:
        print("Pass")
    else:
        print("Fail")

n = 0
solution = [1]

test_case = [n, solution]
test_function(test_case)

n = 1
solution = [1, 1]

test_case = [n, solution]
test_function(test_case)

n = 2
solution = [1, 2, 1]

test_case = [n, solution]
test_function(test_case)

n = 3
solution = [1, 3, 3, 1]

test_case = [n, solution]
test_function(test_case)

n = 4
solution = [1, 4, 6, 4, 1]

test_case = [n, solution]
test_function(test_case)
