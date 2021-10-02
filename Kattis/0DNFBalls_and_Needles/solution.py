import sys
lines = sys.stdin.read().splitlines()
max_index = 1_000

k = int(lines[0])
points = {}

for line in range(1, k+1):
    x1, y1, z1, x2, y2, z2 = map(int, lines[line].split())
    points[(x1, y1)] = points.get((x1, y1), {})
    points[(x1, y1)][z1] = points[(x1, y1)].get(z1, [])
    points[(x1, y1)][z1].append((x2, y2, z2, False, False))

    points[(x2, y2)] = points.get((x2, y2), {})
    points[(x2, y2)][z2] = points[(x2, y2)].get(z2, [])
    points[(x2, y2)][z2].append((x1, y1, z1, False, False))


def dfs3d(x, y, z):
    pass
    

for (x1, y1) in points.keys():
    for z1 in points[(x1, y1)].keys():
        (x2, y2, z2, xyz_seen, xy_seen) = points[(x1, y1)][z1]
