
'''----------- OPCIONAL T13 ----------------'''

class Cueva():
    def __init__(self):
        self.ListaMetalesCueva = []
    def getListaMetalesCueva(self):
        return self.ListaMetalesCueva

    def RemoveMetalCueva(self,indice,weight):
        if weight < self.ListaMetalesCueva[indice].getPeso():
            self.ListaMetalesCueva[indice].peso -= weight
        elif weight == self.ListaMetalesCueva[indice].peso:
            self.ListaMetalesCueva[indice].peso = 0
            self.ListaMetalesCueva.pop(indice)
        elif weight > self.ListaMetalesCueva[indice].peso:
            print('El peso que se quiere introducir es mayor que el disponible')


class Mochila():
    def __init__(self):
        self.ListaMetalesMochila = []
        self.ListaPesosMetalesMochila = []
        self.LimitePeso = None
    def getListaMetalesMochila(self):
        return self.ListaMetalesMochila
    def InsertMetalMochila(self,metal,weight):
        self.ListaMetalesMochila.append(metal)
        if len(self.ListaMetalesMochila) >= 2:
            self.ListaMetalesMochila[-1].peso -= weight
        else:
            self.ListaMetalesMochila[0].peso -= weight #Como hemos hecho un append, la longitud mínima es 1.

class MetalPrecioso():
    def __init__(self,peso,valor,nombre): #peso disponible en la cueva, valor por unidad de peso, str(nombre)
        self.peso = peso #Cantidad disponible del material en unidades de peso
        self.valor = valor #Valor del material por unidad de peso
        self.nombre = nombre
    def __repr__(self): #el identificador es el nombre
        return self.nombre
    def getPeso(self):
        return self.peso
    def getValor(self):
        return self.valor

C = Cueva()#elemrnto de la clase cueva
M = Mochila()#elemento de la clase mochila

#Lista de metales de la cueva
oro = MetalPrecioso(5,1000,'oro')
plata = MetalPrecioso(2,300,'plata')
diamantes = MetalPrecioso(10,3000,'diamantes')
gemas = MetalPrecioso(5,400,'gemas')
caca = MetalPrecioso(40,0.002,'caca')
zanahorias = MetalPrecioso(60,3,'zanahorias')

#introducimos los metales en la cueva
C.ListaMetalesCueva.append(oro)
C.ListaMetalesCueva.append(plata)
C.ListaMetalesCueva.append(diamantes)
C.ListaMetalesCueva.append(caca)
C.ListaMetalesCueva.append(zanahorias)
print('Inicialmente, en la cueva hay:\n'
      'Metal--------Peso-------Valor')
for i in range(len(C.ListaMetalesCueva)):
    print(C.ListaMetalesCueva[i],'--------',C.ListaMetalesCueva[i].peso,'--------',C.ListaMetalesCueva[i].valor)

M.LimitePeso = 25 #el límite de peso de la mochila es 25 unidades.

pesoActual = 0 #peso actual que llevamos en la mochila
maxRatio = 0 #maximo valor/peso disponible de los metales de la cueva
elementoMax = None #elemento con maxRatio
indice = None

while pesoActual < M.LimitePeso:
    espacioDisponible = M.LimitePeso - pesoActual
    maxRatio = 0
    for i in range(len(C.getListaMetalesCueva())):
        if C.ListaMetalesCueva[i].getPeso() != 0 and C.ListaMetalesCueva[i].getValor() / C.ListaMetalesCueva[i].getPeso() > maxRatio:
            maxRatio = C.ListaMetalesCueva[i].getValor() / C.ListaMetalesCueva[i].getPeso()
            elementoMax = C.ListaMetalesCueva[i]
            indice = i
    if elementoMax.getPeso() < M.LimitePeso:
        pesoActual += elementoMax.getPeso()
        M.ListaPesosMetalesMochila.append(elementoMax.getPeso())
        M.InsertMetalMochila(elementoMax,elementoMax.getPeso())
        C.RemoveMetalCueva(indice,elementoMax.getPeso())

    elif elementoMax.getPeso() >= espacioDisponible:
        pesoActual += espacioDisponible
        M.ListaPesosMetalesMochila.append(espacioDisponible)
        M.InsertMetalMochila(elementoMax,espacioDisponible)
        C.RemoveMetalCueva(indice,espacioDisponible)


print('Una vez cometido el robo, los metales que hay en la mochila y sus respectivos pesos son:')
for i in range(len(M.ListaMetalesMochila)):
    print(M.ListaMetalesMochila[i], ' -> ', M.ListaPesosMetalesMochila[i])
print('El valor total del contenido de la mochila es:')
valor = 0
for i in range(len(M.ListaMetalesMochila)):
    valor += M.ListaMetalesMochila[i].valor
print(valor)

print('En la cueva queda:')
for i in range(len(C.ListaMetalesCueva)):
    print(C.ListaMetalesCueva[i],C.ListaMetalesCueva[i].peso)
