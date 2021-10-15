import sys
INF = float('inf')
input = iter(sys.stdin.read().splitlines())
def iinput(): return map(int, next(input).split())
def debug(*ss): print("  >"+" ".join(map(lambda s:f"{s:>8} = {globals()[s] if s in globals() else locals()[s]:<10}", ss)))

N, M = iinput()
F = list(iinput())
IGNORE, ASSIGN, USE = 0, 1, 2
edges = [[] for _ in range(N)]
edges_reverse = [[] for _ in range(N)]
for _ in range(M):
    a, b = iinput()
    edges[a-1].append(b-1)
    edges_reverse[b-1].append(a-1)

assignable = [False] * N
todo = [i for i in range(N) if F[i] == ASSIGN]
while todo:
    v1 = todo.pop()
    if assignable[v1]: continue
    assignable[v1] = True
    for v2 in edges[v1]:
        if assignable[v2]: continue
        todo.append(v2)

cool = [0] * N
todo = [v for v in range(N) if (F[v] == USE and assignable[v])]
while todo:
    v1 = todo.pop()
    if cool[v1] == 1: continue
    cool[v1] = 1
    if F[v1] == ASSIGN: continue
    for v2 in edges_reverse[v1]:
        if (not assignable[v2]) or cool[v2] == 1: continue
        todo.append(v2)
print(*cool, sep = "\n")