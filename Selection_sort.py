# Ordenacion por el método de Selección del mínimo
# Realiza la ordenacion sobre la misma lista recibida
def selectionSort(l):
    size = len(l)
    i = 0
    while i < size:
        idx = i
        for j in range(i+1, size):
            if l[j] < l[idx]:
                idx = j
        l[i], l[idx] = l[idx], l[i]
        i += 1
