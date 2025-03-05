# función recursiva mcd
def mcd(a, b):
    # print(a, b) # para ver que llamadas se realizan
    # caso base
    if b == 0:
        return a
    # recursividad de cola
    return mcd(b, a % b)


print(mcd(2214, 2034))
