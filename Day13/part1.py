packets = [[]]
with open("Input.txt", "r") as f:
    while line := f.readline():
        if line == "\n":
            packets.append([])
        else:
            packets[-1].append(eval(line.rstrip()))

def compare(left, right):
    if type(left) == int and type(right) == int:
        return 1 if left < right else 0 if left == right else -1
    if type(left) == int:
        left = [left]
    if type(right) == int:
        right = [right]
    for j in range(min(len(left), len(right))):
        c = compare(left[j], right[j])
        if c != 0:
            return c
    return 1 if len(left) < len(right) else 0 if len(left) == len(right) else -1

packetsum = 0
for i in range(len(packets)):
    if compare(packets[i][0], packets[i][1]) > 0:
        packetsum += i + 1
print(packetsum)