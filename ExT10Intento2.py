import abc
import random
import time
import numpy
import math

class Nodo():
    def __init__(self, nombre = ''):
        self.nombre = nombre
        self.ListaAristas = []
        self.camino = []
        self.distancia = 1000000 #infinito inicialmente
        self.nivel = 100000 #Valor que no se alcanza (infinito)
        self.explorado = False #Marcamos todos los nodos como no explorados inicialmente
        self.FdeNodo = None #f(nodo) inicialmente no tiene valor para la ordenación topológica
    def __repr__(self):
        return self.nombre #el representante de un elemento de la clase nodo es su nombre
    def AgregarAristaNodo(self,arista):
        self.ListaAristas.append(arista)
    def getListaAristasNodo(self): #lista de aristas que salen de un nodo
        return self.ListaAristas

class Arista():
    identificador = 0
    def __init__(self, origen, destino, peso):
        self.peso = peso
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
    def AristasIguales(self,arista): #si el nombre de dos aristas coincide, son iguales.
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
    def ExisteArista(self,X):
        for i in self.__ListaAristas:
            if i.GetDestino() not in X and i.GetOrigen() in X:
                return True
        return False
    def VisitadoANovisitado(self,X):
        VisitadoANovisitado = []
        for i in self.__ListaAristas:
            if i.GetDestino() not in X and i.GetOrigen() in X:
                VisitadoANovisitado.append(i)
        return VisitadoANovisitado

    def CrearArista(self, origen, destino, peso):#append al revés en no dirigidos
        self.__ListaAristas.append(Arista(origen,destino,peso))
        if self.dirigido == False:
            self.__ListaAristas.append(Arista(destino,origen,peso))
    def getListaPesos(self):
        ListaPesos = []
        for i in self.__ListaAristas:
            ListaPesos.append(i.peso)
    def getListaAristas(self):
        return self.__ListaAristas

    def Dijkstra(self,s):#Entrada:grafo, nodo. Salida: para cada nodo, su distancia desde s a él.
        X = [s] #inicializamos el conjunto de nodos visitados con s
        s.distancia = 0 #su distancia es 0
        for i in self.__ListaNodos:#marcamos la distancia de los nodos no visitados como infinito
            if i != s:
                i.distancia = 1000000
        while self.ExisteArista(X) == True: #Mientras haya una arista del conjunto de nodos visitados a no visitados
            minimo = 10000
            aristamin = None
            for arista in self.VisitadoANovisitado(X): #para cada arista de este conjunto
                x = arista.GetOrigen().distancia + arista.peso #definimos el valor de la distancia del nodo destino
                if minimo > x: #si este es menor que la distancia a otro nodo
                    aristamin = arista #la arista actual pasa a ser la minima
                    minimo = x #el valor minimo es esta distancia
            X.append(aristamin.GetDestino()) #añadimos el nodo destino de la arista al conjunto de visitados
            aristamin.GetDestino().distancia = aristamin.GetOrigen().distancia + aristamin.peso #definimos la distancia del nodo origen
        Distancias = [] #Creamos la lista de distancias para cada nodo
        for i in self.__ListaNodos:
            Distancias.append(i.distancia)
        return Distancias

    def Dijkstra2(self,s): #Salida: (nodo,distancia,camino)
        X = [s]
        Devolver = []
        s.distancia = 0
        for i in self.__ListaNodos:
            if i != s:
                i.distancia = 1000000
        while self.ExisteArista(X) == True:
            minimo = 10000
            aristamin = None
            for arista in self.VisitadoANovisitado(X):
                x = arista.GetOrigen().distancia + arista.peso
                if minimo > x:
                    aristamin = arista
                    minimo = x
            '''El camino hasta un nodo, es el camino del nodo anterior más la arista del nodo anterior a él.'''
            aristamin.GetDestino().camino = aristamin.GetOrigen().camino.copy()
            aristamin.GetDestino().camino.append(aristamin)
            X.append(aristamin.GetDestino())
            aristamin.GetDestino().distancia = aristamin.GetOrigen().distancia + aristamin.peso
        for i in self.__ListaNodos:
            Devolver.append((i.nombre, i.distancia, i.camino)) #devolvemos la tripleta (nombre,distancia,camino)
        return Devolver









print('------------------------------ EJEMPLO DIJKSTRA ----------------------------')

a = Nodo('a')
b = Nodo('b')
c = Nodo('c')
d = Nodo('d')
e = Nodo('e')
f = Nodo('f')
g = Nodo('g')
h = Nodo('h')

D = Grafo(False)

D.AgregarNodo(a)
D.AgregarNodo(b)
D.AgregarNodo(c)
D.AgregarNodo(d)
D.AgregarNodo(e)
D.AgregarNodo(f)
D.AgregarNodo(g)
D.AgregarNodo(h)
print('La lista de nodos es: ' + str(D.getListaNodos()))

#Añadimos las Aristas
ab = D.CrearArista(a,b,16)
ac =D.CrearArista(a,c,10)
ad = D.CrearArista(a,d,5)
bc = D.CrearArista(b,c,2)
D.CrearArista(b,f,4)
D.CrearArista(b,g,6)
cd = D.CrearArista(c,d,4)
D.CrearArista(c,f,12)
D.CrearArista(c,e,10)
D.CrearArista(d,e,15)
D.CrearArista(e,f,3)
D.CrearArista(e,h,5)
D.CrearArista(f,g,8)
D.CrearArista(f,h,16)
D.CrearArista(g,h,7)

print('La lista de aristas es: ' + str(D.getListaAristas()))

a.AgregarAristaNodo(D.getListaAristas()[0])
a.AgregarAristaNodo(D.getListaAristas()[2])
a.AgregarAristaNodo(D.getListaAristas()[4])
print('la lista de aristas de a es: ' + str(a.getListaAristasNodo()))
b.AgregarAristaNodo(D.getListaAristas()[1])
b.AgregarAristaNodo(D.getListaAristas()[6])
b.AgregarAristaNodo(D.getListaAristas()[8])
b.AgregarAristaNodo(D.getListaAristas()[10])
print('la lista de aristas de b es: ' + str(b.getListaAristasNodo()))

c.AgregarAristaNodo(D.getListaAristas()[3])
c.AgregarAristaNodo(D.getListaAristas()[7])
c.AgregarAristaNodo(D.getListaAristas()[12])
c.AgregarAristaNodo(D.getListaAristas()[14])
c.AgregarAristaNodo(D.getListaAristas()[16])
c.AgregarAristaNodo(D.getListaAristas()[3])
print('la lista de aristas de c es: ' + str(c.getListaAristasNodo()))

d.AgregarAristaNodo(D.getListaAristas()[5])
d.AgregarAristaNodo(D.getListaAristas()[13])
d.AgregarAristaNodo(D.getListaAristas()[18])
print('la lista de aristas de d es: ' + str(d.getListaAristasNodo()))

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

print('Los nodos ' + str(D.getListaNodos()) + 'tienen distancias ' + str(D.Dijkstra(a)))

print('Las tripletas (nodo, distancia, nombre) para cada nodo del grafo son: \n' + str(D.Dijkstra2(a)))

