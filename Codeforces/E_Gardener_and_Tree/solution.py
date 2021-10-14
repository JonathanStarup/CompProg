import sys
from collections import deque
#INF = float('inf')
lines = iter(sys.stdin.read().splitlines())
#def debug(*ss): print("\n".join(map(lambda s:f"\t{s} = {globals()[s] if s in globals() else locals()[s]}", ss)))

TESTS = int(next(lines))
for _ in range(TESTS):
    next(lines)
    N, K = map(int, next(lines).split())
    edges = [[] for _ in range(N)]
    indeg = [0] * N
    for _ in range(N-1):
        v1_1, v2_1 = map(int, next(lines).split())
        v1, v2 = v1_1 - 1, v2_1 - 1
        edges[v1].append(v2)
        edges[v2].append(v1)
        indeg[v1] += 1
        indeg[v2] += 1
    
    todo = deque([i for i in range(N) if indeg[i] <= 1])
    cut_step = [1] * N
    while todo:
        v1 = todo.pop()
        for v2 in edges[v1]:
            indeg[v2] -= 1
            if indeg[v2] == 1:
                cut_step[v2] = cut_step[v1] + 1
                todo.appendleft(v2)
    left = N
    for v in range(N):
        if cut_step[v] <= K:
            left -= 1
    print(left)