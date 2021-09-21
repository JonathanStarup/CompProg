import sys
lines = sys.stdin.read().splitlines()
max_index = 1_000

k = int(lines[0])
points = {}
# idea: nested dicts, combined size 50k


for line in range(1, k+1):
    x1, y1, z1, x2, y2, z2 = map(int, lines[line].split())

