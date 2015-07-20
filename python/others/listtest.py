import json

with open('listtest.txt', 'r') as f:
    print(f.read())
    print(type(f.read()))


with open('listtest.txt', 'r') as f:
    f1 = f.readline()
    j1 = list(f1)
    print(j1)
    print(f.readline())
    print(f.readline())
