score = 0
winkey = {'A': {'X': 3, 'Y': 6, 'Z': 0}, 'B': {'X': 0, 'Y': 3, 'Z': 6}, 'C': {'X': 6, 'Y': 0, 'Z': 3}}
movekey = {'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'}, 'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'}, 'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'}}
scorekey = {'X': 1, 'Y': 2, 'Z': 3}
with open("Input.txt", "r") as f:
    while l := f.readline():
        opponent = l[0]
        you = l[2]
        move = movekey[opponent][you]
        score += winkey[opponent][move] + scorekey[move]
print(score)