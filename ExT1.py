import abc
import random
import time
import numpy


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


f = open("ExerciciT1N2500.txt", "w")
i = 0
k = 30
n = 2500  # dando distintos valores de n, obtenemos el otras longitudes de lista.
tiempoSort = 0
tiempoInsertion = 0
tiempoBurbuja = 0

f.write("-------- EJERCICIO LISTAS ------------" + "\n")
while i < k:
    f.write("------------------K = " + i.__str__() + "------------------" + "\n")
    llista = numpy.random.randint(0, 10000, n, int)
    llistaSort = llista.copy()
    llistaInsertion = llista.copy()
    llistaBurbuja = llista.copy()

    t1 = time.time_ns()
    selection_sort(llistaSort)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoSort += temps
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
    i+=1

f.write("Tiempo Medio para SelectionSort : " + (tiempoSort / k).__str__() + " Seg" + "\n")
f.write("Tiempo Medio para InsertionSort : " + (tiempoInsertion / k).__str__() + " Seg" + "\n")
f.write("Tiempo Medio para BubbleSort: " + (tiempoBurbuja / k).__str__() + " Seg" + "\n")

f.close()