fs = {}
wd = []

def get_dir():
    dir = fs
    for d in wd:
        dir = dir[d]
    return dir

with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        cwd = get_dir()
        if line.startswith("$ cd"):
            dir = line.split(" ")[2]
            if dir == "/":
                wd = []
            elif dir == "..":
                wd.pop()
            else:
                if not dir in cwd:
                    cwd[dir] = {}
                wd.append(dir)
        elif not line.startswith("$"):
            val, filename = line.split(" ")
            if not filename in cwd:
                if val == "dir":
                    cwd[filename] = {}
                else:
                    cwd[filename] = val

sizesum = 0
def calc_sizes(dir):
    global sizesum
    size = 0
    for f in dir:
        if type(dir[f]) == dict:
            size += calc_sizes(dir[f])
        elif not f == "_size":
            size += int(dir[f])
    dir["_size"] = size
    if size <= 100000:
        sizesum += size
    return size

calc_sizes(fs)
print(sizesum)