from StackLinkedList import Stack

def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    
    
    equation_ = Stack()
    for char in equation:
        equation_.push(char)
    
    char1,char2 = '(',')'
    count1,count2 = 0,0
    for item in equation:
        if item == '(':
            count1 += 1
        elif item == ')':
            count2 += 1
            
    if(count1 == count2):
        return True
    
    return False

print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")