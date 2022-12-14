x0 = 500
cave = [["."]]

def adapt_cave(x, y):
    global x0, cave
    if x < x0:
        for i in range(len(cave)):
            cave[i] = ["."] * (x0 - x) + cave[i]
        x0 = x
    elif x > x0 + len(cave[0]) - 1:
        for i in range(len(cave)):
            cave[i] = cave[i] + ["."] * (x - x0 - len(cave[i]) + 1)
    if y > len(cave) - 1:
        for _ in range(y - len(cave) + 1):
            cave.append(["."] * len(cave[0]))

with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        points = [[int(i) for i in point.split(",")] for point in line.split(" -> ")]
        adapt_cave(points[0][0], points[0][1])
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            adapt_cave(x2, y2)
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    cave[y][x-x0] = "#"

xs = 500 - x0
sands = 0
while True:
    x = xs
    y = 0
    while y < len(cave) - 1:
        if cave[y+1][x] == ".":
            y += 1
        elif x == 0:
            y = len(cave) - 1
            break
        elif cave[y+1][x-1] == ".":
            y += 1
            x -= 1
        elif x == len(cave[0]) - 1:
            y = len(cave) - 1
            break
        elif cave[y+1][x+1] == ".":
            y += 1
            x += 1
        else:
            break
    if y == len(cave) - 1:
        break
    cave[y][x] = "o"
    sands += 1

print(sands)