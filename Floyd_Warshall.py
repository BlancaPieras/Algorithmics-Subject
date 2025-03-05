#Maria Coll Gelabert
#Bellman-Ford
class Nodo:
    def __init__(self, nombre = ''):
        self.__nombre = nombre
        self.__aristas = []
        self.camino_arista = []

    def afegir_arista(self, arista):
        self.__aristas.append(arista)

    def get_aristas(self):
        return self.__aristas

    def get_name(self):
        return self.__nombre

class Arista:
    def __repr__(self):
        return str(self.__identificador)
    __numaristas = 0
    def __init__(self, inicio, fin, peso):
        self.__identificador = Arista.__numaristas
        self.__inicio = inicio
        self.__fin = fin
        self.__peso = peso
        Arista.__numaristas += 1

    def get_identificador(self):
        return self.__identificador

    def get_inicio(self):
        return self.__inicio

    def get_fin(self):
        return self.__fin

    def get_peso(self):
        return self.__peso

class Grafo:
    def __init__(self, dirigido = False):
        self.__dirigido = dirigido
        self.__listanodos = []
        self.__listaaristas = []

    def crear_nodo(self, nombre):
        nodo = Nodo(nombre)
        self.__listanodos.append(nodo)

    def get_nodo(self, name):
        for n in self.__listanodos:
            if n.get_name() == name:
                return n

    def get_listaristas(self):
        return self.__listaaristas

    def crear_arista( self,ini, fin, peso):
        arista = Arista(ini, fin, peso)
        self.__listaaristas.append(arista)
        for i in self.__listanodos:
            if i == ini:
                i.afegir_arista(arista)
            elif i == fin:
                i.afegir_arista(arista) #No podemos tener aristas de ellas a ellas mismas
    def get_arista_peso(self, indice1, indice2):
        nodo1 = self.__listanodos[indice1]
        nodo2 = self.__listanodos[indice2]
        for i in self.__listaaristas:
            if i.get_fin()== nodo1 and i.get_inicio()==nodo2:
                return i.get_peso()
            # Nos interesa solo una dirección al tratarse de dirigidos
            elif i.get_fin()== nodo2 and i.get_inicio()==nodo1 and self.__dirigido== False:
                return i.get_peso()
        return float('inf')
    def get_arista(self, indice1, indice2):
        nodo1 = self.__listanodos[indice1]
        nodo2 = self.__listanodos[indice2]
        for i in self.__listaaristas:
            if i.get_fin()== nodo1 and i.get_inicio()==nodo2 :
                return i
            #Nos interesa solo ida al tratarse de dirigidos
            elif i.get_fin()== nodo1 and i.get_inicio()==nodo2 and self.__dirigido== False:
                return i
        return None

    def bellman_ford(self):
        n = len(self.__listanodos)
        A= [[float('inf')]*(n) for _ in range(0,n+1)] #Matriz bidimensional
        A[0][0] = 0
        for i in range (1, n+1):
            avanzado = False
            for ind_v in range(0,len(self.__listanodos)):
                minimo = A[i-1][ind_v]
                for ind_w in range(0,len(self.__listanodos)):
                    if A[i - 1][ind_w] + self.get_arista_peso(ind_v, ind_w) < minimo:
                        minimo = A[i-1][ind_w] + self.get_arista_peso(ind_v, ind_w)
                A[i][ind_v]=minimo
                if A[i][ind_v] != A[i-1][ind_v]:
                    avanzado = True
            if not avanzado:
                return A[i-1]
        return None

    def floyd_warshall(self):
        n = len(self.__listanodos)
        # A = [[[float('inf')]*(n+1) for _ in range(0,n+1)] for _ in range(0,n+1)] # Matriz tridimensional
        A = [[[float('inf')]*(n) for _ in range(0,n)] for _ in range(0,n+1)] # Matriz tridimensional
        #caso base
        for v in range(0,n):
            for w in range(0,n):
                if v==w:
                    A[0][v][w] = 0
                elif self.get_arista(v,w) != None:
                    A[0][v][w]= self.get_arista_peso(v,w)
                else:
                    A[0][v][w]= float('inf')
        for i in range(0,n+1):
            print(A[i])
        for k in range(1, n+1):
            for v in range(0,n):
                for w in range(0,n):
                    print (k, v, w)
                    A[k][v][w]= min(A[k-1][v][w],A[k-1][v][k-1]+A[k-1][k-1][w])
        #comprobación ciclos negativos
        for v in range(0,n):
            if A[n][v][v] < 0:
                return None
        return A[n]


#Pruebas
grafo1 = Grafo(True)
Nodos = ['S','V','W','U','T']
for i in Nodos:
    grafo1.crear_nodo(i)
grafo1.crear_arista(grafo1.get_nodo('S'),grafo1.get_nodo('V'), 4) #ARISTA 0
grafo1.crear_arista(grafo1.get_nodo('V'), grafo1.get_nodo('T'),4) #ARISTA 1
grafo1.crear_arista(grafo1.get_nodo('S'), grafo1.get_nodo('U'),2) #ARISTA 2
grafo1.crear_arista(grafo1.get_nodo('U'), grafo1.get_nodo('W'),2) #ARISTA 3
grafo1.crear_arista(grafo1.get_nodo('W'), grafo1.get_nodo('T'),2) #ARISTA 4
grafo1.crear_arista(grafo1.get_nodo('U'), grafo1.get_nodo('V'),-1) #ARISTA 5
BellmanFord = grafo1.bellman_ford()
print(BellmanFord)

grafo2 = Grafo(True)
Nodos = ['P','Q','S','R','T']
for i in Nodos:
    grafo2.crear_nodo(i)
grafo2.crear_arista(grafo2.get_nodo('P'),grafo2.get_nodo('Q'), 2) #ARISTA 6
grafo2.crear_arista(grafo2.get_nodo('Q'), grafo2.get_nodo('S'),2) #ARISTA 7
grafo2.crear_arista(grafo2.get_nodo('P'), grafo2.get_nodo('R'),4) #ARISTA 8
grafo2.crear_arista(grafo2.get_nodo('R'), grafo2.get_nodo('S'),4) #ARISTA 9
grafo2.crear_arista(grafo2.get_nodo('R'), grafo2.get_nodo('T'),3) #ARISTA 10
grafo2.crear_arista(grafo2.get_nodo('T'), grafo2.get_nodo('S'),-5) #ARISTA 11
Floyd = grafo2.floyd_warshall()
print(Floyd)