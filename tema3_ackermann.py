import time

# función recursiva ackerman
def ackermann(m, n):
    # caso base
    if m == 0:
        return n+1
    # recursividad
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))


m = 3
n = 2

t = time.time_ns()
valor = ackermann(m, n)
tiempo = (time.time_ns()-t)/(10**9)
print(valor, tiempo)

