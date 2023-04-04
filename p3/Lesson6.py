def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return None, None

    max_value = ints[0]
    min_value = ints[0]

    for value in ints:
        if value > max_value:
            max_value = value
        elif value < min_value:
            min_value = value

    return min_value, max_value

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [9, 5, 3, 1, 0, 8, 2, 4, 7, 6]
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [5, 0, 1, 4, 6, 8, 9, 7, 2, 3]
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print("Pass" if ((1, 1) == get_min_max(l)) else "Fail")