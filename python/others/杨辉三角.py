def triangles():
    """docstring for triangles"""
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]

result = triangles()
i = 1
for a in result:
    print(a)
    i = i + 1
    if i > 10:
        break

