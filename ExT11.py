import abc
import random
import time
import numpy
import math

class Heap():
    def __init__(self, array):
        self.array = array
    def PosicionPadre(self, i):
        if i >= 2:
            return i//2
        return 0
    def PosicionHI(self, i):
        if 2*i <= len(self.array):
            return 2*i
        return 0
    def PosicionHD(self, i):
        if 2*i + 1 <= len(self.array):
            return 2*i + 1
        return 0
    def Intercambio(self,i,j): #recibe los indices de los elementos que hay que intercambiar en un array
        aux = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = aux
        return self.array #Los intercambia y devuelve el array.
    def TieneHi(self, i):#vemos si el nodo en la posición i tiene hijos
        return 2*i <= len(self.array)
    def TieneHd(self,i):
        return 2*i + 1 <= len(self.array)
    def Insert(self,x):
        self.array.append(x) #añadimos el elemento al heap
        m = self.array[0] #guardamos el valor del elemento minimo
        self.ExtractMin() #eliminamos el minimo y hacemos que el heap cumpla la propiedad
        if m < self.array[0]: #si el minimo es menor que el valor insertado
            self.array.insert(0,m) #lo añadimos en la primera posicion
        else:
            self.array.insert(1, m) #si no, lo añadimos en la segunda
        return self.array
    def ExtractMin(self): #Salida: El minimo que extraemos del Heap
        # El minimo es el nodo raiz, lo intercambiamos con el último elemento del array.
        if len(self.array) == 1: #si la lista es un solo elemento
            m = self.array[0] #guardamos su valor que es el minimo
            self.array.pop(0) #lo eliminamos
            return m#lo devolvemos
        aux = self.array[-1] #guardamos el valor del último elemento que tendremos que reordenar
        m = self.array[0] #guardamos el minimo
        self.array.pop(-1) # eliminamos el ultimo elemento
        self.array[0] = aux # lo pasamos al principio del array
        i = 0 #el indice del elemento a reordenar inicialmente es 0
        minimo = None
        # mientras el elemento a reordenar tiene hijos y es mayor que ellos
        while (self.TieneHi(i+1) and aux > self.array[self.PosicionHI(i+1)-1]) \
                or (self.TieneHd(i+1) and aux > self.array[self.PosicionHD(i+1)-1]):
            if self.TieneHi(i+1) and self.TieneHd(i+1): #si tiene ambos hijos
                x = self.PosicionHD(i+1)-1
                y = self.PosicionHI(i+1)-1
                if self.array[x] < self.array[y]:
                    minimo = x
                else:
                    minimo = y
            else: #si solo tiene hijo izquierdo
                minimo = self.PosicionHI(i+1)-1
            self.Intercambio(minimo,i) #intercambiamos el padre por el valor minimo de hijos
            i = minimo #el indice del elemento a reordenar ahora es el índice del hijo mínimo
        return m
    def FindMin(self,arr):
        return arr[0] #en un heap el mínimo es siempre el nodo raiz
    '''Heapify:
        arr = [1,2,3,4,5,6]
        H = Heap(arr)
       Delete:
        self.arr.pop(posición del objeto)'''
    @staticmethod #método estatico
    def HeapSort(lista): #pasamos la lista
        H = Heap(lista) #creamos el Heap
        resultado = [] #cremos la lista que finalmente será la ordenación
        while len(H.array) > 0: #si el array no es vacío
            resultado.append(H.ExtractMin()) #añadimo el mínimo a la lista
        return resultado


print('--------------------PRUEBAS-----------------------')

L = [4, 4, 8, 9, 4, 12, 9, 11, 13]
A = Heap(L)
print('El array inicial es: ' + str(L))
print('Con el 5 insertado: ' + str(A.Insert(5)))
print('El minimo es: ' + str(A.ExtractMin()))
print('La lista ordenada sin el minimo anterior es: ' + str(Heap.HeapSort(L)))

LL=[0,3,1,6,9,4,5,7,8,10]
He = Heap(LL)
print('El array inicial es: ' + str(LL))
print('Con el 6 insertado: ' + str(He.Insert(6)))
print('El minimo es: ' + str(He.ExtractMin()))
print('La lista ordenada sin el minimo anterior es: ' + str(Heap.HeapSort(LL)))

#La comparación está en la foto de la entrega

import numpy as np
f = open("ExerciciT11", "w")
i = 0
k = 30
n = 2500  # dando distintos valores de n, obtenemos el otras longitudes de lista.
tiempoHeapSort = 0
f.write('--------------N=2500---------------')
while i < k:
    f.write("------------------K = " + i.__str__() + "------------------" + "\n")
    llistaHeapSort = numpy.random.randint(0, 10000, n, int).tolist()
    H = Heap(llistaHeapSort)
    t1 = time.time_ns()
    Heap.HeapSort(llistaHeapSort)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoHeapSort += temps
    print("Tiempo HeapSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo HeapSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")

    i+=1

f.write("Tiempo Medio para HeapSort : " + (tiempoHeapSort / k).__str__() + " Seg" + "\n")
print("Tiempo Medio para HeapSort n=2500 : " + (tiempoHeapSort / k).__str__() + " Seg" + "\n")
f.write('--------------N=5000---------------')

i = 0
k = 30
n = 5000  # dando distintos valores de n, obtenemos el otras longitudes de lista.
tiempoHeapSort = 0


while i < k:
    f.write("------------------K = " + i.__str__() + "------------------" + "\n")
    llistaHeapSort = numpy.random.randint(0, 10000, n, int).tolist()
    H = Heap(llistaHeapSort)
    t1 = time.time_ns()
    Heap.HeapSort(llistaHeapSort)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoHeapSort += temps
    print("Tiempo HeapSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo HeapSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")

    i+=1

f.write("Tiempo Medio para HeapSort : " + (tiempoHeapSort / k).__str__() + " Seg" + "\n")
print("Tiempo Medio para HeapSort n= 5000: " + (tiempoHeapSort / k).__str__() + " Seg" + "\n")
f.write('--------------N=7500---------------')

i = 0
k = 30
n2 = 7500  # dando distintos valores de n, obtenemos el otras longitudes de lista.
tiempoHeapSort = 0



while i < k:
    f.write("------------------K = " + i.__str__() + "------------------" + "\n")
    llistaHS = numpy.random.randint(0, 10000, n2, int).tolist()
    H = Heap(llistaHS)
    t1 = time.time_ns()
    Heap.HeapSort(llistaHS)
    t2 = time.time_ns()

    temps = t2 - t1
    temps /= (10 ** 9)
    tiempoHeapSort += temps
    print("Tiempo HeapSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("Tiempo HeapSort para K = " + i.__str__() + " : " + temps.__str__())
    f.write("\n")

    i+=1

f.write("Tiempo Medio para HeapSort n=7500 : " + (tiempoHeapSort / k).__str__() + " Seg" + "\n")
print("Tiempo Medio para HeapSort n=7500 : " + (tiempoHeapSort / k).__str__() + " Seg" + "\n")

f.close()

L = [4, 4, 8, 9, 4, 12, 9, 11, 13]
A = Heap(L)

LL = []
B = Heap(LL)
B.Insert(3)

#grafo camino conj nodos no conexos que maximiza la suma
#mediana dos listas misma longitud t4
#algoritmo de ordenación con dyv
