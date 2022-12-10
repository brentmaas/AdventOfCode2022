x = 1
cycles = 0
signal_strengths = 0
measure_at = [20, 60, 100, 140, 180, 220]
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        spl = line.split(" ")
        op = spl[0]
        
        if op == "noop":
            cycles += 1
            newx = x
        elif op == "addx":
            if cycles + 1 in measure_at:
                signal_strengths += x * (cycles + 1)
            v = int(spl[1])
            newx = x + v
            cycles += 2
        
        if cycles in measure_at:
            signal_strengths += x * cycles
        
        x = newx

print(signal_strengths)