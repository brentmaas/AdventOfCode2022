with open("Input.txt", "r") as f:
    line = f.readline()
    numstacks = len(line) // 4
    stacks = [[] for _ in range(numstacks)]
    while line:
        if line.startswith(" 1"):
            break
        for i in range(numstacks):
            if line[4*i:4*i+3] != "   ":
                stacks[i].append(line[4*i+1])
        line = f.readline()
    for stack in stacks:
        stack.reverse()
    f.readline()
    while line := f.readline().rstrip():
        spl = line.split(" ")
        num = int(spl[1])
        src = int(spl[3])
        dst = int(spl[5])
        substack = []
        for i in range(num):
            substack.append(stacks[src-1].pop())
        substack.reverse()
        stacks[dst-1] += substack
    out = ""
    for stack in stacks:
        out += stack.pop()
    print(out)