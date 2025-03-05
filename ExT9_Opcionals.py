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
    def GetOrigen(self):
        return self.__origen

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
    def getListaAristas(self):
        return self.__ListaAristas
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

    def DFSTopo(self, s):
        s.explorado = True
        for arista in s.ListaAristas:
            if arista.GetDestino().explorado == False: #si el nodo destino de la arista es no explorado
                self.DFSTopo(arista.GetDestino()) #aplicamos recursividad
        s.FdeNodo = self.CurLabel #f(s) = nº nodos por colocar
        self.CurLabel -= 1 #queda uno menos por colocar
#Inicialmente para GRAFOS DIRIGIDOS
    def OrigenTopologico(self): #Salida: f-valores de los nodos
        if self.dirigido == True or len(self.__ListaAristas) == 0:
            for i in self.__ListaNodos:
                i.explorado = False
            self.CurLabel = len(self.__ListaNodos)-1  #número de nodos por colocar
            fvalores = [] #lista de los fvalores de los nodos
            for v in self.__ListaNodos:
                if v.explorado == False:
                    self.DFSTopo(v)
                fvalores.append(v.FdeNodo)  # añadimos el valor f(nodo) a la lista de fvalores
            return fvalores
        else:
            return ('El grafo no es dirigido y tiene ' + str(len(self.__ListaAristas)) + ' aristas \n-> No '
            'podemos realizar la ordenación topológica ya que para cada arista se da a la vez lo siguiente:\n'
            'f(nodo_orígen)<f(nodo_destino) y f(nodo_destino)<f(nodo_origen). CONTRADICCIÓN!' )



'''
NOTAS SOBRE LOS CAMBIOS RESPECTO AL EJERCICIO OBLIGATORIO:

------------- CAMINO MÁS CORTO ----------

En este método, simplemente hemos eliminado la condición de que el grafo sea no dirigido para aplicarlo.


------------- ORDENACIÓN TOPOLÓGICA -----

- Hemos eliminado la condición de que el grafo sea dirigido.
- El único caso en el que funciona el método para grafos no dirigidos es si no existen aristas en el grafo. 
- Además, como en el programa principal aplicamos primero CaminoMasCorto, antes de comenzar, redefinimos todos 
    los valores explorado de los nodos como False.

'''

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

aux = g.CaminoMasCorto(s)
niveles = []
for i in aux:
    niveles.append(i.nivel)

print('Los nodos accesibles desde s son: ' + str(aux) + ' en los niveles: ' + str(niveles))

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
a.AgregarAristaNodo(G.getListaAristas()[1])
a.AgregarAristaNodo(G.getListaAristas()[4])
a.AgregarAristaNodo(G.getListaAristas()[5])
print('La lista de aristas de a es: '+ str(a.ListaAristas))
b.AgregarAristaNodo(G.getListaAristas()[0])
b.AgregarAristaNodo(G.getListaAristas()[1])
b.AgregarAristaNodo(G.getListaAristas()[2])
b.AgregarAristaNodo(G.getListaAristas()[3])
print('La lista de aristas de b es: '+ str(b.ListaAristas))
c.AgregarAristaNodo(G.getListaAristas()[4])
c.AgregarAristaNodo(G.getListaAristas()[5])
c.AgregarAristaNodo(G.getListaAristas()[6])
c.AgregarAristaNodo(G.getListaAristas()[7])
print('La lista de aristas de c es: '+ str(c.ListaAristas))
d.AgregarAristaNodo(G.getListaAristas()[6])
d.AgregarAristaNodo(G.getListaAristas()[7])

print('La lista de aristas de d es: '+ str(d.ListaAristas))

aux2 = G.CaminoMasCorto(a)
niveles = []
for i in aux2:
    niveles.append(i.nivel)

print('Los nodos accesibles desde a son: ' + str(aux2) + ' en los niveles: ' + str(niveles))
print('La ordenación topológica de los nodos ' +str(G.getListaNodos()) + ' es: ' + str(G.OrigenTopologico()))

#EJEMPLO DIAPOSITIVA 23 TEMA 9.
print('---------------------------- OTRO EJEMPLO NO DIRIGIDO ------------------------')

