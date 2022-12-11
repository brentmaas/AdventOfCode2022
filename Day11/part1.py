monkeys = []
with open("Input.txt", "r") as f:
    while line := f.readline():
        spl = line.strip().replace(",", "").split(" ")
        if spl[0] == "Monkey":
            monkeys.append({"inspections": 0})
        elif spl[0] == "Starting":
            monkeys[-1]["items"] = [int(i) for i in spl[2:]]
        elif spl[0] == "Operation:":
            monkeys[-1]["operation"] = spl[3:]
        elif spl[0] == "Test:":
            monkeys[-1]["divisor"] = int(spl[3])
        elif spl[0] == "If" and spl[1] == "true:":
            monkeys[-1]["true"] = int(spl[5])
        elif spl[0] == "If" and spl[1] == "false:":
            monkeys[-1]["false"] = int(spl[5])

for _ in range(20):
    for i in range(len(monkeys)):
        monkeys[i]["inspections"] += len(monkeys[i]["items"])
        while len(monkeys[i]["items"]) > 0:
            item = monkeys[i]["items"].pop(0)
            left, op, right = monkeys[i]["operation"]
            left = int(item if left == "old" else left)
            right = int(item if right == "old" else right)
            if op == "+":
                item = left + right
            elif op == "*":
                item = left * right
            item = item // 3
            if not item % monkeys[i]["divisor"]:
                monkeys[monkeys[i]["true"]]["items"].append(item)
            else:
                monkeys[monkeys[i]["false"]]["items"].append(item)

inspections = [monkey["inspections"] for monkey in monkeys]
inspections.sort()
print(inspections[-1] * inspections[-2])