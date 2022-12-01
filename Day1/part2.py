elves = []
with open("Input.txt", "r") as f:
    cal = 0
    while line := f.readline():
        if line == "\n":
            elves.append(cal)
            cal = 0
        else:
            cal += int(line.rstrip())
    elves.append(cal)
top3 = 0
for i in range(3):
    top3 += elves.pop(elves.index(max(elves)))
print(top3)