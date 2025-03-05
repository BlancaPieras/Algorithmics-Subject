
import abc

class casas():
    #Es abstracto ya que va a ser unifam. o piso. Lo ponemos primero ya que necesitamos definir un listado
    #de casas dentro de la clase edificio (atributo)
    @abc.abstractmethod
    def __init__(self, metroscuadrados=0, valormercado=0, identificador= " "):
        self.metroscuadrados=metroscuadrados
        self.valormercado=valormercado
        self.__identificador=identificador
    #necesitamos disponer del identificador para poder introducirlo en la lista de casas de cada edificio.
    def __repr__(self):
        return self.__identificador #para que el representante de casa en el print sea el identificador

#ponemos edificio antes que solar para poder poner un objeto de esta clase como atributo de solar.
#La dotamos de la operación añadircasa para que cada edificio tenga su listado de casas 'como atributo'?.
class edificios():
    #numedificios = 0 #fer llista, no contador
    def __init__(self): #si el edificio es de una casa unifamiliar,
                                                             # no puede tener pisos, hacemos la distinción.
                                                             # Además, pasamos por parámetro la lista
                                                             # de dasas de cada edificio en particular
        self.listacasased = []

    def añadircasa(self, casa=casas()):
        self.listacasased.append(casa) #cada casa que se añade al edificio, se añade a la lista de
                                       # casas del edificio concreto
class solares():
    # Constructor que recibe tres parámetros base, altura y edificio. El edificio será un
    # único objeto de la clase edificio o nada.
    def __init__(self, ancho=0, alto=0, edificio = edificios(), identificador = ''):
        self.edificio = edificio
        self.__ancho = ancho
        self.__alto = alto
        self.__identificador = identificador

    def __repr__(self):
        return self.__identificador

    #perimetro = suma de los lados
    def perimetro(self):
        return (self.__alto * 2 + self.__ancho * 2)

    #area = base * altura
    def area(self):
        return (self.__ancho * self.__alto)

    def valormc(self): #El valor por m2 del solar es la media aritmética de el valor
                       # por m2 de las casas que hay en él si no está vacío
        valorm2casa = 0
        if self.edificio != None:
            for i in self.edificio.listacasased: #el valor por m2 de cada casa es el valor de mercado / sus metros.
                valorm2casa += (i.valormercado/i.metroscuadrados) #sumatorio del valor por m2 de cada casa
            valorm2 = valorm2casa/len(self.edificio.listacasased) #sumatorio del valor por m2 de cada casa/ n casas
        else: #si el solar está vacío adjudicamos el valor 0.
            valorm2 = 0
        return (valorm2)

    def varianza(self):
        sumatorio1 = 0
        aux = 0
        sumatorio2 = 0
        for i in self.edificio.listacasased:
            sumatorio1 += (i.valormercado)**2
            aux += i.valormercado
            sumatorio2 = aux**2
        return (sumatorio1/len(self.edificio.listacasased)-sumatorio2/(len(self.edificio.listacasased))**2)


