import abc
import random
import time
import numpy
import math

# 1) Calcular la potencia de un número, con el exponente entero y positivo

def PotenciaEnteroPositivo(a,n): # a es la base, n el exponente
    if isinstance(n,int) and n > 0:
        #caso base, n = 1
        if n == 1:
            return a
        return PotenciaEnteroPositivo(a,n-1)*a
    else:
        return 'En la potencia de base'+ str(a) + 'y exponente' + str(n) + 'El exponente no es entero positivo'

# 2) Calcular la potencia de un número, con el exponente entero (debe funcionar para
# positivos y negativos)

def PotenciaEntero(a,n):
    if isinstance(n,int) and n > 0:
        return PotenciaEnteroPositivo(a,n)
    elif isinstance(n,int) and n < 0:
        if n == -1:
            return 1/a
        return PotenciaEntero(a,n+1)
    else:
        return 'En la potencia de base' + str(a) + 'y exponente' + str(n) + 'El exponente no es entero'

# 3) Sumar los dígitos de un número de forma recursiva: suma_digitos de 487261 = 1 +
# suma_digitos de 48726
def SumarDigits(n):
    if n // 10 == 0:
        return n
    else:
        d = n % 10
    return d + SumarDigits(n//10)

# 4) Calcular el determinante de una matriz cuadrada

def DesarrollarPorPrimeraFila(A,f):
    FilaActual = 1
    B = []
    while FilaActual < len(A):
        B.append((A[FilaActual][:f]+A[FilaActual][f+1:]))
        FilaActual += 1
    return B


def Determinant(A):
    if len(A) == len(A[0]): #si la matriz es cuadrada
        if len(A)==1: #Casos base len=1
            return A[0][0]
        else:
                determinant = 0
                for i in range(len(A[0])):
                    determinant += ((-1)**i)*A[0][i]*Determinant(DesarrollarPorPrimeraFila(A,i))
                return determinant


# 5) Calcular el máximo de una lista, determinar el número mínimo de comparaciones
def MaxLista(L):
    if len(L) == 1:
        return L[0]
    else:
        max = L[-1]
        max2 = MaxLista(L[:-1])
        if max < max2:
            return max2
        else:
            return max

#El número mínimo de comparaciones es len(L)-1


"""

PRUEBAS
_____________________________________
print(PotenciaEnteroPositivo(3,-2))
print(PotenciaEnteroPositivo(3,4))
print(PotenciaEntero(3,-4))
print(PotenciaEntero(3,3.14))
print(PotenciaEntero(3,2))
print(SumarDigits(74359))
L=[1,2,4,5]
print(MaxLista(L))
A=[[1,0,0],[0,1,0],[0,0,1]]
B=[[4,1],[3,2]]
print(DesarrollarPorPrimeraFila(A,1))
print(Determinant(A))
print(Determinant(B))

"""