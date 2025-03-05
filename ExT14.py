
# Dado un grado no dirigido, conexo y con pesos en las
# aristas, determinar el conjunto de aristas que mantiene el
# grafo conexo minimizando la suma de los pesos de las
# aristas
#Entrada: Grafo no dirigido conexo G=(V,E) y el peso c_e para cada e\in E
#Salida: Un árbol de recubrimento T\subset E de G que minimiza sum_{e\in T} c_e

#Copiar y pegar del tema 10.
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
    def AristasDeXaVmenosX(self,X):
        aristas = []
        VmenosX = self.__ListaNodos.copy()
        aux = self.__ListaNodos.copy()
        for nodo in aux:
            if nodo in X:
                VmenosX.remove(nodo)
        for arista in self.__ListaAristas:
            if arista.GetOrigen() in X and arista.GetDestino() in VmenosX:
                aristas.append(arista)
        return aristas
    def minArista(self,aristas):
        min = 10000000000000000000  # infinito
        arista = None
        for a in aristas:
            if a.peso < min:
                arista = a
                min = a.peso
        return arista
    def ordenarAristas(self):
        aux = self.__ListaAristas.copy()
        L = []
        while len(aux) != 0:
            arista = self.minArista(aux)
            L.append(arista)
            aux.remove(arista)
        return L

    def Kruskal(self):
        T = [] #lista aristas
        U = UnionFind() #hacer diccionario
        U.Initialize(self.__ListaNodos)
        L = self.ordenarAristas()
        i = 0
        while len(T) < len(self.__ListaAristas)-1 and i < len(L):
            arista = L[i]
            origen = arista.GetOrigen()
            destino = arista.GetDestino()
            if U.Find(origen) != U.Find(destino):
                T.append(arista)
                U.Union(origen,destino)
            i += 1
        return T


    def Prim(self,s): #s nodo arbitrario
        s.explorado = True
        X = [s]#explorados
        T = [] #Lista aristas
        aristas = self.AristasDeXaVmenosX(X)
        while aristas != []:
            arista = self.minArista(aristas)
            arista.GetDestino().explorado = True
            X.append(arista.GetDestino())
            T.append(arista)
            aristas = self.AristasDeXaVmenosX(X)
        return T


class UnionFind():
    def __init__(self):
        self.representante = {}
    def Initialize(self,array):
        for i in array:
            self.representante[i] = i
    def Find(self,clave):
        #caso base
        if self.representante[clave] == clave:
            return clave
        #recursividad
        else: #si el padre no es él mismo
            return(self.Find(self.representante[clave]))
    def Union(self,x,y):
        self.representante[y]=x

#Ejemplo diapositivas Algoritmo de Prim
a = Nodo('a')
b = Nodo('b')
c = Nodo('c')
d = Nodo('d')

G = Grafo(False)

G.AgregarNodo(a)
G.AgregarNodo(b)
G.AgregarNodo(c)
G.AgregarNodo(d)

print('La lista de nodos es: ' + str(G.getListaNodos()))

ab = G.CrearArista(a,b,1)
ac = G.CrearArista(a,c,4)
ad = G.CrearArista(a,d,3)
bd = G.CrearArista(b,d,2)
cd = G.CrearArista(c,d,5)

print('La lista de aristas es: ' + str(G.getListaAristas()))

print('Prim de G con b: ', G.Prim(b))
print('Kruskal de G: ', G.Kruskal())



#Ejemplo diapositivas Algoritmo de Kruskal
e = Nodo('e')
f = Nodo('f')
g = Nodo('g')
h = Nodo('h')
i = Nodo('i')

D = Grafo(False)

D.AgregarNodo(e)
D.AgregarNodo(f)
D.AgregarNodo(g)
D.AgregarNodo(h)
D.AgregarNodo(i)

print('La lista de nodos es: ' + str(D.getListaNodos()))

D.CrearArista(e,f,4)
D.CrearArista(f,g,1)
D.CrearArista(g,h,7)
D.CrearArista(h,i,6)
D.CrearArista(e,i,2)
D.CrearArista(i,f,3)
D.CrearArista(f,h,5)

print('La lista de aristas es: ' + str(D.getListaAristas()))
print('Prim de D con e: ', D.Prim(e) )
print('Kruskal de D: ', D.Kruskal())
