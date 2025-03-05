import abc
import random
import time
import numpy
import math

class Nodo():
    def __init__(self, nombre = ''):
        self.__nombre = nombre
        self.ListaAristas = []
        self.nivel = 100000 #Valor que no se alcanza (infinito)
        self.explorado = False #Marcamos todos los nodos como no explorados inicialmente
        self.FdeNodo = None #f(nodo) inicialmente no tiene valor para la ordenación topológica
        self.distancia = 100000000  # infinito inicialmente
    def __repr__(self):
        return self.__nombre #el representante de un elemento de la clase nodo es su nombre
    def AgregarAristaNodo(self,arista):
        self.ListaAristas.append(arista)
    def getListaAristasNodo(self): #lista de aristas que salen de un nodo
        return self.ListaAristas

class Arista():
    identificador = 0
    def __init__(self, origen, destino):
        self.__origen = origen
        self.__destino = destino
        self.__identificador = Arista.identificador
        self.__nombre = str((origen,destino))
        Arista.identificador += 1 #Asigna un valor a cada nueva arista que se crea
    def __repr__(self):
        return self.__nombre #El representante d eun elemento de la clase arista es su nombre
    def GetDestino(self):
        return self.__destino
    def GetOrigen(self):
        return self.__origen
    def AristasIguales(self,arista):
        if isinstance(arista,Arista):
            if arista.__nombre == self.__nombre:
                return True
        return False

class Grafo():
    def __init__(self,  dirigido = True):
        self.__ListaNodos = []
        self.__ListaAristas = []
        self.dirigido = dirigido
        self.CurLabel = 0 #Le asignaremos len(self.getListaNodos()) cuando esta no sea vacía
    def getListaNodos(self):
        return self.__ListaNodos
    def AgregarNodo(self, nodo):
        self.__ListaNodos.append(nodo)
    def CrearArista(self, origen, destino):#append al revés en no dirigidos
        self.__ListaAristas.append(Arista(origen,destino))
        if self.dirigido == False:
            self.__ListaAristas.append(Arista(destino,origen))
        return Arista(origen,destino)
    def getListaAristas(self):
        return self.__ListaAristas
    def EncontrarIndiceArista(self,arista):
        for i in range(len(self.__ListaAristas)):
            if self.__ListaAristas[i].AristasIguales(arista):
                return i
    def getPesoArista(self,arista,ListaPesos):
        i = self.EncontrarIndiceArista(arista)
        return ListaPesos[i]
    def ExisteArista(self,X):
        for i in self.__ListaAristas:
            if i.GetDestino() not in X and i.GetOrigen() in X:
                return True
        return False
    def Distancia(self,inicio,fin,ListaPesos): # d(v) = suma pesos aristas camino más corto de nodo inicio a nodo fin.
        AristasCamino = []
        NodosCamino=[inicio]
        distancia = 0
        for i in range(len(self.CaminoMasCorto(inicio))): #del camino más corto total, cogmeos los nodos hasta el que nos interesa
            while self.CaminoMasCorto(inicio)[i] != fin:
                NodosCamino.append(self.CaminoMasCorto(inicio)[i])
        NodosCamino.append(fin)
        print('Los nodos del camino son: ' + str(NodosCamino))
        for i in range(len(NodosCamino)-1): #Creamos la lista de las aristas de este camino
            AristasCamino.append(Arista(NodosCamino[i],NodosCamino[i+1]))
            i += 1
        print('Las aristas del camino son: ' + str(AristasCamino))
        for i in AristasCamino:#Sumamos sus pesos a la distancia.
            distancia += self.getPesoArista(i,ListaPesos)
            print(self.getPesoArista(i,ListaPesos))
        fin.distancia = distancia #asignamos el valor distancia al atributo distancia del nodo
        return distancia

    def Dijkstra(self,NodoActual,ListaPesos):#Entrada:grafo, nodo, pesos aristas. Salida: para cada nodo, su distancia desde s a él.
        X = [NodoActual]
        NodoActual.distancia = 0
        print(self.ExisteArista(X))
        while self.ExisteArista(X) == True:
            peso = 1000000000 #infinito inicialmente
            for i in NodoActual.ListaAristas:
                if peso > self.getPesoArista(i,ListaPesos) + i.GetOrigen().distancia:
                    peso = self.getPesoArista(i,ListaPesos)
                    X.append(i.GetDestino())
                    i.GetDestino().distancia = self.Distancia(NodoActual, i.GetOrigen(),ListaPesos) + i.getPesoArista()
                    NodoActual = i.GetDestino
                    self.Dijkstra(NodoActual,ListaPesos)
            for i in range(len(self.__ListaNodos)):
                distancias.append(self.__ListaNodos[i].distancia)
            return distancias

