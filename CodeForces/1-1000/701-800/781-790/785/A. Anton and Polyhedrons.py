n = int(input())
face = 0

for i in range(n):
    s = input()
    match s:
        case 'Tetrahedron': face += 4
        case 'Cube': face += 6
        case 'Octahedron': face += 8
        case 'Dodecahedron': face += 12
        case 'Icosahedron': face += 20

print(face)