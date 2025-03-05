import abc
import random
import time
import numpy
import math
# 1) Calcular la potencia de un número (con el exponente entero y positivo) aplicando la
# técnica de divide y vencerás

def PotenciaDYVExpPos(a,n):
    #Casos base
    if n==1:
        return str(a)
    elif n==0:
        return str(0)
    else:
        if n%2==0: #si el resto de la division entera es 0
            return PotenciaDYVExpPos(a,n/2)**2 #a^n=a^(n/2)*a^(n/2)
        else:
            return (PotenciaDYVExpPos(a,n/2)**2)*a #a^n=a^(n/2)*a^(n/2)*a
#n-1 multiplicaciones

# 2) Dada una lista ordenada de números sin repetidos, determinar si se encuentra o no un
#valor 𝑥 en la lista. Determinar el coste computacional

def EncontrarElementoTrueFalse(LL,a):
    #Casos base
    if len(LL)==1 and LL[0]==a:
        return True
    elif len(LL)==1 and LL[0]!=a:
        return False
    else:
        frac = len(LL)//2
        #dividimos la lista en dos partes
        L=LL[:frac]
        R=LL[frac:]
        if L[frac-1]<a: #si el elemento central izquierdo es menor que el que buscamos
            return EncontrarElementoTrueFalse(R,a) #buscamos el elemento en la parte derecha
        elif L[frac-1]>a:
            return EncontrarElementoTrueFalse(L,a) #si es mayor, lo buscamos a la izquierda
        else:
            return True #si el elemento es igual, ya está
#O(n^2)

def EncontrarIndiceElemento(LL,a,ini,fin):
    indice = (ini + fin) // 2 #dividimos la longitud de la lista entre 2
    if LL[indice] != a: #si el elemento central no es el qie buscamos
        if LL[indice] < a: #si es menor
            return EncontrarIndiceElemento(LL,a,indice+1,fin)#buscamos el elemento en la parte derecha
        elif LL[indice]> a: #si es mayor
            return EncontrarIndiceElemento(LL,a,ini,indice-1) #lo buscamos a la izquierda
    return indice

#O(n^2)
A=[34,56,78,99,122,3444,56666,89999]
print(EncontrarIndiceElemento(A,34,0,9))

#3) Dada una lista ordenada de números con repetidos, contar el número de apariciones
#de un número 𝑥 dado. Determinar el coste computacional.

contador=0
def ContarApariciones(LL,a):
    #casos base
    if len(LL)==1 and LL[0]==a:
        return contador+1
    elif len(LL)==1 and LL[0]!=a:
        return contador
    else:
        frac = len(LL)//2 #dividimos la lista en 2
        L=LL[:frac]
        R=LL[frac:]
        return ContarApariciones(L,a)+ContarApariciones(R,a) #contamos cuantas veces aparece el elemento a derecha e izquierda
#O(n^2)

# 4) Dadas dos listas ordenadas de igual tamaño, encontrar la mediana de la unión de
# ambas listas

def BuscarIndice(arr,a, ini, fin): #Para un elemento que no aparece en la lista
    while ini<fin: #mientras el marcador inicial sea menor que el final
        mid = (ini+fin)//2 #calculamos el centro entre marcadores
        if arr[mid] > a: #si el elemento central entre marcadores es mayor que el que buscamos
            return BuscarIndice(arr,a,ini,mid) #eliminamos la parte derecha del array
        elif arr[mid] < a: #si es menor
            return BuscarIndice(arr,a,mid+1,fin)#eliminamos la parte izquierda
        elif arr[mid] == a:
            return mid #si es igual, ya tenemos el índice
    return ini #cuando termina el bucle, ini = fin, si no se ha encontrado el elemento, se devuelve el índice en el que se encuentran.


#A=[1,3,5,7,9]
#print(BuscarIndice(A,6,0,4))


def MediaUnion(LL1,LL2,ini1,ini2,fin1,fin2): #entrada: 2 listas y sus 2 marcadores de inicio y fin respectivos
    #CASOS BASE
    if ini1==fin1: #Si los marcadores inicial y final de la lista 1 coinciden,
        indice1 = BuscarIndice(LL2,LL1[ini1],ini2,fin2) #buscamos el indice del elemento que se encuentra en la posición del marcador en la lista 2
        return (LL1[ini1]+LL2[indice1])/2 #devolvemos la media de estos dos elementos
    elif ini2==fin2: #Si los marcadores de la lista 2 coinciden, realizamos lo mismo.
        indice2 = BuscarIndice(LL1,LL2[ini2],ini1,ini2)
        return (LL1[indice2]+LL2[ini2])/2
    #PROGRAMA
    while fin1 > ini1 and fin2 > ini2: #mientras los marcadores no coincidan,
        mid1 = (ini1+fin1) // 2 #encontramos el indice central entre marcadores
        mid2 = BuscarIndice(LL2,LL1[mid1],ini2,fin2) #buscamos el indice del elemento entre marcadores de la primera lista en la segunda.
        if mid1 + mid2 >= len(LL1): #Vemos cuantos elementos hay a la izquierda de estos índices y los sumamos. Si es mayor o igual que la longitud de la lista
            return MediaUnion(LL1,LL2,ini1,ini2,mid1,mid2-1) #eliminamos la parte derecha del elemento en el centro de los marcadores.
        else: #si es menor
            return MediaUnion(LL1,LL2,mid1+1,mid2,fin1,fin2) #eliminamos la parte izquierda.
A=[1,3,5,7,9]
B=[0,2,4,6,8]
print(MediaUnion(A,B,0,0,4,4))

#5) Dada una lista ordenada, donde todos los elementos aparecen dos veces, excepto uno,
#que aparece una vez. Determinar cuál es y su posición


def DosYUno(LL):
    for i in range(len(LL)):
        a=ContarApariciones(LL,LL[i])
        if a == 2:
            pass
        else:
            return 'El elemento que aparece una sola vez es el ' + str(LL[i]) + ' en la posición ' + str(i+1)