def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    max_sum = None
    arr_sum = 0;
    for item in arr:
        arr_sum += item
        
    for index in range(len(arr)-1):
        if max_sum is None:
            max_sum = arr[index] + arr[index+1]
        if arr[index] + arr[index+1] > max_sum:
            max_sum = arr[index] + arr[index+1]
    print(arr_sum)
    print(max_sum)
    return max(arr_sum,max_sum)

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr= [1, 2, 3, -4, 6]
solution= 8 # sum of array

test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, -5, -4, 1, 6]
solution = 7   # sum of last two elements

test_case = [arr, solution]
test_function(test_case)

arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]

test_case = [arr, solution]
test_function(test_case)