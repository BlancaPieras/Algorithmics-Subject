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
    def __repr__(self):
        return self.__nombre #el representante de un elemento de la clase nodo es su nombre
    def AgregarAristaNodo(self,arista):
        self.ListaAristas.append(arista)
    def getListaAristasNodo(self): #lista de aristas que salen de un nodo
        return self.__ListaAristas

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
    def CrearArista(self, origen, destino):
        self.__ListaAristas.append(Arista(origen,destino))
    def getListaAristas(self):
        return self.__ListaAristas
#eSTÁ MAL. FALTA AÑADIR LAS ARISTAS COMPLEMENTARIAS. MIRAR OPCIONALES
    def CaminoMasCorto(self, nodo): #Salida: los nodos marcados como explorados son accesibles desde nodo
        #poner todos los nodos de explorado en false al principio
        if self.dirigido == False:
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

        else:
            return str('El grafo es dirigido.')


    def DFSTopo(self, s):
        s.explorado = True
        for arista in s.ListaAristas:
            if arista.GetDestino().explorado == False: #si el nodo destino de la arista es no explorado
                self.DFSTopo(arista.GetDestino()) #aplicamos recursividad
        s.FdeNodo = self.CurLabel #f(s) = nº nodos por colocar
        self.CurLabel -= 1 #queda uno menos por colocar

    def OrigenTopologico(self): #Salida: f-valores de los nodos
        self.CurLabel = len(self.__ListaNodos)-1  #número de nodos por colocar
        fvalores = [] #lista de los fvalores de los nodos
        if self.dirigido == True:
            for v in self.__ListaNodos:
                if v.explorado == False:
                    self.DFSTopo(v)
                fvalores.append(v.FdeNodo) #añadimos el valor f(nodo) a la lista de fvalores
            return fvalores
        else:
            return str('El grafo no es dirigido.')

print('--------------------------------------PROGRAMA PRINCIPAL-----------------------------------')

#PRUEBA CON GRAFO DIRIGIDO
print('-------------GRAFO DIRIGIDO---------------')
#Definimos los nodos
s = Nodo('s')
v = Nodo('v')
w = Nodo('w')
t = Nodo('t')

#Creamos un grafo dirigido:
g = Grafo(True)

#Añadimos los nodos
g.AgregarNodo(s)
g.AgregarNodo(v)
g.AgregarNodo(w)
g.AgregarNodo(t)
print('La lista de nodos es: ' + str(g.getListaNodos()))

#Añadimos las Aristas
g.CrearArista(s,v)
g.CrearArista(s,w)
g.CrearArista(v,t)
g.CrearArista(w,t)
print('La lista de aristas es: ' + str(g.getListaAristas()))
#Añadimos a cada nodo sus aristas salientes:
s.AgregarAristaNodo(g.getListaAristas()[0])
s.AgregarAristaNodo(g.getListaAristas()[1])
print('La lista de aristas de s es: '+ str(s.ListaAristas))
v.AgregarAristaNodo(g.getListaAristas()[2])
print('La lista de aristas de v es: '+ str(v.ListaAristas))
w.AgregarAristaNodo(g.getListaAristas()[3])
print('La lista de aristas de w es: '+ str(w.ListaAristas))
print('La lista de aristas de t es: '+ str(t.ListaAristas))


print('La ordenación topológica de los nodos ' +str(g.getListaNodos()) + ' es: ' + str(g.OrigenTopologico()))

#PRUEBA CON GRAFO NO DIRIGIDO
print('-----------------GRAFO NO DIRIGIDO--------------')
#Definimos los nodos
a = Nodo('a')
b = Nodo('b')
c = Nodo('c')
d = Nodo('d')
#Creamos un grafo no dirigido:
G = Grafo(False)

#Añadimos los nodos
G.AgregarNodo(a)
G.AgregarNodo(b)
G.AgregarNodo(c)
G.AgregarNodo(d)
print('La lista de nodos es: ' + str(G.getListaNodos()))

#Añadimos las Aristas
G.CrearArista(a,b)
G.CrearArista(b,d)
G.CrearArista(a,c)
G.CrearArista(c,d)
print('La lista de aristas es: ' + str(G.getListaAristas()))
#Añadimos a cada nodo sus aristas salientes:
a.AgregarAristaNodo(G.getListaAristas()[0])
a.AgregarAristaNodo(G.getListaAristas()[2])
print('La lista de aristas de a es: '+ str(a.ListaAristas))
b.AgregarAristaNodo(G.getListaAristas()[1])
print('La lista de aristas de b es: '+ str(b.ListaAristas))
c.AgregarAristaNodo(G.getListaAristas()[3])
print('La lista de aristas de c es: '+ str(c.ListaAristas))
print('La lista de aristas de d es: '+ str(d.ListaAristas))

aux = G.CaminoMasCorto(a)
niveles = []
for i in aux:
    niveles.append(i.nivel)

print('Los nodos accesibles desde a son: ' + str(aux) + ' en los niveles: ' + str(niveles))






