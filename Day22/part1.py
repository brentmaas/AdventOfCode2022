chart = [[None]]
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        row = [None if c == " " else c for c in line]
        if len(row) < len(chart[0]):
            row += [None] * (len(chart[0]) - len(row))
        elif len(row) > len(chart[0]):
            for i in range(len(chart)):
                chart[i] += [None] * (len(row) - len(chart[0]))
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

def move(steps, x, y, dx, dy):
    for _ in range(steps):
        newx = (x + dx) % len(chart[0])
        newy = (y + dy) % len(chart)
        while chart[newy][newx] is None:
            newx = (newx + dx) % len(chart[0])
            newy = (newy + dy) % len(chart)
        if chart[newy][newx] == "#":
            break
        else:
            x, y = newx, newy
    return x, y

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
        x, y = move(step, x, y, dx, dy)

password = (y + 1) * 1000 + (x + 1) * 4
if dx == 0 and dy == 1:
    password += 1
elif dx == -1 and dy == 0:
    password += 2
elif dx == 0 and dy == -1:
    password += 3
print(password)