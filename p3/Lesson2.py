def find_pivot(input_list, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if mid < right and input_list[mid] > input_list[mid + 1]:
        return mid

    if mid > left and input_list[mid] < input_list[mid - 1]:
        return mid - 1

    if input_list[left] >= input_list[mid]:
        return find_pivot(input_list, left, mid - 1)
    else:
        return find_pivot(input_list, mid + 1, right)


def binary_search(input_list, left, right, number):
    if left > right:
        return -1

    mid = (left + right) // 2
    if input_list[mid] == number:
        return mid

    if input_list[mid] < number:
        return binary_search(input_list, mid + 1, right, number)
    else:
        return binary_search(input_list, left, mid - 1, number)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    n = len(input_list)
    pivot = find_pivot(input_list, 0, n - 1)

    if pivot == -1:
        return binary_search(input_list, 0, n - 1, number)

    if input_list[pivot] == number:
        return pivot

    if input_list[0] <= number:
        return binary_search(input_list, 0, pivot - 1, number)
    else:
        return binary_search(input_list, pivot + 1, n - 1, number)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1
    
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])