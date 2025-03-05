import time

# función recursiva numero combinatorio
def n_sobre_k(n, k):
    # casos base
    if k == 0 or n == k:
        return 1
    if n == 0:
        return 0
    # recursividad
    return n_sobre_k(n-1, k-1) + n_sobre_k(n-1, k)


# función recursiva factorial
def factorial(n):
    # caso base
    if n == 0:
        return 1
    # recursividad de cola
    return n*factorial(n-1)


# calculo directo n sobre k
def formula_n_sobre_k(n, k):
    # n!/((n-k!)*k!)
    return factorial(n)//(factorial(n-k)*factorial(k))


n = 24
k = 10

t = time.time_ns()
valor = n_sobre_k(n, k)
tiempo = (time.time_ns()-t)/(10**9)
print(valor, tiempo)

t = time.time_ns()
valor = formula_n_sobre_k(n, k)
tiempo = (time.time_ns()-t)/(10**9)
print(valor, tiempo)
