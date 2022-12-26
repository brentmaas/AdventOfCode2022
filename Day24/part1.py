blizzards = []
blizzarddirs = []
valleyheight = -2
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        valleywidth = len(line) - 2
        valleyheight += 1
        for x in range(1, valleywidth + 1):
            if not line[x] == ".":
                if line[x] == ">":
                    blizzards.append((x - 1, valleyheight))
                    blizzarddirs.append((1, 0))
                elif line[x] == "<":
                    blizzards.append((x - 1, valleyheight))
                    blizzarddirs.append((-1, 0))
                elif line[x] == "^":
                    blizzards.append((x - 1, valleyheight))
                    blizzarddirs.append((0, -1))
                elif line[x] == "v":
                    blizzards.append((x - 1, valleyheight))
                    blizzarddirs.append((0, 1))

states = [(0, -1)]
steps = 0
while not (valleywidth - 1, valleyheight - 1) in states:
    steps += 1
    for i in range(len(blizzards)):
        blizzards[i] = ((blizzards[i][0] + blizzarddirs[i][0]) % valleywidth, (blizzards[i][1] + blizzarddirs[i][1]) % valleyheight)
    newstates = []
    for x, y in states:
        if y < 0 or (not (x, y) in blizzards and not (x, y) in newstates):
            newstates.append((x, y))
        if y + 1 < valleyheight and not (x, y + 1) in blizzards and not (x, y + 1) in newstates:
            newstates.append((x, y + 1))
        if y > 0 and not(x, y - 1) in blizzards and not (x, y - 1) in newstates:
            newstates.append((x, y - 1))
        if y >= 0 and x + 1 < valleywidth and not (x + 1, y) in blizzards and not (x + 1, y) in newstates:
            newstates.append((x + 1, y))
        if y >= 0 and x > 0 and not (x - 1, y) in blizzards and not (x - 1, y) in newstates:
            newstates.append((x - 1, y))
    states = newstates
print(steps + 1)