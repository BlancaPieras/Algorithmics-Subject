import abc
import random
import time
import numpy
import math

def QuickSortOriginal(arr):
    elements = len(arr)
    if elements < 2: # Base case
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
    left = QuickSortOriginal(arr[0:current_position])  # Sorts the elements to the left of pivot
    right = QuickSortOriginal(arr[current_position + 1:elements])  # sorts the elements to the right of pivot
    arr = left + [arr[current_position]] + right  # Merging everything together
    return arr

def MediaQuickSort(arr):
    arr.sort() #ordenamos la lista
    if len(arr)==5:
        return arr[2] #si tiene longitud 5, la mediana es el elemento central
    elif len(arr)==4 or len(arr)==3:
        return arr[1] #si es 4 o 3, la mediana es el segundo elemento
    elif len(arr)==2 or len(arr)==1:
        return arr[0] #si es 1 o 2, el primero

#Usareos este método para buscar el índice del pivote
def BuscarIndice(arr,a, ini, fin): #Para un elemento que no aparece en la lista
    while ini<fin:
        mid = (ini+fin)//2
        if arr[mid] > a:
            return BuscarIndice(arr,a,ini,mid)
        elif arr[mid] < a:
            return BuscarIndice(arr,a,mid+1,fin)
        elif arr[mid] == a:
            return mid
    return ini

def QuickSort1(arr):
    # Selección del pivote
    if len(arr)>5:
        division = len(arr)//4 #dividimos la longitud de la lista en 4 para hallar los elementos:
        lista = []
        lista.append(arr[0])#primero
        lista.append(arr[division-1])#25%
        lista.append(arr[2*division-1])#50%
        lista.append(arr[3*division-1])#75%
        lista.append(arr[len(arr)-1])#último
        pivote = MediaQuickSort(lista) #hallamos la media de la lista con los elementos anteriores
    else:
        pivote=MediaQuickSort(arr) #si la longitud del array es menor que 5, el pivote es la media de él mismo
    fin = len(arr)-1
    IndicePivote = BuscarIndice(arr,pivote,0,fin) #buscamos el índice del pivote en el array
    aux = arr[0] #asignamos el primer valor de la lista a una variable auxiliar
    arr[0] = arr[IndicePivote] #cambiamos el valor del primer elemento de la lista por el pivote
    arr[IndicePivote] = aux #y el pivote por el primer valor de la lista
    return QuickSortOriginal(arr) #Quick sort 1

def QuickSort2(arr):
    if len(arr)>5:
        llista = random.sample(list(arr), 5) #generamos una lista aleatoria de 5 valores dentro de la lista
        pivote = MediaQuickSort(llista) #el pivote será la mediana de la lista.
    else:
        pivote = MediaQuickSort(arr) #si la longitud de la lista es menor que 5, calculamos la mediana del propio array
    fin = len(arr)-1
    IndicePivote = BuscarIndice(arr, pivote, 0, fin) #buscamos el índice del pivote
    aux = arr[0] #intercambiamos el primer el emento de la lista con el pivote.
    arr[0] = arr[IndicePivote]
    arr[IndicePivote] = aux
    return QuickSortOriginal(arr) #Aplicamos el QuickSort 2!!!.


f = open("ExerciciT7.txt", "w")
i = 1
k = 30
n = 2500  # dando distintos valores de n, obtenemos el otras longitudes de lista.
tiempoQuick = 0
tiempoQuick1 = 0
tiempoQuick2 = 0


f.write("-------- EJERCICIO T7 ------------" + "\n")
f.write("-------- Comenzamos con N=2500 ------------" + "\n")

while i <= k:
    f.write("------------------K = " + i.__str__() + "------------------" + "\n")
    llista = numpy.random.randint(0, 10000, n, int)
    llistaQuick = llista.copy()
    llistaQuick1 = llista.copy()
    llistaQuick2 = llista.copy()

    t1 = time.time_ns()
    QuickSortOriginal(llistaQuick)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoQuick += temps
    print("Tiempo QuickSortOriginal para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo QuickSortOriginal para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")

    ##------------------------------------------------

    t1 = time.time_ns()
    QuickSort1(llistaQuick1)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoQuick1 += temps
    print("Tiempo Quick1 para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo Quick1 para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")

    ##------------------------------------------------

    t1 = time.time_ns()
    QuickSort2(llistaQuick2)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoQuick2 += temps
    print("Tiempo quick2 para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo quick2 para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")
