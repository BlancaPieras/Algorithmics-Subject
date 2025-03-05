# función recursiva factorial
def factorial(n):
    # caso base
    if n == 0:
        return 1
    # recursividad de cola
    return n * factorial(n-1)

print(factorial(200))