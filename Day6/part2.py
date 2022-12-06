base = 13
with open("Input.txt", "r") as f:
    inp = f.readline().rstrip()
    window = [" "] * base
    i = 0
    skip = base
    while i < len(inp):
        if inp[i] in window:
            skip = max(skip, base - window[::-1].index(inp[i]))
        elif skip <= 0:
            print(i + 1)
            exit()
        window.pop(0)
        window.append(inp[i])
        i += 1
        skip -= 1