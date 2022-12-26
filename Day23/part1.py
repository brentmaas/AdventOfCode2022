elves = []
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        elves.append(["."] + [c for c in line] + ["."])
elves = [["."] * len(elves[0])] + elves + [["."] * len(elves[0])]

def propose(x, y, dir):
    adj = [elves[y-1][x], elves[y-1][x+1], elves[y][x+1], elves[y+1][x+1], elves[y+1][x], elves[y+1][x-1], elves[y][x-1], elves[y-1][x-1]] #Clockwise N->NW
    adj = [iadj == "#" for iadj in adj]
    if any(adj):
        for i in range(4):
            if (i + dir) % 4 == 0 and not adj[0] and not adj[1] and not adj[7]:
                return (x, y - 1)
            elif (i + dir) % 4 == 1 and not adj[4] and not adj[3] and not adj[5]:
                return (x, y + 1)
            elif (i + dir) % 4 == 2 and not adj[6] and not adj[7] and not adj[5]:
                return (x - 1, y)
            elif (i + dir) % 4 == 3 and not adj[2] and not adj[1] and not adj[3]:
                return (x + 1, y)
    return None

for dir in range(10):
    proposals = {}
    padleft, padright, padtop, padbottom = 0, 0, 0, 0
    for x in range(1, len(elves[0]) - 1):
        for y in range(1, len(elves) - 1):
            if elves[y][x] == "#":
                proposal = propose(x, y, dir)
                if not proposal is None:
                    if proposal in proposals:
                        proposals[proposal].append((x, y))
                    else:
                        proposals[proposal] = [(x, y)]
                    if proposal[0] == 0:
                        padleft = 1
                    elif proposal[0] == len(elves[0]) - 1:
                        padright = 1
                    if proposal[1] == 0:
                        padtop = 1
                    elif proposal[1] == len(elves) - 1:
                        padbottom = 1
                else:
                    proposals[(x, y)] = [(x, y)]
    newelves = []
    for y in range(-padtop, len(elves) + padbottom):
        newelves.append(["."] * (len(elves[0]) + padleft + padright))
    for proposal in proposals:
        if len(proposals[proposal]) > 1:
            for pos in proposals[proposal]:
                newelves[pos[1]+padtop][pos[0]+padleft] = "#"
        else:
            newelves[proposal[1]+padtop][proposal[0]+padleft] = "#"
    elves = newelves

minx = len(elves[0])
miny = len(elves)
maxx = 0
maxy = 0
numelves = 0
for y in range(len(elves)):
    for x in range(len(elves[0])):
        if elves[y][x] == "#":
            minx = min(minx, x)
            miny = min(miny, y)
            maxx = max(maxx, x)
            maxy = max(maxy, y)
            numelves += 1
print((maxx - minx + 1) * (maxy - miny + 1) - numelves)