#Definimos los nodos
s = Nodo('s')
a = Nodo('a')
b = Nodo('b')
c = Nodo('c')
d = Nodo('d')
e = Nodo('e')

#Creamos un grafo no dirigido:
HolaCaracola = Grafo(False)

#Añadimos los nodos
HolaCaracola.AgregarNodo(s)
HolaCaracola.AgregarNodo(a)
HolaCaracola.AgregarNodo(b)
HolaCaracola.AgregarNodo(c)
HolaCaracola.AgregarNodo(d)
HolaCaracola.AgregarNodo(e)
print('La lista de nodos es: ' + str(HolaCaracola.getListaNodos()))

#Añadimos las Aristas
HolaCaracola.CrearArista(s,a)
HolaCaracola.CrearArista(s,b)
HolaCaracola.CrearArista(a,c)
HolaCaracola.CrearArista(b,c)
HolaCaracola.CrearArista(b,d)
HolaCaracola.CrearArista(c,e)
HolaCaracola.CrearArista(c,d)
HolaCaracola.CrearArista(e,d)
print('La lista de aristas es: ' + str(HolaCaracola.getListaAristas()))

#Añadimos a cada nodo sus aristas salientes:
s.AgregarAristaNodo(HolaCaracola.getListaAristas()[0])
s.AgregarAristaNodo(HolaCaracola.getListaAristas()[1])
s.AgregarAristaNodo(HolaCaracola.getListaAristas()[2])
s.AgregarAristaNodo(HolaCaracola.getListaAristas()[3])
print('La lista de aristas de s es: '+ str(s.ListaAristas))

a.AgregarAristaNodo(HolaCaracola.getListaAristas()[0])
a.AgregarAristaNodo(HolaCaracola.getListaAristas()[1])
a.AgregarAristaNodo(HolaCaracola.getListaAristas()[4])
a.AgregarAristaNodo(HolaCaracola.getListaAristas()[5])

print('La lista de aristas de a es: '+ str(a.ListaAristas))


b.AgregarAristaNodo(HolaCaracola.getListaAristas()[2])
b.AgregarAristaNodo(HolaCaracola.getListaAristas()[3])
b.AgregarAristaNodo(HolaCaracola.getListaAristas()[6])
b.AgregarAristaNodo(HolaCaracola.getListaAristas()[7])
b.AgregarAristaNodo(HolaCaracola.getListaAristas()[8])
b.AgregarAristaNodo(HolaCaracola.getListaAristas()[9])


print('La lista de aristas de b es: '+ str(b.ListaAristas))

c.AgregarAristaNodo(HolaCaracola.getListaAristas()[4])
c.AgregarAristaNodo(HolaCaracola.getListaAristas()[5])
c.AgregarAristaNodo(HolaCaracola.getListaAristas()[6])
c.AgregarAristaNodo(HolaCaracola.getListaAristas()[7])
c.AgregarAristaNodo(HolaCaracola.getListaAristas()[10])
c.AgregarAristaNodo(HolaCaracola.getListaAristas()[11])
c.AgregarAristaNodo(HolaCaracola.getListaAristas()[12])
c.AgregarAristaNodo(HolaCaracola.getListaAristas()[13])

print('La lista de aristas de c es: '+ str(c.ListaAristas))

d.AgregarAristaNodo(HolaCaracola.getListaAristas()[8])
d.AgregarAristaNodo(HolaCaracola.getListaAristas()[9])
d.AgregarAristaNodo(HolaCaracola.getListaAristas()[12])
d.AgregarAristaNodo(HolaCaracola.getListaAristas()[13])
d.AgregarAristaNodo(HolaCaracola.getListaAristas()[14])
d.AgregarAristaNodo(HolaCaracola.getListaAristas()[15])

print('La lista de aristas de d es: '+ str(d.ListaAristas))

e.AgregarAristaNodo(HolaCaracola.getListaAristas()[10])
e.AgregarAristaNodo(HolaCaracola.getListaAristas()[11])
e.AgregarAristaNodo(HolaCaracola.getListaAristas()[14])
e.AgregarAristaNodo(HolaCaracola.getListaAristas()[15])


