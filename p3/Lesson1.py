def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    precisao=1e-10
    if number < 0:
        raise ValueError("O valor de 'n' deve ser não negativo")
    
    if number == 0 or number == 1:
        return number

    esquerda, direita = 0, number
    raiz = (esquerda + direita) / 2

    while abs(raiz * raiz - number) > precisao:
        if raiz * raiz < number:
            esquerda = raiz
        else:
            direita = raiz
        raiz = (esquerda + direita) / 2

    return round(raiz)

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")