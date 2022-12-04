overlapping = 0
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        left, right = line.split(",")
        left_start, left_end = [int(i) for i in left.split("-")]
        right_start, right_end = [int(i) for i in right.split("-")]
        if not ((left_start < right_start and left_end < right_start) or (right_start < left_start and right_end < left_start)):
            overlapping += 1
print(overlapping)