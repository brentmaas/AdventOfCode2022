trees = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        trees.append([int(tree) for tree in line])

w = len(trees[0])
h = len(trees)
hidden = [[1] * w for _ in range(h)]
for x in range(w):
    hidden[0][x] = 0
    hidden[w-1][x] = 0
for y in range(1, h-1):
    hidden[y][0] = 0
    hidden[y][h-1] = 0

for y in range(1, h - 1):
    highest = trees[y][0]
    for x in range(1, w - 1):
        if trees[y][x] > highest:
            hidden[y][x] = 0
        highest = max(highest, trees[y][x])
    highest = trees[y][w-1]
    for x in range(w - 2, 0, -1):
        if trees[y][x] > highest:
            hidden[y][x] = 0
        highest = max(highest, trees[y][x])
for x in range(1, w - 1):
    highest = trees[0][x]
    for y in range(1, h - 1):
        if trees[y][x] > highest:
            hidden[y][x] = 0
        highest = max(highest, trees[y][x])
    highest = trees[h-1][x]
    for y in range(h - 2, 0, -1):
        if trees[y][x] > highest:
            hidden[y][x] = 0
        highest = max(highest, trees[y][x])

print(w * h - sum([sum(row) for row in hidden]))