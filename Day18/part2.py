s = 21
cubes = [[[False for _ in range(s)] for _ in range(s)] for _ in range(s)]
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        x, y, z = [int(i) - 1 for i in line.split(",")]
        cubes[x][y][z] = True

nair = 0
air = [[[False for _ in range(s)] for _ in range(s)] for _ in range(s)]
for x in range(s):
    for y in range(s):
        air[x][y][0] = not cubes[x][y][0]
        air[x][y][s-1] = not cubes[x][y][s-1]
        air[x][0][y] = not cubes[x][0][y]
        air[x][s-1][y] = not cubes[x][s-1][y]
        air[0][x][y] = not cubes[0][x][y]
        air[s-1][x][y] = not cubes[s-1][x][y]
        nair += air[x][y][0] + air[x][y][-1] + air[x][0][y] + air[x][-1][y] + air[0][x][y] + air[-1][x][y]

run = True
while run:
    run = False
    for x in range(1, s - 1):
        for y in range(1, s - 1):
            for z in range(1, s - 1):
                if not air[x][y][z] and not cubes[x][y][z] and (air[x-1][y][z] or air[x+1][y][z] or air[x][y-1][z] or air[x][y+1][z] or air[x][y][z-1] or air[x][y][z+1]):
                    run = True
                    air[x][y][z] = True
                    nair += 1

surface = 0
for x in range(s):
    for y in range(s):
        for z in range(s):
            if cubes[x][y][z]:
                surface += (x == 0 or (not cubes[x-1][y][z] and air[x-1][y][z])) + (y == 0 or (not cubes[x][y-1][z] and air[x][y-1][z])) + (z == 0 or (not cubes[x][y][z-1] and air[x][y][z-1])) + (x == s - 1 or (not cubes[x+1][y][z] and air[x+1][y][z])) + (y == s - 1 or (not cubes[x][y+1][z] and air[x][y+1][z])) + (z == s - 1 or (not cubes[x][y][z+1] and air[x][y][z+1]))
print(surface)