class ciudad():
    def __init__(self):
        self.listasolares = []

    def añadirsolar(self, solar = solares()):
        self.listasolares.append(solar)

    def contared(self): #recorremos la lista de solares para ver cuántos no están vacíos y los sumamos.
                        #éste será el n de edificios.
        contadored = 0
        for i in self.listasolares:
            if i.edificio != None:
                contadored += 1
        return(contadored)

    def solaresvacios(self):
        solvac = [] #lista de solares vacíos
        for i in self.listasolares:
            if i.edificio == None:
                solvac.append(i) #si un solar no tiene edificio, añadimos su identificador a la lista.
        return (solvac)

    def piscinasyterrazas(self):
        npiscinas = 0
        nterrazas = 0
        for i in self.listasolares: #recorremos la lista solares
            if i.edificio != None: #si el solar no está vacío
                for j in i.edificio.listacasased: #Recorremos la lista de casas del edificio en cuestión.
                    if isinstance(j,aticos) == True: #si la casa que tratamos es un ático
                        if j.terraza == True: #y además tiene terraza
                            nterrazas += 1 #sumamos uno al contador de terrazas
                    if isinstance(j, unifamiliar) == True: #si la casa es unifamiliar
                        if j.piscina == True: #y además tiene piscina
                            npiscinas += 1 #sumamos 1 al contador de piscinas
        return (npiscinas,nterrazas) #devolvemos la tupla de n piscinas y n terrazas.

    def porcentaje(self):
        npisos = 0
        naticos = 0
        for i in self.listasolares: #recorremos la lista solares
            if i.edificio != None: #si el solar no está vacío
                for j in i.edificio.listacasased: #recorremos su lista de casas
                    if isinstance(j,pisos): #si la casa es un piso
                        npisos += 1 #sumamos 1 piso al contador de pisos
                    if isinstance(j,aticos): # si es ático
                        naticos += 1 #sumamos 1 ático al contador de áticos
        return (naticos*100/npisos) #Hacemos la regla de tres pertinente


#casa unifamiliar con piscina o no
class unifamiliar(casas):
    def __init__(self, piscina=False, metroscuadrados=0, valormercado=0, identificador = " "):
        super().__init__(metroscuadrados, valormercado, identificador)
        self.piscina = piscina


#la clase piso está vacía. Hay pisos que son áticos y otros no
class pisos(casas):
    def __init__(self, metroscuadrados=0, valormercado=0, identificador= " "):
        super().__init__(metroscuadrados, valormercado, identificador) #Herencia con casa


#el ático es un piso que puede tener terraza (True) o no (False)
class aticos(pisos):
    def __init__(self, terraza = False, metroscuadrados=0, valormercado=0, identificador = " "):
        super().__init__( metroscuadrados, valormercado, identificador) #Herencia con piso
        self.terraza = terraza #definimos el nuevo atributo terraza, propio de áticos


#CREAMOS LOS DATOS

e1 = edificios()
e2 = edificios()
e3 = edificios()
e4 =edificios()

s0 = solares(500,900, None ,'s0') #solar vacío
s1 = solares(100,150,e1,'s1')
s2 = solares(200,300,e2,'s2')
s3 = solares(900,500, e3,'s3')
s4 = solares(100,150,e4,'s4')



p1 = pisos(40,300000,"BJ")
u1 = unifamiliar(True,40,300000,"14B")
u2 = unifamiliar(True, 50, 40000, 'una vaina loca')
u3 = unifamiliar(False, 30 , 40000 , 'pringao sin piscina')

a1 = aticos(True,50,100000,"A1")
a2 = aticos(True,50, 404000, 'A2')
a3= aticos(False,40,229292, '3C')

#PROGRAMA PRINCIPAL

e1.añadircasa(p1)
e1.añadircasa(a1)
e1.añadircasa(a2)
e1.añadircasa(a3)
e2.añadircasa(u1)
e3.añadircasa(u2)
e4.añadircasa(u3)

c1 = ciudad()
c1.añadirsolar(s0)
c1.añadirsolar(s1)
c1.añadirsolar(s2)
c1.añadirsolar(s3)
c1.añadirsolar(s4)

print('El número de casas con piscina y casas con terraza es', c1.piscinasyterrazas())

print('Los solares en la ciudad son:', c1.listasolares)

print('El valor por m2 del solar s0 es', s0.valormc())
print('El valor por m2 del solar s1 es', s1.valormc())
print('El valor por m2 del solar s2 es', s2.valormc())
print('El valor por m2 del solar s3 es', s3.valormc())
print('El valor por m2 del solar s4 es', s4.valormc())

print('Los solares vacíos son', c1.solaresvacios(), 'que suman un total de', len(c1.solaresvacios()))

print('El porcentaje de áticos respecto de pisos es', c1.porcentaje(), '%')

print(s1.varianza())