heights = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        row = []
        for i in range(len(line)):
            if line[i] == "S":
                start_x = i
                start_y = len(heights)
                row.append(0)
            elif line[i] == "E":
                end_x = i
                end_y = len(heights)
                row.append(25)
            else:
                row.append(ord(line[i]) - ord("a"))
        heights.append(row)

steps = [[None] * len(heights[0]) for _ in range(len(heights))]
steps[start_y][start_x] = 0
updated = [(start_x, start_y)]
while steps[end_y][end_x] is None:
    new_updated = []
    for x, y in updated:
        if x + 1 < len(steps[0]) and heights[y][x] + 1 >= heights[y][x+1] and (steps[y][x+1] is None or steps[y][x+1] > steps[y][x] + 1):
            steps[y][x+1] = steps[y][x] + 1
            new_updated.append((x + 1, y))
        if y + 1 < len(steps) and heights[y][x] + 1 >= heights[y+1][x] and (steps[y+1][x] is None or steps[y+1][x] > steps[y][x] + 1):
            steps[y+1][x] = steps[y][x] + 1
            new_updated.append((x, y + 1))
        if x > 0 and heights[y][x] + 1 >= heights[y][x-1] and (steps[y][x-1] is None or steps[y][x-1] > steps[y][x] + 1):
            steps[y][x-1] = steps[y][x] + 1
            new_updated.append((x - 1, y))
        if y > 0 and heights[y][x] + 1 >= heights[y-1][x] and (steps[y-1][x] is None or steps[y-1][x] > steps[y][x] + 1):
            steps[y-1][x] = steps[y][x] + 1
            new_updated.append((x, y - 1))
    updated = new_updated

print(steps[end_y][end_x])