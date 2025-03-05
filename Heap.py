class Heap:
    def __init__(self):
        self.__valores = []

    def get_parent(self, index):
        if index == 0:
            return None
        return ((index + 1) // 2) - 1

    def get_left_child(self, index):
        size = len(self.__valores)
        pos = ((index + 1) * 2) - 1
        if pos >= size:
            return None
        return pos

    def get_right_child(self, index):
        size = len(self.__valores)
        pos = ((index + 1) * 2)
        if pos >= size:
            return None
        return pos

    def get_num_elements(self):
        return len(self.__valores)

    def get_valor(self, index):
        return self.__valores[index]

    def insert(self, valor):
        index = self.get_num_elements()
        self.__valores.append(valor)
        p_index = self.get_parent(index)
        while p_index != None:
            if self.get_valor(p_index) > valor:
                self.__valores[index], self.__valores[p_index] = self.__valores[p_index], self.__valores[index]
                index = p_index
                p_index = self.get_parent(index)
            else:
                p_index = None

    def find_min(self):
        size = len(self.__valores)
        if size == 0:
            return None
        return self.__valores[0]

    def __repr__(self):
        s = ""
        for t in self.__valores:
            s += str(t[0]) + ", "
        return s

    def extract_min(self):
        size = len(self.__valores)
        if size == 0:
            return None
        r = self.__valores[0]
        self.__valores[0] = self.__valores[-1]
        self.__valores.pop()
        size -= 1
        if size == 0:
            # El heap se queda vacío, no hay nada que hacer
            return r

        index = 0
        valor = self.get_valor(0)
        seguir = True
        while seguir:
            seguir = False
            hi = self.get_left_child(index)
            hd = self.get_right_child(index)
            if hi == None:
                pass
            elif hd == None:
                if self.get_valor(hi) < self.get_valor(index):
                    self.__valores[index], self.__valores[hi] = self.__valores[hi], self.__valores[index]
            else:
                seguir = False
                # tiene ambos hijos
                if self.get_valor(hi) < self.get_valor(hd) and self.get_valor(hi) < valor:
                    # hijo izquierdo es el menor
                    self.__valores[index], self.__valores[hi] = self.__valores[hi], self.__valores[index]
                    index = hi
                    seguir = True
                elif self.get_valor(hd) <= self.get_valor(hi) and self.get_valor(hd) < valor:
                    # hijo derecho es el menor
                    self.__valores[index], self.__valores[hd] = self.__valores[hd], self.__valores[index]
                    index = hd
                    seguir = True
        return r

