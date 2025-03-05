import copy


class Objeto:
    def __init__(self, valor, peso):
        self.valor = valor
        self.peso = peso

    def __repr__(self):
        return '[' + str(self.peso) + ',' + str(self.valor) + ']'


class Mochila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.peso = 0
        self.valor = 0
        self.objetos = []

    def introducir(self, objeto):
        self.objetos.append(objeto)
        self.peso += objeto.peso
        self.valor += objeto.valor

    def __repr__(self):
        r = 'Capacidad:' + str(self.capacidad) + ' Peso:' + str(self.peso) + ' Valor:' + str(self.valor) + ' con objetos ('
        for x in self.objetos:
            r += str(x)
        return r + ')'


class Cueva:
    def __init__(self):
        self.objetos = []

    def anadir(self, objeto):
        self.objetos.append(objeto)

# Objetos
o1 = Objeto(3, 4)
o2 = Objeto(2, 3)
o3 = Objeto(4, 2)
o4 = Objeto(4, 3)

# los metemos en la cueva
cueva = Cueva()
cueva.anadir(o1)
cueva.anadir(o2)
cueva.anadir(o3)
cueva.anadir(o4)

# número de objetos y capacidad de la mochila
n = len(cueva.objetos)
C = 6

# en cada posición de la matriz tenemos una mochila en lugar de un entero para saber que objetos lleva
A = [[Mochila(C) for x in range(C + 1)] for y in range(n + 1)]

# Resolvemos todos los subproblemas
# para cada objeto
for i in range(1, n + 1):
    tam = cueva.objetos[i - 1].peso  # tamaño del objeto
    val = cueva.objetos[i - 1].valor # valor del objeto

    # para cada capacidad
    for c in range(0, C + 1):
        # recurrencia corolario
        if tam > c:
            #  no cabe el objeto, sigue igual
            A[i][c] = A[i - 1][c]
        else:
            n_valor = A[i - 1][c - tam].valor + val
            if A[i - 1][c].valor < n_valor:
                # copiamos la mochila y metemos el objeto nuevo
                m = copy.deepcopy(A[i - 1][c - tam])
                m.introducir(cueva.objetos[i - 1])
                A[i][c] = m
            else:
                # es mejor opción seguir con la configuración que teniamos
                A[i][c] = A[i - 1][c]

# mostramos el resultado
print(A[n][c])
