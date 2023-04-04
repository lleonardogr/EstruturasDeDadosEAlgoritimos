def merge_sort(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2
    left = merge_sort(input_list[:mid])
    right = merge_sort(input_list[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] > right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result


def rearrange_digits(input_list):
    if len(input_list) < 2:
        raise ValueError("A lista de entrada deve conter pelo menos 2 elementos")

    sorted_list = merge_sort(input_list)

    num1, num2 = 0, 0
    for i, digit in enumerate(sorted_list):
        if i % 2 == 0:
            num1 = num1 * 10 + digit
        else:
            num2 = num2 * 10 + digit

    return [num1, num2]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])

test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

test_case2 = [[9, 8, 7, 6, 5, 4, 3, 2, 1],[97531, 8642]]
test_function(test_case2)

test_case3 = [[5, 3, 0, 7, 4, 1, 6, 2, 8],[7531, 8642]]
test_function(test_case3)

test_case4 = [[9, 9, 9, 1, 1, 1],[991, 991]]
test_function(test_case4)

test_case5 = [[1, 1, 1, 1, 1, 1],[111, 111]]
test_function(test_case5)