#inicialmente para NO DIRIGIDOS
    def CaminoMasCorto(self, nodo): #Salida: los nodos marcados como explorados son accesibles desde nodo
        nodo.explorado = True
        nodo.nivel = 0 #El nodo que inicia el camino está en el nivel 0
        camino = [] #nodos accesibles desde nodo
        Q = [] #Cola: Metemos elementos en el final, los sacamos por el principio.
        Q.append(nodo)
        while Q != []:
            camino.append(Q[0]) #Añadimos el nodo que tratamos
            aux = Q[0] #guardamos su valor
            Q.pop(0)#quitar primer elemento de la cola
            for i in aux.ListaAristas: #para cada elemento en la lista de aristas del nodo tratado
                if i.GetDestino().explorado == False: #si el nodo destino de la arista no es explorado
                    i.GetDestino().explorado = True #lo marcamos como explorado
                    i.GetDestino().nivel = aux.nivel + 1 #fórmula del nivel
                    Q.append(i.GetDestino()) #lo añadimos a la cola
        camino.remove(nodo) #quitamos el nodo inicial de la lista de nodos accesibles
        return camino #Lista de nodos accesibles desde el nodo


print('------------------------------ EJEMPLO DIJKSTRA ----------------------------')

a = Nodo('a')
b = Nodo('b')
c = Nodo('c')
d = Nodo('d')
#e = Nodo('e')
#f = Nodo('f')
#g = Nodo('g')
#h = Nodo('h')

D = Grafo(False)

D.AgregarNodo(a)
D.AgregarNodo(b)
D.AgregarNodo(c)
D.AgregarNodo(d)
#D.AgregarNodo(e)
#D.AgregarNodo(f)
#D.AgregarNodo(g)
#D.AgregarNodo(h)
print('La lista de nodos es: ' + str(D.getListaNodos()))

#Añadimos las Aristas
ab = D.CrearArista(a,b)
ac =D.CrearArista(a,c)
ad = D.CrearArista(a,d)
bc = D.CrearArista(b,c)
#D.CrearArista(b,f)
#D.CrearArista(b,g)
cd = D.CrearArista(c,d)
#D.CrearArista(c,f)
#D.CrearArista(c,e)
#D.CrearArista(d,e)
#D.CrearArista(e,f)
#D.CrearArista(e,h)
#D.CrearArista(f,g)
#D.CrearArista(f,h)
#D.CrearArista(g,h)

print('La lista de aristas es: ' + str(D.getListaAristas()))

a.AgregarAristaNodo(D.getListaAristas()[0])
a.AgregarAristaNodo(D.getListaAristas()[2])
a.AgregarAristaNodo(D.getListaAristas()[4])
print('la lista de aristas de a es: ' + str(a.getListaAristasNodo()))
b.AgregarAristaNodo(D.getListaAristas()[1])
b.AgregarAristaNodo(D.getListaAristas()[6])
b.AgregarAristaNodo(D.getListaAristas()[8])
#b.AgregarAristaNodo(D.getListaAristas()[10])
print('la lista de aristas de b es: ' + str(b.getListaAristasNodo()))

c.AgregarAristaNodo(D.getListaAristas()[3])
c.AgregarAristaNodo(D.getListaAristas()[7])
#c.AgregarAristaNodo(D.getListaAristas()[12])
#c.AgregarAristaNodo(D.getListaAristas()[14])
#c.AgregarAristaNodo(D.getListaAristas()[16])
#c.AgregarAristaNodo(D.getListaAristas()[3])
print('la lista de aristas de c es: ' + str(c.getListaAristasNodo()))

d.AgregarAristaNodo(D.getListaAristas()[5])
#d.AgregarAristaNodo(D.getListaAristas()[13])
#d.AgregarAristaNodo(D.getListaAristas()[18])
print('la lista de aristas de d es: ' + str(d.getListaAristasNodo()))
'''
e.AgregarAristaNodo(D.getListaAristas()[17])
e.AgregarAristaNodo(D.getListaAristas()[19])
e.AgregarAristaNodo(D.getListaAristas()[20])
e.AgregarAristaNodo(D.getListaAristas()[22])
print('la lista de aristas de e es: ' + str(e.getListaAristasNodo()))

f.AgregarAristaNodo(D.getListaAristas()[9])
f.AgregarAristaNodo(D.getListaAristas()[15])
f.AgregarAristaNodo(D.getListaAristas()[21])
f.AgregarAristaNodo(D.getListaAristas()[24])
print('la lista de aristas de f es: ' + str(f.getListaAristasNodo()))

g.AgregarAristaNodo(D.getListaAristas()[11])
g.AgregarAristaNodo(D.getListaAristas()[25])
g.AgregarAristaNodo(D.getListaAristas()[28])
print('la lista de aristas de g es: ' + str(g.getListaAristasNodo()))

h.AgregarAristaNodo(D.getListaAristas()[23])
h.AgregarAristaNodo(D.getListaAristas()[27])
h.AgregarAristaNodo(D.getListaAristas()[29])
print('la lista de aristas de h es: ' + str(h.getListaAristasNodo()))
'''
aux5 = D.CaminoMasCorto(a)
niveles = []
for i in aux5:
    niveles.append(i.nivel)

#ListaPesos = [16,16,10,10,5,5,2,2,4,4,6,6,4,4,12,12,10,10,15,15,3,3,5,5,8,8,16,16,7,7]
ListaPesos = [16,16,10,10,5,5,2,2,4,4]
print('Los pesos de las aristas de D son: ' + str(ListaPesos))
print('Los nodos accesibles desde a son: ' + str(aux5) + ' en los niveles: ' + str(niveles))


print(D.EncontrarIndiceArista(ac))
print(D.getPesoArista(ac,ListaPesos))
print(D.Distancia(a,c,ListaPesos))
print(D.Dijkstra(a,ListaPesos))













