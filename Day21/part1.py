monkeys = {}
answers = {}
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        spl = line.split(" ")
        monkey = spl[0][:-1]
        if len(spl) == 2:
            answers[monkey] = int(spl[1])
        else:
            monkeys[monkey] = spl[1:]

while not "root" in answers:
    for monkey in [monkey for monkey in monkeys]:
        left, op, right = monkeys[monkey]
        if left in answers and right in answers:
            left = answers[left]
            right = answers[right]
            if op == "+":
                ans = left + right
            elif op == "-":
                ans = left - right
            elif op == "*":
                ans = left * right
            elif op == "/":
                ans = left // right
            answers[monkey] = ans
print(answers["root"])