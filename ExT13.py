
class Nodo():
    def __init__(self):
        self.nombre = ''
        self.peso = None
        self.codigo = []
        self.esnuevo = False # if esnuevo==True, el nodo ha sido creado en la fusión, else, es nodo etiquetado (del diccionario)
        self.HI = None
        self.HD = None
    def __repr__(self):
        return self.nombre
    def getHI(self):
        return self.HI
    def getHD(self):
        return self.HD

'-------------------- HUFFMAN --------------------'
print('Escribe')
text = input()
diccionario = {}
for letra in text: #si la letra está en el diccionario, sumamos uno a su valor, si no, su valor es 1
    if letra in diccionario:
        diccionario[letra] += 1
    else:
        diccionario[letra] = 1

bosque=[] #creamos la lista de árboles, inicialmente será la lista de nodos del diccionario

for i in diccionario: #a cada nodo del diccionario
    n = Nodo() #lo convertimos en elemento de la clase nodo
    n.nombre = str(i) #le asignamos como nombre la clave del diccionario
    n.peso = diccionario.get(i) #su peso es el valor en el diccionario
    bosque.append(n) #añadimos el nodo al bosque

def Min(bosque): #buscamos el arbol de frecuencia acumulada mínima
    min = 1000000000000000
    arbolmin = None
    for i in bosque: #para cada arbol del bosque
        if i.peso < min: #si la frecuencia acumulada del arbol es menor que el minimo
            min = i.peso #el minimo es esa frecuencia
            arbolmin = i #y el árbol de minima frecuencia es él
    bosque.remove(arbolmin) #eliminamos el árbol mínimo del bosque
    return arbolmin


while len(bosque) >= 2: #mientras no tengamos un solo árbol
    t1 = Min(bosque) #eliminamos del bosque los dos árboles con menor frecuencia acumulada y los fusionamos
    t2 = Min(bosque)
    t = Nodo() #creando un nuevo árbol en bosque y le asignamos sus árboles hijos
    t.HI = t1
    t.HD = t2
    t.nombre = 'nuevo'
    t.esnuevo = True #el nodo raíz será nuevo
    t.peso = t1.peso + t2.peso #su peso es la frecuencia acumulada de los dos arboles fusionados
    bosque.append(t) #añadimos el nuevo árbol

ListaNodos =[]
def Codigo(nodo, codigo): #nodoactual=boswue[0] inicialmente. Nodo = raiz que buscamos
    nodo.codigo = codigo.copy()
    if nodo.esnuevo == False:
        ListaNodos.append(nodo)
    if nodo.HI != None:
        aux = codigo.copy()
        aux.append(0)
        Codigo(nodo.getHI(),aux)
    if nodo.HD != None:
        aux = codigo.copy()
        aux.append(1)
        Codigo(nodo.getHD(), aux)

Codigo(bosque[0],[])

for i in ListaNodos:
    print(i,'->',i.peso,'->', i.codigo)