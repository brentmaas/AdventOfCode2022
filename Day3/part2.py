groups = [[]]
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        if len(groups[-1]) < 3:
            groups[-1].append(line)
        else:
            groups.append([line])
sum = 0
for group in groups:
    for i in group[0]:
        if i in group[1] and i in group[2]:
            if i >= 'a':
                sum += ord(i) - ord('a') + 1
            else:
                sum += ord(i) - ord('A') + 27
            break
print(sum)