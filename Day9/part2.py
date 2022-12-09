l = 10
x = [0] * l
y = [0] * l
dx = {'U': 0, 'R': 1, 'D': 0, 'L': -1}
dy = {'U': 1, 'R': 0, 'D': -1, 'L': 0}
visited = {0: [0]}

with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        dir, steps = line.split(" ")
        for _ in range(int(steps)):
            x_n = x[0] + dx[dir]
            y_n = y[0] + dy[dir]
            for i in range(1, l):
                adx = abs(x[i] - x_n)
                ady = abs(y[i] - y_n)
                if adx > 1 or ady > 1:
                    if (adx == 2 and ady == 2) or adx == 0 or ady == 0:
                        x[i-1], y[i-1], x_n, y_n = x_n, y_n, (x[i] + x_n) // 2, (y[i] + y_n) // 2
                    else:
                        dx_n = 1 if x_n > x[i] else -1
                        dy_n = 1 if y_n > y[i] else -1
                        x[i-1], y[i-1], x_n, y_n = x_n, y_n, x[i] + dx_n, y[i] + dy_n
                else:
                    x[i-1], y[i-1], x_n, y_n = x_n, y_n, x[i], y[i]
            x[l-1], y[l-1] = x_n, y_n
            if not x[l-1] in visited:
                visited[x[l-1]] = [y[l-1]]
            elif not y[l-1] in visited[x[l-1]]:
                visited[x[l-1]].append(y[l-1])

print(sum([len(visited[i]) for i in visited]))