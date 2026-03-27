n = int(input())
tetrahedron = 4
cube = 6 
octahedron = 8 
dodecahedron = 12 
icosahedron = 20
value = 0
for i in range(n):
    k = input()
    if k.lower() == 'tetrahedron':
        value += tetrahedron
    elif k.lower() == 'cube':
        value += cube
    elif k.lower() == 'octahedron':
        value += octahedron
    elif k.lower() == 'dodecahedron':
        value += dodecahedron
    else:
        value += icosahedron
print(value)