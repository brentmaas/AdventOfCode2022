rocks = [["####"], [".#.", "###", ".#."], ["###", "..#", "..#"], ["#", "#", "#", "#"], ["##", "##"]]

with open("Input.txt", "r") as f:
    windpattern = f.readline().rstrip()

room = []
roomwidth = 7
wind = 0
rock = 0

def intersects_at(x, y):
    if y < 0 or x < 0 or x + len(rocks[rock][0]) > roomwidth:
        return True
    for ry in range(len(rocks[rock])):
        for rx in range(len(rocks[rock][ry])):
            if rocks[rock][ry][rx] == "#" and len(room) > y + ry and room[y+ry][x+rx] == "#":
                return True
    return False

for _ in range(2022):
    x = 2
    y = len(room) + 3
    run = True
    while run:
        dx = 1 if windpattern[wind] == ">" else -1
        if not intersects_at(x + dx, y):
            x += dx
        wind = (wind + 1) % len(windpattern)
        run = not intersects_at(x, y - 1)
        if run:
            y -= 1
    for ry in range(len(room), y + len(rocks[rock])):
        room.append(["."] * 7)
    for ry in range(len(rocks[rock])):
        for rx in range(len(rocks[rock][ry])):
            if rocks[rock][ry][rx] == "#":
                room[y+ry][x+rx] = "#"
    rock = (rock + 1) % len(rocks)

print(len(room))