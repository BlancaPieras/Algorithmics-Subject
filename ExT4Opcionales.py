import abc
import random
import time
import numpy
import math
#7) Dadas dos listas ordenadas (no hacemos suposición de que son de igual longitud),
#encontrar la mediana de la unión de ambas listas.

def BuscarIndice(arr,a, ini, fin):
    while ini<fin:
        mid = (ini+fin)//2
        if arr[mid] > a:
            return BuscarIndice(arr,a,ini,mid)
        elif arr[mid] < a:
            return BuscarIndice(arr,a,mid+1,fin)
    return ini

def MediaUnion2(LL1,LL2,ini1,ini2,fin1,fin2):
    if ini1==fin1:
        indice1 = BuscarIndice(LL2,LL1[ini1],ini2,fin2)
        return (LL1[ini1]+LL2[indice1])/2
    elif ini2==fin2:
        indice2 = BuscarIndice(LL1,LL2[ini2],ini1,ini2)
        return (LL1[indice2]+LL2[ini2])/2
    while fin1 > ini1 and fin2 > ini2:
        mid1 = (ini1+fin1) // 2
        mid2 = BuscarIndice(LL2,LL1[mid1],ini2,fin2)
        if mid1 + mid2 >= (len(LL1)+len(LL2))//2: #Solo cambiamos el hecho de que la suma del numero de elementos a la izquierda
            #de los marcadores debe compararse con la longitud de la unión de las listas / 2 ya que no tienen la misma dimensión.
            return MediaUnion2(LL1,LL2,ini1,ini2,mid1,mid2-1)
        else:
            return MediaUnion2(LL1,LL2,mid1+1,mid2,fin1,fin2)
A=[1,3,5,7,9]
B=[0,2,4,6,8,10,12,13,45]
print(UnaVainaLoca(A,B,0,0,5,9))



#8. Dada una matriz A de N filas x N columnas, donde los valores están ordenados
#(primera fila los valores más pequeños, dentro de cada fila están ordenados).
#Encontrar si existe el elemento con valor K.

def EncontrarElementoTrueFalse(LL,a):
    if len(LL)==1 and LL[0]==a:
        return True
    elif len(LL)==1 and LL[0]!=a:
        return False
    else:
        frac = len(LL)//2
        L=LL[:frac]
        R=LL[frac:]
        if L[frac-1]<a:
            return EncontrarElementoTrueFalse(R,a)
        elif L[frac-1]>a:
            return EncontrarElementoTrueFalse(L,a)
        else:
            return True

def EstaEsteMatriz(A,a): #devuelve True si está y None si no.
    for i in range(len(A)):
        if EncontrarElementoTrueFalse(A[i],a) == True:
            i=i+1
            return True
        else:
            i=i+1
            pass
"""
A=[[1,4,8,10],[12,13,25,31],[32,40,49,52],[59,62,63,65]]
print(EstaEsteMatriz(A,40))
print(EstaEsteMatriz(A,2))
"""
