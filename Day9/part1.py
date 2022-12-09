x_h = y_h = x_t = y_t = 0
dx = {'U': 0, 'R': 1, 'D': 0, 'L': -1}
dy = {'U': 1, 'R': 0, 'D': -1, 'L': 0}
visited = {0: [0]}

with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        dir, steps = line.split(" ")
        for _ in range(int(steps)):
            x_n = x_h + dx[dir]
            y_n = y_h + dy[dir]
            adx = abs(x_t - x_n)
            ady = abs(y_t - y_n)
            if adx > 1 or ady > 1:
                if (adx == 2 and ady == 2) or adx == 0 or ady == 0:
                    x_t, y_t = (x_t + x_n) // 2, (y_t + y_n) // 2
                else:
                    x_t += 1 if x_n > x_t else -1
                    y_t += 1 if y_n > y_t else -1
            x_h, y_h = x_n, y_n
            if not x_t in visited:
                visited[x_t] = [y_t]
            elif not y_t in visited[x_t]:
                visited[x_t].append(y_t)

print(sum([len(visited[i]) for i in visited]))