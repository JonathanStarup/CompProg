import sys
INF = float('inf')
input = iter(sys.stdin.read().splitlines())
def iinput(): return map(int, next(input).split())
#def debug(*ss): print("  >"+" ".join(map(lambda s:f"{s:>8} = {globals()[s] if s in globals() else locals()[s]}", ss)))

N = int(next(input))
edges = [list(map(lambda x: 1 if x == "1" else INF, next(input))) for _ in range(N)]
M = int(next(input))
path = list(map(lambda x: x-1, iinput()))

for i in range(N): edges[i][i] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if edges[i][k] != INF and edges[k][j] != INF:
                new_d = edges[i][k] + edges[k][j]
                edges[i][j] = min(edges[i][j], new_d)
res = [path[0]]
for v in range(2, len(path)):
    if edges[res[-1]][path[v]] < edges[res[-1]][path[v-1]] + edges[path[v-1]][path[v]]:
        res.append(path[v-1])
res.append(path[-1])
print(len(res))
print(*map(lambda x: x+1, res), end = '\n')
