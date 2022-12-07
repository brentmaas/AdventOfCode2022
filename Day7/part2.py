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

sizes = []
def calc_sizes(dir):
    global sizes, needed
    size = 0
    for f in dir:
        if type(dir[f]) == dict:
            size += calc_sizes(dir[f])
        elif not f == "_size":
            size += int(dir[f])
    dir["_size"] = size
    sizes.append(size)
    return size

calc_sizes(fs)
needed = int(fs["_size"]) - 40000000
print(min([size for size in sizes if size >= needed]))