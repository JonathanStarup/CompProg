from sys import stdin
from math import pi
from math import sqrt
lines = stdin.read().splitlines()
output = []
def out_str(n):
    return f'{n:.2f}'

for line_index in range(len(lines) - 1):
    r, h, s = map(int, lines[line_index].split())
    half_circle = pi * r
    side =  sqrt(h*h + r*r)
    need = 2 * side + half_circle
    total = (need * (100.0+s)) / 100.0
    output.append(out_str(total))

print("\n".join(output))