print('La lista de aristas de e es: '+ str(e.ListaAristas))

aux3 = HolaCaracola.CaminoMasCorto(s)
niveles = []
for i in aux3:
    niveles.append(i.nivel)

print('Los nodos accesibles desde s son: ' + str(aux3) + ' en los niveles: ' + str(niveles))
print('La ordenación topológica de los nodos ' +str(HolaCaracola.getListaNodos()) + ' es: ' + str(HolaCaracola.OrigenTopologico()))



print('---------------------------- OTRO EJEMPLO DIRIGIDO ------------------------')

#Definimos los nodos
s = Nodo('s')
a = Nodo('a')
b = Nodo('b')
c = Nodo('c')
d = Nodo('d')
e = Nodo('e')

#Creamos un grafo no dirigido:
HolaCaracola2 = Grafo(True)

#Añadimos los nodos
HolaCaracola2.AgregarNodo(s)
HolaCaracola2.AgregarNodo(a)
HolaCaracola2.AgregarNodo(b)
HolaCaracola2.AgregarNodo(c)
HolaCaracola2.AgregarNodo(d)
HolaCaracola2.AgregarNodo(e)
print('La lista de nodos es: ' + str(HolaCaracola2.getListaNodos()))

#Añadimos las Aristas
HolaCaracola2.CrearArista(s,a)
HolaCaracola2.CrearArista(s,b)
HolaCaracola2.CrearArista(a,c)
HolaCaracola2.CrearArista(b,c)
HolaCaracola2.CrearArista(b,d)
HolaCaracola2.CrearArista(c,e)
HolaCaracola2.CrearArista(c,d)
HolaCaracola2.CrearArista(e,d)
print('La lista de aristas es: ' + str(HolaCaracola2.getListaAristas()))

#Añadimos a cada nodo sus aristas salientes:
s.AgregarAristaNodo(HolaCaracola2.getListaAristas()[0])
s.AgregarAristaNodo(HolaCaracola2.getListaAristas()[1])

print('La lista de aristas de s es: '+ str(s.ListaAristas))


a.AgregarAristaNodo(HolaCaracola2.getListaAristas()[2])


print('La lista de aristas de a es: '+ str(a.ListaAristas))


b.AgregarAristaNodo(HolaCaracola2.getListaAristas()[3])
b.AgregarAristaNodo(HolaCaracola2.getListaAristas()[4])



print('La lista de aristas de b es: '+ str(b.ListaAristas))


c.AgregarAristaNodo(HolaCaracola2.getListaAristas()[5])
c.AgregarAristaNodo(HolaCaracola2.getListaAristas()[6])

print('La lista de aristas de c es: '+ str(c.ListaAristas))


print('La lista de aristas de d es: '+ str(d.ListaAristas))

e.AgregarAristaNodo(HolaCaracola2.getListaAristas()[7])

print('La lista de aristas de e es: '+ str(e.ListaAristas))

aux4 = HolaCaracola2.CaminoMasCorto(a)
niveles = []
for i in aux4:
    niveles.append(i.nivel)

print('Los nodos accesibles desde a son: ' + str(aux4) + ' en los niveles: ' + str(niveles))
print('La ordenación topológica de los nodos ' +str(HolaCaracola2.getListaNodos()) + ' es: ' + str(HolaCaracola2.OrigenTopologico()))

print('------------------ EJEMPLO DE GRAFO NO DIRIGIDO SIN ARISTAS ------------------------')

s = Nodo('s')
UnNodo = Grafo(False)
UnNodo.AgregarNodo(s)
print('La lista de nodos es: ' + str(UnNodo.getListaNodos()))
print('La lista de aristas es: ' + str(UnNodo.getListaAristas()))
print('La lista de aristas de s es: '+ str(s.ListaAristas))
print('La ordenación topológica de los nodos ' +str(UnNodo.getListaNodos()) + ' es: ' + str(UnNodo.OrigenTopologico()))
#Como vemos, en este caso no se da la contradicción del ejemplo 3.