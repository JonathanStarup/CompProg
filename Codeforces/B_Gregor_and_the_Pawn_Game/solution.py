from sys import stdin
lines = stdin.read().splitlines()
output = []

tests = int(lines[0])
test = 0
line = 1
while test < tests:
    n = int(lines[line])
    check = lambda x: x == "1"
    e_pawns = list(map(check, lines[line + 1]))
    g_pawns = list(map(check, lines[line + 2]))
    line += 3
    test += 1

    goals = 0
    for col in range(n):
        if g_pawns[col]:
            if col > 0 and e_pawns[col-1]:
                goals += 1
            elif not e_pawns[col]:
                e_pawns[col] = False
                goals += 1
            elif col < n -1 and e_pawns[col + 1]:
                e_pawns[col + 1] = False
                goals += 1
    output.append(str(goals))
print("\n".join(output))

