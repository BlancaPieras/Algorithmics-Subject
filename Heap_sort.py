from Heap import Heap


def heapSort(l):
    h = Heap()
    for x in l:
        h.insert(x)

    index = 0
    x = h.extract_min()
    while x != None:
        l[index] = x
        index += 1
        x = h.extract_min()
