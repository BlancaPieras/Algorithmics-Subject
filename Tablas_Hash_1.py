import sys

dict = {}

c = sys.stdin.read(1)
while c != '\n':
    count = dict.get(c, 0)
    count += 1
    dict[c] = count
    c = sys.stdin.read(1)

for x in dict.items():
    print(x[0], ":", x[1])
