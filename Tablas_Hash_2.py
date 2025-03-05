import sys

dict = {}

linea = sys.stdin.readline()[:-1]
while linea != '':
    count = dict.get(linea, 0)
    count += 1
    dict[linea] = count
    linea = sys.stdin.readline()[:-1]

for x in dict.items():
    print(x[0], ":", x[1])
