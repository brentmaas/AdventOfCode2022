chart = [[None]]
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        row = [None if c == " " else c for c in line]
        if len(row) < len(chart[0]):
            row += [None] * (len(chart[0]) - len(row))
        elif len(row) > len(chart[0]):
            for i in range(len(chart)):
                chart[i] += [None] * (len(row) - len(chart[i]))
        chart.append(row)
    chart.pop(0)
    line = f.readline().rstrip()
    path = []
    i = ""
    for c in line:
        if c == "L" or c == "R":
            if i:
                path.append(int(i))
                i = ""
            path.append(c)
        else:
            i += c
    if i:
        path.append(int(i))

#Input specific
warps = {}
for i in range(50):
    warps[(50 + i, 0, 0, -1)] = (0, 150 + i, 1, 0)
    warps[(0, 150 + i, -1, 0)] = (50 + i, 0, 0, 1)
    warps[(99, 50 + i, 1, 0)] = (100 + i, 49, 0, -1)
    warps[(50, i, -1, 0)] = (0, 149 - i, 1, 0)
    warps[(0, 100 + i, -1, 0)] = (50, 49 - i, 1, 0)
    warps[(50, 50 + i, -1, 0)] = (i, 100, 0, 1)
    warps[(i, 100, 0, -1)] = (50, 50 + i, 1, 0)
    warps[(99, 100 + i, 1, 0)] = (149, 49 - i, -1, 0)
    warps[(149, i, 1, 0)] = (99, 149 - i, -1, 0)
    warps[(50 + i, 149, 0, 1)] = (49, 150 + i, -1, 0)
    warps[(49, 150 + i, 1, 0)] = (50 + i, 149, 0, -1)
    warps[(100 + i, 49, 0, 1)] = (99, 50 + i, -1, 0)
    warps[(100 + i, 0, 0, -1)] = (i, 199, 0, -1)
    warps[(i, 199, 0, 1)] = (100 + i, 0, 0, 1)

def move(steps, x, y, dx, dy):
    step = 0
    while step < steps:
        if (x, y, dx, dy) in warps:
            newx, newy, newdx, newdy = warps[(x, y, dx, dy)]
            if chart[newy][newx] == "#":
                break
            x, y, dx, dy = newx, newy, newdx, newdy
            step += 1
            continue
        newx = x + dx
        newy = y + dy
        newdx = dx
        newdy = dy
        if newx < 0 or newy < 0 or newx >= len(chart[0]) or newy >= len(chart) or chart[newy][newx] is None:
            print("MISSED WARP AT", newx, newy, newdx, newdy)
            exit()
        if chart[newy][newx] == "#":
            break
        else:
            x, y, dx, dy = newx, newy, newdx, newdy
            step += 1
    return x, y, dx, dy

x = chart[0].index(".")
y = 0
dx = 1
dy = 0
for step in path:
    if step == "L":
        dx, dy = dy, -dx
    elif step == "R":
        dx, dy = -dy, dx
    else:
        x, y, dx, dy = move(step, x, y, dx, dy)

password = (y + 1) * 1000 + (x + 1) * 4
if dx == 0 and dy == 1:
    password += 1
elif dx == -1 and dy == 0:
    password += 2
elif dx == 0 and dy == -1:
    password += 3
print(password)