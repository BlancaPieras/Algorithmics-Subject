"""
OPCIONAL
_____________________________________________________________________________________________________________
"""
def EncontrarElemento(LL,a):
    if len(LL)==1 and LL[0]==a:
        return True
    elif len(LL)==1 and LL[0]!=a:
        return False
    else:
        frac = len(LL)//2
        L=LL[:frac]
        R=LL[frac:]
        if L[frac-1]<a:
            return EncontrarElemento(R,a)
        elif L[frac-1]>a:
            return EncontrarElemento(L,a)
        else:
            return True
        
#8. Dada una matriz A de N filas x N columnas, donde los valores están ordenados
#(primera fila los valores más pequeños, dentro de cada fila están ordenados).
#Encontrar si existe el elemento con valor K.

def EstaEsteMatriz(A,a): #devuelve True si está y None si no.
    for i in range(len(A)):
        if EncontrarElemento(A[i],a) == True:
            i=i+1
            return True
        else:
            i=i+1
            pass

