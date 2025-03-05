class Nodo():
    def __init__(self, nombre = ''):
        self.nombre = nombre
        self.ListaAristas = []
        self.camino = []
        self.indice = None
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
    def minArista(self,aristas,w,v):
        min = 10000000000000000000  # infinito
        arista = None
        for a in aristas:
            if a.peso < min:
                if a.GetDestino()==v and a.GetOrigen()==w:
                    arista = a
                    min = a.peso
        if arista != None:
            return arista.peso
        elif arista == None:
            return 100000000000000000


    def asignarindicesnodos(self):
        ind = 0
        for i in self.getListaNodos():
            i.indice = ind
            ind += 1
    def encontrarArista(self,w,v):
        arista = None
        for a in self.getListaAristas():
            if a.GetOrigen()==w and a.GetDestino()==v:
                arista = a
        return arista
    def FloydWarshal(self):
        n = len(self.getListaNodos())
        A = [[[float('inf')]*n for z in range(0,n)] for k in range(0,n+1)]
        #Caso base
        for v in range(0,n):
            for w in range(0,n):
                if v == w:
                    A[0][v][w] = 0
                elif self.encontrarArista(self.getListaNodos()[v],self.getListaNodos()[w]) != None:
                    A[0][v][w] = self.encontrarArista(self.getListaNodos()[v],self.getListaNodos()[w]).peso
                else:
                    A[0][v][w] = float('inf')
        #cálculo de los caminos
        for k in range(1,n+1):
            for v in range(0,n):
                for w in range(0,n):
                    A[k][v][w] = min(A[k-1][v][w], A[k-1][v][k-1] + A[k-1][k-1][w])
        #comprobación ciclos negativos
        for v in range(0,n):
            if A[n][v][v] < 0:
                return None
        return A[n]
    def BellmanFord(self):
        self.asignarindicesnodos()
        n = len(self.getListaNodos())
        A = [[float('inf')] * n for z in range(0, n+1)]
        A[0][self.getListaNodos()[0].indice] = 0
        for i in range(1, n+1):
            avanzado = False
            for v in self.getListaNodos():
                minimo = 100000000000000000000000
                for w in self.getListaNodos():
                    if A[i-1][w.indice] + self.minArista(self.getListaAristas(),w,v) < minimo:
                        minimo = A[i-1][w.indice] + self.minArista(self.getListaAristas(),w,v)
                A[i][v.indice] = min(A[i-1][v.indice], minimo)
                if A[i][v.indice] < A[i-1][v.indice]:
                    avanzado = True
            if avanzado == False:
                return A[i-1]
        return None #tenemos un ciclo infinito.

print('------------EJEMPLO DIAPOSITIVAS BELLMAN-FORD---------------')
s = Nodo('s')
t = Nodo('t')
u = Nodo('u')
v = Nodo('v')
w = Nodo('w')

D = Grafo(True)

D.AgregarNodo(s)
D.AgregarNodo(t)
D.AgregarNodo(u)
D.AgregarNodo(v)
D.AgregarNodo(w)

print('La lista de nodos es: ' + str(D.getListaNodos()))

D.CrearArista(s,v,4)
D.CrearArista(s,u,2)
D.CrearArista(v,t,4)
D.CrearArista(u,v,-1)
D.CrearArista(u,w,2)
D.CrearArista(w,t,2)

print('la lista de aristas es: ' + str(D.getListaAristas()))
print('Con pesos:')
for i in D.getListaAristas():
    print(i,'->',i.peso)

print('Bellman-Ford ->',D.BellmanFord())


print('FloydWarshal -> ',D.FloydWarshal())

print('------------EJEMPLO CIRCULAR---------------')
A = Nodo('A')
B = Nodo('B')
C = Nodo('C')
D = Nodo('D')
E = Nodo('E')

G = Grafo(True)

G.AgregarNodo(A)
G.AgregarNodo(B)
G.AgregarNodo(C)
G.AgregarNodo(D)
G.AgregarNodo(E)

print('La lista de nodos es: ' + str(G.getListaNodos()))

G.CrearArista(A,B,2)
G.CrearArista(B,C,1)
G.CrearArista(C,D,-2)
G.CrearArista(D,E,4)
G.CrearArista(E,A,-1)

print('la lista de aristas es: ' + str(G.getListaAristas()))
print('Con pesos:')
for i in G.getListaAristas():
    print(i,'->',i.peso)


print('FloydWarshal -> ',G.FloydWarshal())
