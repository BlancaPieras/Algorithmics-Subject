# Ordenacion por el método de inserción
# Realiza la ordenacion sobre la misma lista recibida
def insertionSort(l):
    size = len(l)
    for i in range(1, size):
        value = l[i]
        j = i-1
        while j >= 0 and value < l[j]:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = value
