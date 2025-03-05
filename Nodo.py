class Nodo:
    def __init__(self, nombre, peso):
        self.__nombre = nombre
        self.__peso = peso
        self.__left_child = None
        self.__right_child = None

    def get_nombre(self):
        return self.__nombre

    def get_peso(self):
        return self.__peso

    def get_hijo_izquierdo(self):
        return self.__left_child

    def get_hijo_derecho(self):
        return self.__right_child

    def set_hijo_izquierdo(self, hi):
        self.__left_child = hi

    def set_hijo_derecho(self, hd):
        self.__right_child = hd

    def __repr__(self):
        return self.__nombre

    @staticmethod
    def genera_codigos(prefix, n, codigos):
        hi = n.get_hijo_izquierdo()
        if hi == None:
            t = (prefix, n)
            codigos.append(t)
            return

        Nodo.genera_codigos(prefix + "0", hi, codigos)

        hd = n.get_hijo_derecho()
        if hd != None:
            Nodo.genera_codigos(prefix + "1", hd, codigos)

    def get_codigos(self):
        r = []
        Nodo.genera_codigos("", self, r)
        return r
