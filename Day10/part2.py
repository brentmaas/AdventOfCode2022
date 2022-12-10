x = 1
cycles = 0
signal_strengths = 0
screen = [["."] * 40 for _ in range(6)]

def get_pixel_at(x, cycle):
    screen_x = cycle % 40
    return "#" if screen_x in [x, x + 1, x + 2] else "."

with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        spl = line.split(" ")
        op = spl[0]
        
        if op == "noop":
            cycles += 1
            newx = x
        elif op == "addx":
            screen[cycles // 40][cycles % 40] = get_pixel_at(x, cycles + 1)
            v = int(spl[1])
            newx = x + v
            cycles += 2
        
        if cycles > 0:
            screen[(cycles - 1) // 40][(cycles - 1) % 40] = get_pixel_at(x, cycles)
        
        x = newx

for row in screen:
    print("".join(row))