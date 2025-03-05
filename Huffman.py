import math
import sys
from Heap import Heap
from Nodo import Nodo

dict = {}

c = sys.stdin.read(1)
longitud_texto = 0
while c != '\n':
    longitud_texto += 1
    count = dict.get(c, 0)
    count += 1
    dict[c] = count
    c = sys.stdin.read(1)

h = Heap()
for x in dict.items():
    n = Nodo(x[0], x[1])
    h.insert(x[1], n)

while h.get_num_elements() > 1:
    n1 = h.extract_min()[1]
    n2 = h.extract_min()[1]
    nuevo = Nodo(n1.get_nombre() + n2.get_nombre(), n1.get_peso() + n2.get_peso())
    nuevo.set_hijo_izquierdo(n1)
    nuevo.set_hijo_derecho(n2)
    h.insert(nuevo.get_peso(), nuevo)

arbol = h.find_min()[1]
codigos = arbol.get_codigos()
total_huffman = 0
for cod, n in codigos:
    print(cod, n.get_nombre(), n.get_peso())
    total_huffman += len(cod) * n.get_peso()

numero_simbolos = len(dict.items())
numero_bits = math.ceil(math.log2(numero_simbolos))
print("numero simbolos", numero_simbolos)
print("numero bits", numero_bits)
print("longitud texto", longitud_texto)
print("total bits", longitud_texto * numero_bits)
print("total bits huffman:", total_huffman)
