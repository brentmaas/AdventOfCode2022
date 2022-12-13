packets = [[[2]], [[6]]]
with open("Input.txt", "r") as f:
    while line := f.readline():
        if line != "\n":
            packets.append(eval(line.rstrip()))

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

for _ in range(len(packets) - 1):
    for i in range(len(packets) - 1):
        if compare(packets[i], packets[i+1]) < 0:
            packets[i], packets[i+1] = packets[i+1], packets[i]

print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))