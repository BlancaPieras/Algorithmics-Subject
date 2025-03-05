import random


def quickSort(l):
    quickSort_internal(l, 0, len(l), primero)


def quickSort_posiciones(l):
    quickSort_internal(l, 0, len(l), posicion)


def quickSort_aleatorio(l):
    quickSort_internal(l, 0, len(l), aleatorio)


def primero(l, ini, fin):
    pass


def get_mayor_menor(valor, a, b, c, d, e):
    count_menor = count_mayor = 0
    if a >= valor:
        count_mayor += 1
    if a <= valor:
        count_menor += 1
    if b >= valor:
        count_mayor += 1
    if b <= valor:
        count_menor += 1
    if c >= valor:
        count_mayor += 1
    if c <= valor:
        count_menor += 1
    if d >= valor:
        count_mayor += 1
    if d <= valor:
        count_menor += 1
    if e >= valor:
        count_mayor += 1
    if e <= valor:
        count_menor += 1

    return count_menor, count_mayor


def get_median(l, id0, id1, id2, id3, id4):
    v0, v1, v2, v3, v4 = l[id0], l[id1], l[id2], l[id3], l[id4]
    for id, v in zip([id0, id1, id2, id3, id4], [v0, v1, v2, v3, v4]):
        v_men, v_may = get_mayor_menor(v, v0, v1, v2, v3, v4)
        if v_men >= 3 and v_may >= 3:
            return id


def posicion(l, ini, fin):
    num_elements = fin - ini
    indice = (ini + fin) // 2
    if num_elements >= 5:
        id0 = ini
        id1 = ini + num_elements // 4
        id2 = ini + (num_elements * 2) // 4
        id3 = ini + (num_elements * 3) // 4
        id4 = fin-1
        indice = get_median(l, id0, id1, id2, id3, id4)
    if indice != ini:
        l[ini], l[indice] = l[indice], l[ini]


def aleatorio(l, ini, fin):
    num_elements = fin - ini
    indice = (ini + fin) // 2
    if num_elements >= 5:
        id0 = random.randint(ini, fin-1)
        id1 = random.randint(ini, fin-1)
        id2 = random.randint(ini, fin-1)
        id3 = random.randint(ini, fin-1)
        id4 = random.randint(ini, fin-1)
        indice = get_median(l, id0, id1, id2, id3, id4)
    if indice != ini:
        l[ini], l[indice] = l[indice], l[ini]


def quickSort_internal(l, ini, fin, p_method):
    if ini >= fin:
        return l
    else:
        j = partition(l, ini, fin, p_method)
        quickSort_internal(l, ini, j, p_method)
        quickSort_internal(l, j + 1, fin, p_method)


def partition(l, ini, fin, p_method):
    p_method(l, ini, fin)
    pivot = l[ini]
    i = ini + 1
    for j in range(ini + 1, fin):
        if l[j] < pivot:
            # intercambio
            l[i], l[j] = l[j], l[i]
            i += 1
    # intercambio
    l[ini], l[i - 1] = l[i - 1], l[ini]
    return i - 1
