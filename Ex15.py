import numpy as np

class Objeto():
    def __init__(self,tamaño,valor,nombre): #peso disponible en la cueva, valor por unidad de peso, str(nombre)
        self.tamaño = tamaño #Cantidad disponible del material en unidades de peso
        self.valor = valor #Valor del material por unidad de peso
        self.nombre = nombre
    def __repr__(self): #el identificador es el nombre
        return self.nombre
    def getTamaño(self):
        return self.tamaño
    def getValor(self):
        return self.valor
    def appendLista(self,objeto,lista):
        lista.append(objeto)

class Cueva():
    def __init__(self):
        self.ListaObjetos = []
        self.ListaValores = []
        self.ListaTamaños = []
    def getTamaños(self):
        return self.ListaTamaños
    def getValores(self):
        return self.ListaValores
    def getObjetos(self):
        return self.ListaObjetos
    def appendValor(self,valor):
        self.ListaValores.append(valor)
    def appendTamaño(self,tamaño):
        self.ListaTamaños.append(tamaño)
    def appendObjeto(self,objeto):
        self.ListaObjetos.append(objeto)

    def mochila(self, c):
        n = len(self.getObjetos())
        mochila = [[[] for i in range(c+1)]for i in range(n+1)]
        A = np.zeros([n + 1, c + 1])  # matriz nula
        for i in range(1, n + 1):
            for C in range(0, c + 1):
                tam = self.ListaTamaños[i - 1]
                #recurrencia corolario
                if tam > C:
                    A[i][C] = A[i - 1][C]
                    mochila[i][C] = mochila[i-1][C]
                else:
                    A[i][C] = max(A[i - 1][C], A[i - 1][C - tam] + self.ListaValores[i - 1])
                    if max(A[i - 1][C], A[i - 1][C - tam] + self.ListaValores[i - 1]) == A[i - 1][C]:
                        mochila[i][C] = mochila[i-1][C].copy()
                    else:
                        mochila[i][C] = mochila[i - 1][C - tam].copy()
                        mochila[i][C].append(self.ListaObjetos[i-1])

        print('La matriz de objetos añadidos a la mochila en cada caso es:' )
        for i in range(n+1):
            print(mochila[i][:])
        print('El valor obtenido en cada caso es:\n',A)
        return "La solución valor máximo, objetos escogidos es:",A[n][C], mochila[n][C]

print('En cada caso, en las matrices de valores, las columnas son las capacidades y las filas, los objetos. De la misma '
      'forma en las matrices mochila.')
'---------EJEMPLO DIAPOSITIVAS---------'
print('------------------EJEMPLO DIAPOSITIVAS---------------')
C = Cueva()

uno = Objeto(4,3,'uno')
C.ListaTamaños.append(uno.tamaño)
C.ListaValores.append(uno.valor)
C.ListaObjetos.append(uno)

dos = Objeto(3,2,'dos')
C.ListaTamaños.append(dos.tamaño)
C.ListaValores.append(dos.valor)
C.ListaObjetos.append(dos)

tres = Objeto(2,4,'tres')
C.ListaTamaños.append(tres.tamaño)
C.ListaValores.append(tres.valor)
C.ListaObjetos.append(tres)

cuatro = Objeto(3,4,'cuatro')
C.ListaTamaños.append(cuatro.tamaño)
C.ListaValores.append(cuatro.valor)
C.ListaObjetos.append(cuatro)

print(C.mochila(6))

'--------------OTRO EJEMPLO------------'
print('------------------OTRO EJEMPLO---------------')

M = Cueva()
u = Objeto(12,4,'uno')
M.ListaTamaños.append(u.tamaño)
M.ListaValores.append(u.valor)
M.ListaObjetos.append(u)

d = Objeto(2,2,'dos')
M.ListaTamaños.append(d.tamaño)
M.ListaValores.append(d.valor)
M.ListaObjetos.append(d)

t = Objeto(1,2,'tres')
M.ListaTamaños.append(t.tamaño)
M.ListaValores.append(t.valor)
M.ListaObjetos.append(t)

c = Objeto(1,1,'cuatro')
M.ListaTamaños.append(c.tamaño)
M.ListaValores.append(c.valor)
M.ListaObjetos.append(c)

s = Objeto(4,10,'cinco')
M.ListaTamaños.append(s.tamaño)
M.ListaValores.append(s.valor)
M.ListaObjetos.append(s)

print(M.mochila(15))

'--------------OPCIONALES----------'

'1) ¿Qué sucede si la capacidad no es entera pero los objetos sí tienen tamaño entero?' \
'Se observa que dado que la capacidad no es entera, no se puede iterar con indices de las columnas de una matriz que no' \
'sean enteros. (error en la línea 40)'

'2) ¿Qué sucede si la capacidad es entera pero los tamaños son números racionales conocidos?' \
'En el cálculo del tam, resulta un número que no es entero, y dado que usamos ese número para iterar sobre las columnas ' \
'de la matriz, no es posible ejecutar la línea 47.'

'3) ¿Qué sucede si la capacidad es entera pero los tamaños son números no racionales conocidos' \
'Ocurre lo mismo que en el caso 2.'

'4) ¿Qué sucede si todos los datos son números no racionales conocidos?' \
'Hay dos errores: El primero es la creación de las matrices A y mochila, ya que la dimensión de las columnas ' \
'no es entera. Por otra parte, ya que el número de columnas no sería entero, tampoco se puede ejecutar la línea 47.'
