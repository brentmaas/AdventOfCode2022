monkeys = {}
answers = {}
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        spl = line.split(" ")
        monkey = spl[0][:-1]
        if not monkey == "humn":
            if len(spl) == 2:
                answers[monkey] = int(spl[1])
            else:
                monkeys[monkey] = spl[1:]

run = True
while run:
    run = False
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
            monkeys.pop(monkey)
            run = True

toanswer = monkeys["root"][2] if monkeys["root"][0] in answers else monkeys["root"][0]
answer = answers[monkeys["root"][0] if monkeys["root"][0] in answers else monkeys["root"][2]]
while not toanswer == "humn":
    left, op, right = monkeys[toanswer]
    newtoanswer = monkeys[toanswer][2] if monkeys[toanswer][0] in answers else monkeys[toanswer][0]
    if op == "+":
        answer -= answers[left] if left in answers else answers[right]
    elif op == "-":
        if left == newtoanswer:
            answer += answers[right]
        else:
            answer = answers[left] - answer
    elif op == "*":
        answer //= answers[left] if left in answers else answers[right]
    elif op == "/":
        if left == newtoanswer:
            answer *= answers[right]
        else:
            answer = answers[left] // answer
    toanswer = newtoanswer
print(answer)