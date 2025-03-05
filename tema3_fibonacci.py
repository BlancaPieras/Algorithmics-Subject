import math


# función recursiva fibonacci
def fibonacci(n):
    # caso base n = 0 --> 0     n=1 --> 1
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# calculo del n-esimo valor de la serie de fibonacci mediante la formula
def formula_fibonacci(n):
    raiz_5 = math.sqrt(5)
    phi = (1 + raiz_5) / 2
    psi = (1 - raiz_5) / 2
    return int((pow(phi, n) - pow(psi, n)) / raiz_5)


num = 10
# print(formula_fibonacci(num))
print(fibonacci(num))