##------------------------------------------------
    i+=1

f.write("---------------TIEMPOS MEDIOS (N=2500): ----------------" + "\n")


f.write("Tiempo Medio para quick: " + (tiempoQuick / k).__str__() + " Seg" + "\n")
f.write("Tiempo Medio para InsertionSort : " + (tiempoQuick1 / k).__str__() + " Seg" + "\n")
f.write("Tiempo Medio para BubbleSort: " + (tiempoQuick2 / k).__str__() + " Seg" + "\n")
f.write("-------- Seguimos con N=7000 ------------" + "\n")


i = 1
k = 30
n = 7000  # dando distintos valores de n, obtenemos el otras longitudes de lista.
tiempoQuick = 0
tiempoQuick1 = 0
tiempoQuick2 = 0

while i <= k:
    f.write("------------------K = " + i.__str__() + "------------------" + "\n")
    llista = numpy.random.randint(0, 10000, n, int)
    llistaQuick = llista.copy()
    llistaQuick1 = llista.copy()
    llistaQuick2 = llista.copy()

    t1 = time.time_ns()
    QuickSortOriginal(llistaQuick)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoQuick += temps
    print("Tiempo QuickSortOriginal para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo QuickSortOriginal para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")

    ##------------------------------------------------

    t1 = time.time_ns()
    QuickSort1(llistaQuick1)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoQuick1 += temps
    print("Tiempo Quick1 para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo Quick1 para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")

    ##------------------------------------------------

    t1 = time.time_ns()
    QuickSort2(llistaQuick2)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoQuick2 += temps
    print("Tiempo quick2 para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo quick2 para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")
##-------------------------------------------------
    i+=1

f.write("---------------TIEMPOS MEDIOS (N=7000): ----------------" + "\n")

f.write("Tiempo Medio para quick: " + (tiempoQuick / k).__str__() + " Seg" + "\n")
f.write("Tiempo Medio para InsertionSort : " + (tiempoQuick1 / k).__str__() + " Seg" + "\n")
f.write("Tiempo Medio para BubbleSort: " + (tiempoQuick2 / k).__str__() + " Seg" + "\n")
f.write("-------- Seguimos con N=7000 ------------" + "\n")

i = 1
k = 30
n = 10000  # dando distintos valores de n, obtenemos el otras longitudes de lista.
tiempoQuick = 0
tiempoQuick1 = 0
tiempoQuick2 = 0

while i <= k:
    f.write("------------------K = " + i.__str__() + "------------------" + "\n")
    llista = numpy.random.randint(0, 10000, n, int)
    llistaQuick = llista.copy()
    llistaQuick1 = llista.copy()
    llistaQuick2 = llista.copy()

    t1 = time.time_ns()
    QuickSortOriginal(llistaQuick)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoQuick += temps
    print("Tiempo QuickSortOriginal para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo QuickSortOriginal para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")

    ##------------------------------------------------

    t1 = time.time_ns()
    QuickSort1(llistaQuick1)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoQuick1 += temps
    print("Tiempo Quick1 para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo Quick1 para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")

    ##------------------------------------------------

    t1 = time.time_ns()
    QuickSort2(llistaQuick2)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoQuick2 += temps
    print("Tiempo quick2 para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo quick2 para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")
##------------------------------------------------
    i+=1

f.write("---------------TIEMPOS MEDIOS (N=10000): ----------------" + "\n")

f.write("Tiempo Medio para quick: " + (tiempoQuick / k).__str__() + " Seg" + "\n")
f.write("Tiempo Medio para quick1 : " + (tiempoQuick1 / k).__str__() + " Seg" + "\n")
f.write("Tiempo Medio para quick2: " + (tiempoQuick2 / k).__str__() + " Seg" + "\n")
f.write("-------- Seguimos con N=7000 ------------" + "\n")

f.close()