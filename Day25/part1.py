def snafu_to_dec(num):
    val = 0
    for c in num:
        val *= 5
        if c == "=":
            val -= 2
        elif c == "-":
            val -= 1
        else:
            val += int(c)
    return val

def dec_to_snafu(num):
    base5 = []
    while num > 0:
        base5 = [num % 5] + base5
        num //= 5
    for i in range(len(base5) - 1, -1, -1):
        if base5[i] >= 3:
            if base5[i] == 3:
                base5[i] = -2
            elif base5[i] == 4:
                base5[i] = -1
            if i > 0:
                base5[i-1] += 1
            else:
                base5 = [1] + base5
            while 5 in base5:
                j = base5.index(5)
                base5[j] = 0
                if j == 0:
                    base5 = [1] + base5
                else:
                    base5[j-1] += 1
    val = ""
    for i in base5:
        if i == -2:
            val += "="
        elif i == -1:
            val += "-"
        else:
            val += str(i)
    return val

snafusum = 0
with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        snafusum += snafu_to_dec(line)
print(dec_to_snafu(snafusum))