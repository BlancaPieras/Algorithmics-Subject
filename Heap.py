class Heap:
    def __init__(self):
        self.__valores = []

    # devuelve el numero de elementos en el heap
    def get_num_elements(self):
        return len(self.__valores)

    # dado una posicion (la primera es 0) devuelve el padre, si es la cima devuelvve None
    def get_parent(self, index):
        if index == 0:
            return None
        return ((index + 1) // 2) - 1

    # devuelve el índice del hijo izquierdo, si no tiene hijo izquierdo devuelve None
    def get_left_child(self, index):
        size = len(self.__valores)
        pos = ((index + 1) * 2) - 1
        if pos >= size:
            return None
        return pos

    # devuelve el índice del hijo derecho, si no tiene hijo derecho devuelve None
    def get_right_child(self, index):
        size = len(self.__valores)
        pos = ((index + 1) * 2)
        if pos >= size:
            return None
        return pos

    # devuelve el valor asociado al elemento en index
    # el valor es campo usado para mantener ordenado el heap
    def get_valor(self, index):
        return self.__valores[index][0]

    # devuelve la información asociada al elemento en index
    # esta información sólo sirve de acompañamiento, es opcional
    def get_data(self, index):
        return self.__valores[index][1]

    # inserta un nuevo elemento, con valor e información asociada indicada
    def insert(self, valor, data=None):
        t = (valor, data)  # construimos la pareja a insertar
        index = self.get_num_elements()
        self.__valores.append(t)
        p_index = self.get_parent(index)
        while p_index is not None:
            if self.get_valor(p_index) > valor:
                # el valor del nodo padre es mayor qu el nodo actual, los intercambiamos y seguimos comprobando
                self.__valores[index], self.__valores[p_index] = self.__valores[p_index], self.__valores[index]
                index = p_index
                p_index = self.get_parent(index)
            else:
                # fin de la comprobación, se cumple la propiedad
                p_index = None

    # devuelve el valor del elemento mínimo del heap
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

    # devuelve la pareja (valor, informacion) con valor mínimo, el que está en la cima
    # si el heap está vacío devuelve None
    def extract_min(self):
        size = len(self.__valores)
        if size == 0:
            return None

        # hay elementos, nos guardamos el elemento a devolver
        # movemos el último elemento al principio y empezamos a comprobar la propiedad
        r = self.__valores[0]
        self.__valores[0] = self.__valores[-1]
        self.__valores.pop()
        size -= 1
        if size == 0:
            # El heap se queda vacío, no hay nada que hacer
            return r

        index = 0
        valor = self.get_valor(0)
        seguir = True  # variable que indica si hay que comprobar el valor del nodo actual con sus hijos
        while seguir:
            seguir = False
            hi = self.get_left_child(index)
            hd = self.get_right_child(index)
            if hi is None:
                # no tiene hijos, no se puede bajar
                pass
            elif hd is None:
                # no tiene hijo derecho, miramos si el hijo izquierdo es menor
                # no habrá más comparaciones
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
        # devolvemos la cima
        return r
