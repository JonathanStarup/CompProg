import sys
lines = sys.stdin.read().splitlines()
output = []

r1, c1, r2, c2 = map(lambda x: int(x)-1, lines[0].split())

#rook
if r1 == r2 or c1 == c2:
    output.append(1)
else:
    output.append(2)

#bishop
if (r1 + c1) % 2 != (r2 + c2) % 2:
    output.append(0)
elif abs(r1-r2) == abs(c1-c2):
    output.append(1)
else:
    output.append(2)

#king
output.append(max(abs(r1-r2), abs(c1-c2)))

print(" ".join(map(str, output)))