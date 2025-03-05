# Código fuente adaptado de: https://www.geeksforgeeks.org/merge-sort/

# Algoritmo Merge Sort
# Recibe un array y devuelve el array ordenado
def mergeSort(arr):
    if len(arr) > 1:
        # elemento central
        mid = len(arr) // 2
        # Parte izquierda del array
        L = arr[:mid]
        #  Parte derecha del array
        R = arr[mid:]
        # Ordenamos parte izquierda
        mergeSort(L)
        # Ordenamos parte derecha
        mergeSort(R)

        # i es el indice del array L
        # j es el indice del array R
        # k es el indice del array final arr
        i = j = k = 0

        # Copiamos a arr los elementos de L y R de forma ordenada
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Si uno de los dos indices ha llegado al final se copian los del otro array
        # Si quedan elementos de L por copiar
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Si quedan elementos de R por copiar
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
