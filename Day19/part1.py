import math

minutes = 24

def eval_blueprint(blueprint, oreperorebot, oreperclaybot, oreperobsbot, clayperobsbot, orepergeobot, obspergeobot):
    #min, geo, ore, clay, obs, orepm, claypm, obspm
    maxorepermin = max(oreperclaybot, oreperobsbot, orepergeobot)
    maxgeo = 0
    states = [(0, 0, 0, 0, 0, 1, 0, 0)]
    while len(states) > 0:
        state = states.pop(-1)
        if state[0] < minutes and state[1] + math.factorial(minutes - state[0]) > maxgeo:
            needobs = state[7] < obspergeobot and (minutes - state[0]) * obspergeobot > state[4] + state[7] * (minutes - state[0])
            needclay = state[6] < clayperobsbot and (minutes - state[0]) * clayperobsbot > state[3] + state[6] * (minutes - state[0])
            needore = state[5] < maxorepermin and (minutes - state[0]) * maxorepermin > state[2] + state[5] * (minutes - state[0])
            stepped = False
            if state[7] > 0:
                timetogeobot = max(0, max(math.ceil((orepergeobot - state[2]) / state[5]), math.ceil((obspergeobot - state[4]) / state[7]))) + 1
                if state[0] + timetogeobot < minutes:
                    states.append((state[0] + timetogeobot, state[1] + minutes - state[0] - timetogeobot, state[2] + timetogeobot * state[5] - orepergeobot, state[3] + timetogeobot * state[6], state[4] + timetogeobot * state[7] - obspergeobot, state[5], state[6], state[7]))
                    stepped = True
            if needobs and state[6] > 0:
                timetoobsbot = max(0, max(math.ceil((oreperobsbot - state[2]) / state[5]), math.ceil((clayperobsbot - state[3]) / state[6]))) + 1
                if state[0] + timetoobsbot < minutes:
                    states.append((state[0] + timetoobsbot, state[1], state[2] + timetoobsbot * state[5] - oreperobsbot, state[3] + timetoobsbot * state[6] - clayperobsbot, state[4] + timetoobsbot * state[7], state[5], state[6], state[7] + 1))
                    stepped = True
            if needclay:
                timetoclaybot = max(0, math.ceil((oreperclaybot - state[2]) / state[5])) + 1
                if state[0] + timetoclaybot < minutes:
                    states.append((state[0] + timetoclaybot, state[1], state[2] + timetoclaybot * state[5] - oreperclaybot, state[3] + timetoclaybot * state[6], state[4] + timetoclaybot * state[7], state[5], state[6] + 1, state[7]))
                    stepped = True
            if needore:
                timetoorebot = max(0, math.ceil((oreperorebot - state[2]) / state[5])) + 1
                if state[0] + timetoorebot < minutes:
                    states.append((state[0] + timetoorebot, state[1], state[2] + timetoorebot * state[5] - oreperorebot, state[3] + timetoorebot * state[6], state[4] + timetoorebot * state[7], state[5] + 1, state[6], state[7]))
                    stepped = True
            if not stepped:
                states.append((minutes, state[1], state[2] + (minutes - state[0]) * state[5], state[3] + (minutes - state[0]) * state[6], state[4] + (minutes - state[0]) * state[7], state[5], state[6], state[7]))
        else:
            maxgeo = max(maxgeo, state[1])
    return maxgeo * blueprint

total_quality = 0
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        spl = line.split(" ")
        blueprint = int(spl[1][:-1])
        oreperorebot = int(spl[6])
        oreperclaybot = int(spl[12])
        oreperobsbot = int(spl[18])
        clayperobsbot = int(spl[21])
        orepergeobot = int(spl[27])
        obspergeobot = int(spl[30])
        total_quality += eval_blueprint(blueprint, oreperorebot, oreperclaybot, oreperobsbot, clayperobsbot, orepergeobot, obspergeobot)
print(total_quality)