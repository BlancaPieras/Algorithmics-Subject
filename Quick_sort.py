def quickSort(l):
    quickSort_internal(l, 0, len(l))


def quickSort_internal(l, ini, fin):
    if ini >= fin:
        return l
    else:
        j = partition(l, ini, fin)
        quickSort_internal(l, ini, j)
        quickSort_internal(l, j + 1, fin)


def partition(l, ini, fin):
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
