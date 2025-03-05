import copy


class UnionFind:
    def __init__(self, nodos):
        self.__dict = {}
        for n in nodos:
            self.__dict[n] = n

    def union(self, nodo1, nodo2):
        self.__dict[nodo1] = self.__dict[nodo2]

    def find(self, nodo):
        while nodo != self.__dict[nodo]:
            nodo = self.__dict[nodo]
        return nodo
