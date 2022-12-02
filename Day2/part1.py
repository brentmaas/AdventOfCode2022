score = 0
winkey = {'A': {'X': 3, 'Y': 6, 'Z': 0}, 'B': {'X': 0, 'Y': 3, 'Z': 6}, 'C': {'X': 6, 'Y': 0, 'Z': 3}}
scorekey = {'X': 1, 'Y': 2, 'Z': 3}
with open("Input.txt", "r") as f:
    while l := f.readline():
        opponent = l[0]
        you = l[2]
        score += winkey[opponent][you] + scorekey[you]
print(score)