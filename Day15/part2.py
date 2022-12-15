sensors = []
beacons = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        spl = line.split(" ")
        sx, sy, bx, by = int(spl[2][2:-1]), int(spl[3][2:-1]), int(spl[8][2:-1]), int(spl[9][2:])
        sensors.append((sx, sy, abs(sx - bx) + abs(sy - by)))

for y in range(4000000):
    excluded = []
    for sensor in sensors:
        dy = abs(y - sensor[1])
        if dy <= sensor[2]:
            excluded.append((sensor[0] - sensor[2] + dy, sensor[0] + sensor[2] - dy))
    i = 1
    while i < len(excluded):
        j = 0
        while j < i:
            if excluded[j][0] >= excluded[i][0] and excluded[j][1] >= excluded[i][1] and excluded[i][1] + 1 >= excluded[j][0]:
                item_i = excluded.pop(i)
                item_j = excluded.pop(j)
                excluded.append((item_i[0], item_j[1]))
                i -= 2
                break
            elif excluded[j][0] <= excluded[i][0] and excluded[j][1] <= excluded[i][1] and excluded[j][1] + 1 >= excluded[i][0]:
                item_i = excluded.pop(i)
                item_j = excluded.pop(j)
                excluded.append((item_j[0], item_i[1]))
                i -= 2
                break
            elif excluded[j][0] <= excluded[i][0] and excluded[j][1] >= excluded[i][1]:
                excluded.pop(i)
                i -= 2
                break
            elif excluded[j][0] >= excluded[i][0] and excluded[j][1] <= excluded[i][1]:
                excluded.pop(j)
                i -= 2
                break
            j += 1
        i += 1
    if len(excluded) > 1:
        x = (excluded[0][1] if excluded[0][1] < excluded[1][0] else excluded[1][1]) + 1
        print(4000000 * x + y)
        break