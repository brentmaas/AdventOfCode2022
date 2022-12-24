file = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        file.append(int(line))
order = [i for i in range(len(file))]

for i in range(len(file)):
    j = order.index(i)
    val = file.pop(j)
    order.pop(j)
    newj = (j + val) % len(file)
    file.insert(newj, val)
    order.insert(newj, i)

izero = file.index(0)
print(file[(1000 + izero) % len(file)] + file[(2000 + izero) % len(file)] + file[(3000 + izero) % len(file)])