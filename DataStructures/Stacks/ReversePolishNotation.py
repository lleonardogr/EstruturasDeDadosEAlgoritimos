from StackLinkedList import Stack

def evaluate_post_fix(input_list):
    """
    Evaluate the postfix expression to find the answer

    Args:
       input_list(list): List containing the postfix expression
    Returns:
       int: Postfix expression solution
    """
    equation = Stack()
    for input_ in input_list:
        if input_ not in ["+","-","*","/"]:
            equation.push(input_)
        else:
            if input_ == '+':
                equation.push(int(equation.pop())+int(equation.pop()))
            elif input_ == '-':
                equation.push(int(equation.pop())-int(equation.pop()))
            elif input_ == '*':
                equation.push(int(equation.pop())*int(equation.pop()))
            elif input_ == '/':
                second = int(equation.pop())
                first = int(equation.pop())
                output = int(first / second)
                equation.push(output)
    return equation.pop()

def test_function(test_case):
    output = evaluate_post_fix(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")

test_case_1 = [["3", "1", "+", "4", "*"], 16]
test_function(test_case_1)

test_case_2 = [["4", "13", "5", "/", "+"], 6]
test_function(test_case_2)

test_case_3 = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22]
test_function(test_case_3)