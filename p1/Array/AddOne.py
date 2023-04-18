def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    sum = True
    new_arr = []
    for item in reversed(arr):
        if sum:
            if item < 9:
                item += 1
                sum = False
            else:
                item = 0
        new_arr.append(item)
    if new_arr[-1] == 0:
        new_arr.append(1)
    return reversed(new_arr)

# A helper function for Test Cases
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass") 

# Test Case 1
arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

# Test Case 2
arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

# Test Case 3
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)