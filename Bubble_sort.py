# Ordenacion por el método de la burbuja
# Realiza la ordenacion sobre la misma lista recibida
def bubbleSort(l):
    size = len(l)
    for i in range(size-1):
        for j in range(0, size-i-1):
            if l[j] > l[j+1]:
                # intercambio de elementos
                l[j], l[j+1] = l[j+1], l[j]

