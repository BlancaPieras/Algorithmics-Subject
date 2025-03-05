# función recursiva invertir
def invertir(l):
    print("invirtiendo", l)
    # caso base
    if l == []:
        return l
    # recursividad
    return [l[-1]] + invertir(l[:-1])

l = [1, 2, 3, 4, 5, 6, 7, 8]
print(invertir(l))
