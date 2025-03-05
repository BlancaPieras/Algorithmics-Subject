# Algoritmo Merge Sort dividiendo el problema en 3 partes
# Recibe un array y devuelve el array ordenado


def merge3Sort(arr):
    size = len(arr)
    # caso base, un elemento
    if size == 1:
        return

    # caso base, dos elementos
    if size == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return

    # size > 2:

    # Indices de separacion de las tres partes del array
    ter = size // 3
    dos_ter = (size*2)//3

    # Parte izquierda del array
    L = arr[:ter]
    # Parte intermedia del array
    M = arr[ter:dos_ter]
    # Parte derecha del array
    R = arr[dos_ter:]

    # Ordenamos parte izquierda
    merge3Sort(L)
    # Ordenamos parte media
    merge3Sort(M)
    # Ordenamos parte derecha
    merge3Sort(R)

    # l es el indice del array L
    # m es el indice del array M
    # r es el indice del array R
    # z es el indice del array final arr
    l = m = r = a = 0

    # Copiamos a arr los elementos de L, M y R de forma ordenada
    # como mucho hará 9 operaciones en cada iteracion
    while l < len(L) and m < len(M) and r < len(R): # 3 comparaciones
        if L[l] < M[m] and L[l] < R[r]: # 2 comparaciones
            # 2 operaciones
            arr[a] = L[l]
            l += 1
        elif M[m] < R[r]: # 2 comparaciones
            # 2 operaciones
            arr[a] = M[m]
            m += 1
        else:
            # 2 operaciones
            arr[a] = R[r]
            r += 1
        a += 1 # 1 operacion

    # Copiamos a arr los elementos de L y R de forma ordenada
    # como mucho hará 6 operaciones en cada iteracion
    while l < len(L) and r < len(R): # 2 comparaciones
        if L[l] < R[r]: # 1  comparacion
            # 2 operaciones
            arr[a] = L[l]
            l += 1
        else:
            # 2 operaciones
            arr[a] = R[r]
            r += 1
        a += 1 # 1 operacion

    # Copiamos a arr los elementos de L y M de forma ordenada
    # como mucho hará 6 operaciones en cada iteracion
    while l < len(L) and m < len(M): # 2 comparaciones
        if L[l] < M[m]: # 1 comparacion
            # 2 operaciones
            arr[a] = L[l]
            l += 1
        else:
            # 2 operaciones
            arr[a] = M[m]
            m += 1
        a += 1 # 1 operacion

    # Copiamos a arr los elementos de M y R de forma ordenada
    # como mucho hará 6 operaciones en cada iteracion
    while m < len(M) and r < len(R): # 2 comparaciones
        if M[m] < R[r]: # 1 comparacion
            arr[a] = M[m]
            m += 1
        else:
            arr[a] = R[r]
            r += 1
        a += 1 # 1 operacion

    # Si uno de los dos indices ha llegado al final se copian los del otro array
    # Si quedan elementos de L por copiar
    while l < len(L):
        arr[a] = L[l]
        l += 1
        a += 1

    # Si quedan elementos de M por copiar
    # como mucho hará 4 operaciones
    while m < len(M):
        arr[a] = M[m]
        m += 1
        a += 1

    # Si quedan elementos de R por copiar
    # como mucho hará 4 operaciones
    while r < len(R):
        arr[a] = R[r]
        r += 1
        a += 1

    # Explicacion de la cota superior el numero de operaciones
    # tenemos 2 operaciones iniciales
    # la copia de 3 listas que son n operaciones
    # 4 operaciones de asignación
    # y a continuación, 7 bucles

    # bucle 3 arrays (LMR)  --> 9 operaciones por iteracion
    # bucle 2 arrays (LR)   --> 6 operaciones por iteracion
    # bucle 2 arrays (LM)   --> 6 operaciones por iteracion
    # bucle 2 arrays (MR)   --> 6 operaciones por iteracion
    # bucle array (L)       --> 4 operaciones por iteracion
    # bucle array (M)       --> 4 operaciones por iteracion
    # bucle array (R)       --> 4 operaciones por iteracion

    # el peor de los casos es cuando todas las copias (menos dos) se realizan en el primer bucle
    # si en el primer bucle termina cualquier de los dos arrays reduce el número de oepraciones
    # luego la cota superior del número de operaciones que se realiza viene dado por 9n
    # más un número constante de operaciones

    # Luego pasamos a los bucles de dos listas
    # teniendo 6 comparaciones (dos por bucle) de las cuales entrará en un bucle
    # teniendo 4 operaciones para el bucle de dos listas

    # Luego pasamos a los bucles de una lista
    # teniendo 3 comparaciones (una por bucle) de las cuales entrará en un bucle
    # teniendo 3 operaciones para el bucle de una lista

    # luego la cota superior es 2 + n + 4 + 9n + 10 + 6 = 22 + 10n

    # el número de llamadas que se realiza es log_3(n)+1
    # luego la cota superior del algoritmo completo es
    # (log_3(n)+1)*(22+10n)
    # pero cuidado!!!
    # hemos al requerir más memoria hay operaciones "ocultas" al tener que adquirir memoria