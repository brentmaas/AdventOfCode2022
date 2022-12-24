valves = {}
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        spl = line.split(" ")
        flow = int(spl[4][5:-1])
        valves[spl[1]] = (flow, flow == 0, [v.rstrip(",") for v in spl[9:]])

locations = [v for v in valves]
distances = {}
for valve in valves:
    distances[valve] = {}
    for location in locations:
        distances[valve][location] = 0 if valve == location else 1 if location in valves[valve][2] else 1000000

for _ in range(2 * len(locations) - 1):
    for valve in valves:
        for cvalve in valves[valve][2]:
            for ccvalve in valves:
                dist_via = 1 + distances[cvalve][ccvalve]
                if dist_via < distances[valve][ccvalve]:
                    distances[valve][ccvalve] = distances[ccvalve][valve] = dist_via

newvalves = {}
for valve in valves:
    if not valves[valve][1]:
        newvalves[valve] = valves[valve]
valves = newvalves
locations = [v for v in valves]
states = []
for i in range(len(locations) - 1):
    for j in range(i + 1, len(locations)):
        valve = locations[i]
        valve2 = locations[j]
        if valve != valve2:
            closer = valve if distances["AA"][valve] < distances["AA"][valve2] else valve2
            farther = valve if distances["AA"][valve] >= distances["AA"][valve2] else valve2
            states.append([(valve, valve2), tuple([valve == v or valve2 == v for v in valves]), (distances["AA"][valve] + 1, distances["AA"][valve2] + 1), valves[valve][0] + valves[valve2][0], -valves[farther][0] * abs(distances["AA"][valve] - distances["AA"][valve2])])

minutes = 26

maxreleased = 0
while len(states) > 0:
    state = states.pop(-1)
    if not all(state[1]):
        moving = 0 if state[2][0] < state[2][1] else 1
        for dest_valve in valves:
            if not state[1][locations.index(dest_valve)]:
                newpos = [p for p in state[0]]
                newpos[moving] = dest_valve
                newopens = [o for o in state[1]]
                newopens[locations.index(dest_valve)] = True
                dt_moving = min(minutes, state[2][moving] + distances[state[0][moving]][dest_valve] + 1) - state[2][moving]
                newtime = [t for t in state[2]]
                newtime[moving] += dt_moving
                dt = min(newtime) - state[2][moving]
                if dt < distances[state[0][moving]][dest_valve] + 1 and state[2][1 - moving] == minutes:
                    maxreleased = max(maxreleased, state[4] + dt * state[3])
                else:
                    states.append([tuple(newpos), tuple(newopens), tuple(newtime), state[3] + valves[dest_valve][0], state[4] + dt * state[3] - valves[dest_valve][0] * max(newtime[moving] - newtime[1-moving], 0)])
    else:
        maxreleased = max(maxreleased, state[4] + (minutes - min(state[2][0], state[2][1])) * state[3])
print(maxreleased, "      ")