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
states = [[valve, tuple([valve == v for v in valves]), distances["AA"][valve] + 1, valves[valve][0], 0] for valve in valves]

minutes = 30

maxreleased = 0
while len(states) > 0:
    state = states.pop(0)
    if not all(state[1]):
        for dest_valve in valves:
            if not state[1][locations.index(dest_valve)]:
                newopens = [o for o in state[1]]
                newopens[locations.index(dest_valve)] = True
                dt = min(minutes, state[2] + distances[state[0]][dest_valve] + 1) - state[2]
                if dt < distances[state[0]][dest_valve] + 1:
                    maxreleased = max(maxreleased, state[4] + dt * state[3])
                else:
                    states.append([dest_valve, tuple(newopens), state[2] + dt, state[3] + valves[dest_valve][0], state[4] + dt * state[3]])
    else:
        maxreleased = max(maxreleased, state[4] + (minutes - state[2]) * state[3])
print(maxreleased, "      ")