import copy
from UnionFind import UnionFind
from Heap import Heap


class Nodo:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__aristas_salida = []
        self.__aristas_llegada = []

    def get_nombre(self):
        return self.__nombre

    def get_aristas_salida(self):
        return self.__aristas_salida

    def add_arista_salida(self, a):
        self.__aristas_salida.append(a)

    def get_aristas_llegada(self):
        return self.__aristas_llegada

    def add_arista_llegada(self, a):
        self.__aristas_llegada.append(a)

    def __repr__(self):
        return self.__nombre


class Arista:
    __next_id = 0

    def __init__(self, nodo_salida, nodo_llegada, peso):
        self.__nodo_salida = nodo_salida
        self.__nodo_llegada = nodo_llegada
        self.__peso = peso
        self.__id = Arista.__next_id
        Arista.__next_id += 1

    def get_salida(self):
        return self.__nodo_salida

    def get_llegada(self):
        return self.__nodo_llegada

    def get_peso(self):
        return self.__peso

    def __repr__(self):
        return str(self.__nodo_salida) + "-->" + str(self.__nodo_llegada)


class Grafo:
    def __init__(self, dirigido):
        self.__dirigido = dirigido
        self.__nodos = []
        self.__aristas = []

    def add_nodo(self, nombre):
        nuevo_nodo = Nodo(nombre)
        self.__nodos.append(nuevo_nodo)
        return nuevo_nodo

    def get_nodo_by_index(self, index):
        return self.__nodos[index]

    def add_arista(self, salida, llegada, peso=0):
        nodo_salida = self.get_nodo(salida)
        nodo_llegada = self.get_nodo(llegada)
        # arista en un sentido
        nueva_arista = Arista(nodo_salida, nodo_llegada, peso)
        self.__aristas.append(nueva_arista)
        nodo_salida.add_arista_salida(nueva_arista)
        nodo_llegada.add_arista_llegada(nueva_arista)
        # arista en el otro sentido si no es dirigido
        if self.__dirigido == False:
            nueva_arista = Arista(nodo_llegada, nodo_salida, peso)
            self.__aristas.append(nueva_arista)
            nodo_llegada.add_arista_salida(nueva_arista)
            nodo_salida.add_arista_llegada(nueva_arista)
        return nueva_arista

    def get_arista(self, salida, llegada):
        for a in salida.get_aristas_salida():
            if a.get_llegada() == llegada:
                return a
        return None

    def get_nodo(self, nombre):
        for n in self.__nodos:
            if n.get_nombre() == nombre:
                return n
        return None

    def get_index_nodo(self, nodo):
        for i in range(0, len(self.__nodos)):
            if self.__nodos[i] == nodo:
                return i
        return None

    def camino_mas_corto(self, nodo_fuente):
        MAX_VALUE = float('inf')
        resultado = []
        for n in self.__nodos:
            n.explorado = False
            n.distancia = MAX_VALUE
        nodo_fuente.explorado = True
        nodo_fuente.distancia = 0
        q = [nodo_fuente]
        while len(q) > 0:
            n = q.pop(0)
            aristas = n.get_aristas_salida()
            for a in aristas:
                nodo_llegada = a.get_llegada()
                if nodo_llegada.explorado == False:
                    nodo_llegada.explorado = True
                    nodo_llegada.distancia = a.get_salida().distancia + 1
                    q.append(nodo_llegada)

        resultado = []
        for n in self.__nodos:
            r = (n, n.distancia)
            resultado.append(r)
            # borramos los atribtos temporales creados
            del n.explorado
            del n.distancia
        return resultado

    def dijkstra(self, nodo_fuente):
        MAX_VALUE = float('inf')
        for n in self.__nodos:
            n.explorado = False
            n.distancia = MAX_VALUE
            n.previo = None
            n.camino = []
        nodo_fuente.explorado = True
        nodo_fuente.distancia = 0
        l = [nodo_fuente]
        menor_peso = 0
        while menor_peso >= 0:
            best_arista = None
            menor_peso = -1
            for n in l:
                for a in n.get_aristas_salida():
                    if a.get_llegada().explorado == False:
                        total = a.get_salida().distancia + a.get_peso()
                        if best_arista is None or total < menor_peso:
                            menor_peso = total
                            best_arista = a

            if best_arista is not None:
                origen = best_arista.get_salida()
                nuevo = best_arista.get_llegada()
                nuevo.explorado = True
                nuevo.distancia = menor_peso
                nuevo.previo = origen
                nuevo.camino = copy.copy(origen.camino)
                nuevo.camino.append(best_arista)
                l.append(nuevo)

        resultado = []
        for n in self.__nodos:
            r = (n, n.distancia, n.previo, n.camino)
            resultado.append(r)
            # borramos los atribtos temporales creados
            del n.explorado
            del n.distancia
            del n.previo
            del n.camino
        return resultado

    def dfs_topo(self, nodo):
        nodo.explorado = True
        for a in nodo.get_aristas_salida():
            n = a.get_llegada()
            if n.explorado == False:
                self.dfs_topo(n)
            elif n.orden == -1:
                raise Exception("Es un grafo cíclico")

        nodo.orden = self.cur_label
        self.cur_label -= 1

    def orden_topologico(self):
        for n in self.__nodos:
            n.explorado = False
            n.orden = -1

        self.cur_label = len(self.__nodos)
        for n in self.__nodos:
            if n.explorado == False:
                self.dfs_topo(n)

        resultado = []
        for n in self.__nodos:
            r = (n, n.orden)
            resultado.append(r)
            # borramos los atribtos temporales creados
            del n.explorado
            del n.orden
        del self.cur_label

        return resultado

    def prim(self):
        nodo_fuente = self.__nodos[0]
        MAX_VALUE = 999
        resultado = []
        for n in self.__nodos:
            n.explorado = False
        nodo_fuente.explorado = True
        l = [nodo_fuente]
        menor_peso = 0
        while menor_peso >= 0:
            best_arista = None
            menor_peso = -1
            for n in l:
                for a in n.get_aristas_salida():
                    if a.get_llegada().explorado == False:
                        total = a.get_peso()
                        if best_arista is None or total < menor_peso:
                            menor_peso = total
                            best_arista = a

            if best_arista is not None:
                nuevo = best_arista.get_llegada()
                nuevo.explorado = True
                l.append(nuevo)
                resultado.append(best_arista)

        for n in self.__nodos:
            # borramos los atribtos temporales creados
            del n.explorado
        return resultado

    def kruskal(self):
        resultado = []
        uf = UnionFind(self.__nodos)
        h = Heap()
        for a in self.__aristas:
            h.insert(a.get_peso(), a)
        num_nodos = len(self.__nodos)
        while len(resultado) < num_nodos - 1 and h.get_num_elements() > 0:
            peso, a = h.extract_min()
            origen = a.get_salida()
            destino = a.get_llegada()
            if uf.find(origen) != uf.find(destino):
                resultado.append(a)
                uf.union(origen, destino)
        return resultado

    def bellman_ford(self, nodo_fuente):
        n = len(self.__nodos)
        A = [[float('inf')] * (n) for _ in range(0, n + 1)]  # Matriz bidimensional
        ind_s = self.get_index_nodo(nodo_fuente)
        A[0][ind_s] = 0
        for i in range(1, n + 1):
            avanzado = False
            for ind_v in range(0, len(self.__nodos)):
                nodo_v = self.get_nodo_by_index(ind_v)
                minimo = A[i - 1][ind_v]
                for ind_w in range(0, len(self.__nodos)):
                    nodo_w = self.get_nodo_by_index(ind_w)
                    a = self.get_arista(nodo_w, nodo_v)
                    if a is not None:
                        if A[i - 1][ind_w] + a.get_peso() < minimo:
                            minimo = A[i - 1][ind_w] + a.get_peso()
                A[i][ind_v] = minimo
                if A[i][ind_v] != A[i - 1][ind_v]:
                    avanzado = True
            if not avanzado:
                return A[i - 1]
        return None

    def floyd_warshall(self):
        n = len(self.__nodos)
        A = [[[float('inf')] * (n) for _ in range(0, n)] for _ in range(0, n + 1)]  # Matriz tridimensional

        # Creamos la matriz para k = 0
        for ind_v in range(0, n):
            nodo_v = self.get_nodo_by_index(ind_v)
            for ind_w in range(0, n):
                if ind_v == ind_w:
                    A[0][ind_v][ind_w] = 0
                else:
                    nodo_w = self.get_nodo_by_index(ind_w)
                    a = self.get_arista(nodo_v, nodo_w)
                    if a is not None:
                        A[0][ind_v][ind_w] = a.get_peso()
                    else:
                        A[0][ind_v][ind_w] = float('inf')

        # desde k = 1 hasta n, buscamos los caminos pasando por el nodo ind_k=k-1
        for k in range(1, n + 1):
            ind_k = k - 1
            for ind_v in range(0, n):
                for ind_w in range(0, n):
                    A[k][ind_v][ind_w] = min(A[k - 1][ind_v][ind_w], A[k - 1][ind_v][ind_k] + A[k - 1][ind_k][ind_w])

        # comprobación ciclos negativos
        # si para ir de un nodo a el mismo el coste es negativo es que hay un ciclo negativo
        for ind_v in range(0, n):
            if A[n][ind_v][ind_v] < 0:
                return None

        # devolvemos el resultado
        return A[n]


# Pruebas
g1 = Grafo(True)
for nombre in ['S', 'V', 'W', 'U', 'T']:
    g1.add_nodo(nombre)
g1.add_arista('S', 'V', 4)
g1.add_arista('V', 'T', 4)
g1.add_arista('S', 'U', 2)
g1.add_arista('U', 'W', 2)
g1.add_arista('W', 'T', 2)
g1.add_arista('U', 'V', -1)
print(g1.bellman_ford(g1.get_nodo('S')))

g2 = Grafo(True)
for nombre in ['P', 'Q', 'S', 'R', 'T']:
    g2.add_nodo(nombre)
g2.add_arista('P', 'Q', 2)
g2.add_arista('Q', 'S', 2)
g2.add_arista('P', 'R', 4)
g2.add_arista('R', 'S', 4)
g2.add_arista('R', 'T', 3)
g2.add_arista('T', 'S', -5)
print(g2.floyd_warshall())
