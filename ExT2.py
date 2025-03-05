import abc


# 1) Calcular el coste (número de primitivas) del peor caso y del mejor caso del algoritmo de
# ordenación por Selección:
# Mejor caso (lista ya ordenada): (n^2-n)/2 = O(n^2/2)
# Peor caso (reordenar todos los numeros): (n^2+n)/2 = O(n^2/2)

# 2) Calcular el coste (número de primitivas) del peor caso y del mejor caso del algoritmo de
# ordenación por Inserción.
# Mejor caso (lista ya ordenada): n = O(n)
# Peor caso: (n-1)*n = O(n^2)

# 3) Implementar una función que calcula el factorial de un número, y determinar su coste
# asintótico (Big-O, Big-Omega y Big-Theta si existe).
def Factorial(n):
    factorial = 1
    j = n
    i = 0
    while i <= n - 1:
        factorial = factorial * j
        i = i + 1
        j -= 1
    return factorial


# Big-O, Big-Omega y Big-Theta = O(n)

# 4) Implementar una función que recibe dos matrices cuadradas de NxN y devuelve la matriz
# resultante de la multiplicación. Determinar su coste asintótico.

def multiplicarMatrius(A, B):
    filesA = len(A)
    filesB = len(B)
    columnesA = len(A[0])
    columnesB = len(B[0])
    multiplicacio = []
    for i in range(filesB):
        multiplicacio.append([])
        for j in range(columnesB):
            multiplicacio[i].append(None)
    for c in range(columnesB):
        for i in range(filesA):
            suma = 0
            for j in range(columnesA):
                suma += A[i][j] * B[j][c]
            multiplicacio[i][c] = suma
    return multiplicacio


# A = [ [1,2],[3,4]]
# B = [[5,4],[3,2]]
# print(multiplicarMatrius(A,B))

# Coste asintotico: 2n^2+n^3 = O(n^3)

# 5) Implementar una función que recibe una matriz cuadrada de NxN y devuelve el determinante
# de dicha matriz desarrollando siempre por la primera fila. Determinar su coste asintótico.
def determinante(A, C):
    print("entr")
    n = len(A)
    print("n es :" + n.__str__())
    i = 0
    a = 0
    b = 0
    if n <= 2:
        print((A[0][0] * A[1][1] - A[0][1] * A[1][0]).__str__() + " Assseeeere")
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    else:
        B = [[0] * (n - 1)] * (n - 1)
        #print("len es : " + len(B).__str__())
        for i in range(n):
            print("---------------------------")
            print("ronda " + i.__str__())
            b = 0
            for j in range(n):
                print("i es :" + i.__str__() + "j es :" + j.__str__())
                if i != C and j != C:
                    print("a es :" + a.__str__() + "  b es :" + b.__str__())
                    B[a][b] = A[i][j]
                    b += 1
            if i != C:
                a += 1
    for i in range(n):
        for j in range(n):
            A[i][j]
    A[0][C] * determinante(B, C + 1) -


A = [[0, 2, 3], [4, 6, 6], [10, 8, 9]]
print("DETERMINANT", determinante(A, 0).__str__())
#No he conseguido acabarlo, pero el orden sería el siguiente: O(n^4).
# desarrollando por filas es n!

#El método óptimo es gauss o(n^3), por recursividad.

# 6) Implementar una función que recibe una matriz cuadrada de NxN y devuelve la traza de dicha
# matriz. Determinar su coste asintótico.

def trazaMatriz(A):
    traza = 0
    n = len(A)
    i = 0
    while i <= n - 1:
        traza += A[i][i]
        i = i + 1
    return traza


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(trazaMatriz(A))

# coste asintótico = O(n)
