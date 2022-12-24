s = 21
cubes = [[[False for _ in range(s)] for _ in range(s)] for _ in range(s)]
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        x, y, z = [int(i) - 1 for i in line.split(",")]
        cubes[x][y][z] = True

surface = 0
for x in range(s):
    for y in range(s):
        for z in range(s):
            if cubes[x][y][z]:
                surface += (x == 0 or not cubes[x-1][y][z]) + (y == 0 or not cubes[x][y-1][z]) + (z == 0 or not cubes[x][y][z-1]) + (x == s - 1 or not cubes[x+1][y][z]) + (y == s - 1 or not cubes[x][y+1][z]) + (z == s - 1 or not cubes[x][y][z+1])
print(surface)