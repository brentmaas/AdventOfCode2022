sum = 0
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        c1 = line[:len(line)//2]
        c2 = line[len(line)//2:]
        for i in c1:
            if i in c2:
                if i >= 'a':
                    sum += ord(i) - ord('a') + 1
                else:
                    sum += ord(i) - ord('A') + 27
                break
print(sum)