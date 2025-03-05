import abc
import random
import time
import numpy
import math


def QuickSort(arr):
    elements = len(arr)

    # Base case
    if elements < 2:
        return arr

    current_position = 0  # Position of the partitioning element

    for i in range(1, elements):  # Partitioning loop
        if arr[i] <= arr[0]:
            current_position += 1
            temp = arr[i]
            arr[i] = arr[current_position]
            arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position]
    arr[current_position] = temp  # Brings pivot to it's appropriate position
    #aquí copiamos listas, mejor con índices.
    left = QuickSort(arr[0:current_position])  # Sorts the elements to the left of pivot
    right = QuickSort(arr[current_position + 1:elements])  # sorts the elements to the right of pivot

    arr = left + [arr[current_position]] + right  # Merging everything together

    return arr

'''
PRUEBA
____________________________________________________-
array_to_be_sorted = [4, 2, 7, 3, 1, 6]
print("Original Array: ", array_to_be_sorted)
print("Sorted Array: ", QuickSort(array_to_be_sorted))
'''

#Algoritmo Sort de Python
def sort(A):
    A.sort()
    return A

# Algoritmo Selection Sort
def selection_sort(L):
    # i indicates how many items were sorted
    for i in range(len(L) - 1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i + 1, len(L) - 1):
            # Update the min_index if the element at j is lower than it
            if L[j] < L[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        L[i], L[min_index] = L[min_index], L[i]
    return L


# L = [3, 1, 41, 59, 26, 53, 59]
# print('lista inicial es', L)
# selection_sort(L)

# Let's see the list after we run the Selection Sort
# print('lista reordenada es',L)

# Algoritmo Insertion Sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Driver code to test above
# arr = [12, 11, 13, 5, 6]
# print('arr is', arr)
# insertionSort(arr)
# print("Sorted array is:")
# for i in range(len(arr)):
#   print("%d" % arr[i])

# Algoritmo Bubble Sort
def ordenamientoBurbujaCorto(unaLista):
    intercambios = True
    numPasada = len(unaLista) - 1
    while numPasada > 0 and intercambios:
        intercambios = False
        for i in range(numPasada):
            if unaLista[i] > unaLista[i + 1]:
                intercambios = True
                temp = unaLista[i]
                unaLista[i] = unaLista[i + 1]
                unaLista[i + 1] = temp
        numPasada = numPasada - 1


# unaLista=[20,30,40,90,50,60,70,80,100,110]
# print(unaLista)
# ordenamientoBurbujaCorto(unaLista)
# print(unaLista)


f = open("ExerciciT6.txt", "w")
i = 1
k = 30
n = 2500  # dando distintos valores de n, obtenemos el otras longitudes de lista.
tiempoSelectionSort = 0
tiempoInsertion = 0
tiempoBurbuja = 0
tiempoQuick = 0
tiempoSort = 0

f.write("-------- EJERCICIO T6 ------------" + "\n")
f.write("-------- Comenzamos con N=2500 ------------" + "\n")

while i <= k:
    f.write("------------------K = " + i.__str__() + "------------------" + "\n")
    llista = numpy.random.randint(0, 10000, n, int)
    llistaSelectionSort = llista.copy()
    llistaInsertion = llista.copy()
    llistaBurbuja = llista.copy()
    llistaQuick = llista.copy()
    llistaSort = llista.copy()

    t1 = time.time_ns()
    selection_sort(llistaSort)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoSelectionSort += temps
    print("Tiempo SelectionSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo SelectionSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")

    ##------------------------------------------------

    t1 = time.time_ns()
    insertionSort(llistaInsertion)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoInsertion += temps
    print("Tiempo InsertionSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo InsertionSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")

    ##------------------------------------------------

    t1 = time.time_ns()
    ordenamientoBurbujaCorto(llistaBurbuja)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoBurbuja += temps
    print("Tiempo BubbleSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo BubbleSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")
##------------------------------------------------

    t1 = time.time_ns()
    QuickSort(llistaQuick)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoQuick += temps
    print("Tiempo QuickSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo QuickSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")
    ##------------------------------------------------

    t1 = time.time_ns()
    sort(llistaSort)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoSort += temps
    print("Tiempo Sort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo Sort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")

    ##------------------------------------------------
    i+=1
f.write("---------------TIEMPOS MEDIOS (N=2500): ----------------" + "\n")


f.write("Tiempo Medio para SelectionSort : " + (tiempoSelectionSort / k).__str__() + " Seg" + "\n")
f.write("Tiempo Medio para InsertionSort : " + (tiempoInsertion / k).__str__() + " Seg" + "\n")
f.write("Tiempo Medio para BubbleSort: " + (tiempoBurbuja / k).__str__() + " Seg" + "\n")
f.write("Tiempo Medio para QuickSort: " + (tiempoQuick / k).__str__() + " Seg" + "\n")
f.write("Tiempo Medio para Sort: " + (tiempoSort / k).__str__() + " Seg" + "\n")

f.write("-------- Seguimos con N=7000 ------------" + "\n")

i = 1
k = 30
n = 7000
tiempoSelectionSort = 0
tiempoInsertion = 0
tiempoBurbuja = 0
tiempoQuick = 0
tiempoSort = 0


while i <= k:
    f.write("------------------K = " + i.__str__() + "------------------" + "\n")
    llista = numpy.random.randint(0, 10000, n, int)
    llistaSelectionSort = llista.copy()
    llistaInsertion = llista.copy()
    llistaBurbuja = llista.copy()
    llistaQuick = llista.copy()
    llistaSort = llista.copy()

    t1 = time.time_ns()
    selection_sort(llistaSort)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoSelectionSort += temps
    print("Tiempo SelectionSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo SelectionSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")

    ##------------------------------------------------

    t1 = time.time_ns()
    insertionSort(llistaInsertion)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoInsertion += temps
    print("Tiempo InsertionSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo InsertionSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")

    ##------------------------------------------------

    t1 = time.time_ns()
    ordenamientoBurbujaCorto(llistaBurbuja)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoBurbuja += temps
    print("Tiempo BubbleSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo BubbleSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")
##------------------------------------------------

    t1 = time.time_ns()
    QuickSort(llistaQuick)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoQuick += temps
    print("Tiempo QuickSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo QuickSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")
    ##------------------------------------------------

    t1 = time.time_ns()
    sort(llistaSort)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoSort += temps
    print("Tiempo Sort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo Sort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")

    ##------------------------------------------------
    i+=1
f.write("---------------TIEMPOS MEDIOS (N = 7000: ----------------" + "\n")


f.write("Tiempo Medio para SelectionSort : " + (tiempoSelectionSort / k).__str__() + " Seg" + "\n")
f.write("Tiempo Medio para InsertionSort : " + (tiempoInsertion / k).__str__() + " Seg" + "\n")
f.write("Tiempo Medio para BubbleSort: " + (tiempoBurbuja / k).__str__() + " Seg" + "\n")
f.write("Tiempo Medio para QuickSort: " + (tiempoQuick / k).__str__() + " Seg" + "\n")
f.write("Tiempo Medio para Sort: " + (tiempoSort / k).__str__() + " Seg" + "\n")


f.write("-------- Para acabar, N=10000 ------------" + "\n")

i = 1
k = 30
n = 10000
tiempoSelectionSort = 0
tiempoInsertion = 0
tiempoBurbuja = 0
tiempoQuick = 0
tiempoSort = 0


while i <= k:
    f.write("------------------K = " + i.__str__() + "------------------" + "\n")
    llista = numpy.random.randint(0, 10000, n, int)
    llistaSelectionSort = llista.copy()
    llistaInsertion = llista.copy()
    llistaBurbuja = llista.copy()
    llistaQuick = llista.copy()
    llistaSort = llista.copy()

    t1 = time.time_ns()
    selection_sort(llistaSort)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoSelectionSort += temps
    print("Tiempo SelectionSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo SelectionSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")

    ##------------------------------------------------

    t1 = time.time_ns()
    insertionSort(llistaInsertion)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoInsertion += temps
    print("Tiempo InsertionSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo InsertionSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")

    ##------------------------------------------------

    t1 = time.time_ns()
    ordenamientoBurbujaCorto(llistaBurbuja)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoBurbuja += temps
    print("Tiempo BubbleSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo BubbleSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")
##------------------------------------------------

    t1 = time.time_ns()
    QuickSort(llistaQuick)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoQuick += temps
    print("Tiempo QuickSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo QuickSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")
    ##------------------------------------------------

    t1 = time.time_ns()
    sort(llistaSort)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoSort += temps
    print("Tiempo Sort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo Sort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")

    ##------------------------------------------------
    i+=1
f.write("---------------TIEMPOS MEDIOS (N = 10000: ----------------" + "\n")


f.write("Tiempo Medio para SelectionSort : " + (tiempoSelectionSort / k).__str__() + " Seg" + "\n")
f.write("Tiempo Medio para InsertionSort : " + (tiempoInsertion / k).__str__() + " Seg" + "\n")
f.write("Tiempo Medio para BubbleSort: " + (tiempoBurbuja / k).__str__() + " Seg" + "\n")
f.write("Tiempo Medio para QuickSort: " + (tiempoQuick / k).__str__() + " Seg" + "\n")
f.write("Tiempo Medio para Sort: " + (tiempoSort / k).__str__() + " Seg" + "\n")

f.write("-------En definitiva:----------" + "\n")
f.write("Claramente el método sort de Python es el más rápido debido a su ejecución en código máquina" + "\n" +
        "Por otra parte, el siguiente más rápido es el Quick sort. O(nlogn).")

f.close()

