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

    def add_arista(self, salida, llegada, peso = 0):
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

    def get_nodo(self, nombre):
        for n in self.__nodos:
            if n.get_nombre() == nombre:
                return n
        return None

    def camino_mas_corto(self, nodo_fuente):
        MAX_VALUE = 999
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
        MAX_VALUE = 999
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
                        if best_arista == None or total < menor_peso:
                            menor_peso = total
                            best_arista = a

            if best_arista != None:
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
                        if best_arista == None or total < menor_peso:
                            menor_peso = total
                            best_arista = a

            if best_arista != None:
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
        while len(resultado) < num_nodos-1 and h.get_num_elements()> 0:
            peso, a = h.extract_min()
            origen = a.get_salida()
            destino = a.get_llegada()
            if uf.find(origen) != uf.find(destino):
                resultado.append(a)
                uf.union(origen, destino)
        return resultado



g2 = Grafo(False)
g2.add_nodo("S")
g2.add_nodo("A")
g2.add_nodo("B")
g2.add_nodo("C")
g2.add_nodo("D")
g2.add_nodo("T")
g2.add_arista("S", "A", 4)
g2.add_arista("S", "B", 7)
g2.add_arista("S", "C", 3)
g2.add_arista("A", "B", 3)
g2.add_arista("A", "D", 2)
g2.add_arista("C", "D", 3)
g2.add_arista("B", "T", 2)
g2.add_arista("D", "T", 2)

arbol = g2.prim()
print(arbol)

arbol = g2.kruskal()
print(arbol)
