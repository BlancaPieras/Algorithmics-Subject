'''-------------TABLAS HASH------------'''

#Creamos un diccionario con las claves letras y los valores 0, estos serán las apariciones.
diccionari1 = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'ñ':0,
              'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0,' ':0 ,'.':0,',':0}

#El usuario introduce la frase
print('Introduzca una línea de texto en minusculas:\n')

texto = input() #

#Cada vez que aparece una letra en el texto, sumamos 1 a su valor
for letra in texto:
    if letra in diccionari1:
        diccionari1[letra] += 1
    else:
        diccionari1[letra] = 1

#Imprimimos las claves y valores finales
print('Las apariciones de cada letra del diccionario son:')
for item in diccionari1:
    print(item , '->', diccionari1.get(item))

diccionari2 = {'Mia':0,'Patricia':0,'JJ':0,'Tomeu':0,'Frodo':0,'Xesc':0,'Blanca':0}

print('Escribe el nombre de tus alumnos preferidos de la lista, tantas veces como quieras separados por espacios:')

text = input()

LlistaParaules = text.split() #Cada vez que se encuentra con un espacio, añade la palabra a la lista

#Aumentamos los valores de las palabras del diccionario
for item in LlistaParaules:
    if item in diccionari2:
        diccionari2[item] += 1
    else:
        diccionari2[item] = 1

#Imprimimos las claves y valores finales
for item in diccionari2:
    print(item, '->', diccionari2.get(item))