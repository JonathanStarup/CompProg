# copy-setup
import sys
input = iter(sys.stdin.read().splitlines())
def ii(): return int(next(input))
def iii(): return list(map(int, next(input).split()))

# infinite
INF = float('inf')

# floats
.5
1.

# scope
for i in range(123):
    pass
print(i)

# Other notes
# https://github.com/kth-competitive-programming/kactl

# 2d distance and norm
from math import hypot
x1, y1, x2, y2  = 0, 1, 5, 4
hypot(x2-x1, y2-y1)

# flush print (doenst work with end='')
def print(*s): print(*s, flush=True)
print("hey")
import sys
sys.stdout.flush()

# debug things
def debug(*ss): print("\n".join(map(lambda s:f"\t{s} = {globals()[s] if s in globals() else locals()[s]}", ss)))

# Input (slower, non-alloc)
import sys
#def input(): return sys.stdin.readline().rstrip()
input = lambda: sys.stdin.readline().rstrip()
def iinput(): return list(map(int, input().split()))

# Input (faster, in-memory)
import sys
input = iter(sys.stdin.read().splitlines())
def iinput(): return list(map(int, next(input).split()))
next(input)
n, k = iinput()

# unfold
lst = [1, 2, 3] 
print(*lst)

# reverse range (no allocation)
range(100)[::-1]

# memoization
import functools
@functools.lru_cache(maxsize=None)
def rec(x): 1 if x == 1 or x ==2 else rec(x-1) + rec(x-2)

# queues
from collections import deque
queue = deque()
queue.append(2)
queue.appendleft(2)
queue.popleft()
queue.pop()

# priority queue
from heapq import heappop, heappush, heapify

# count things
from collections import Counter
cnt = Counter("DKLVFAHKLGASFLG")
cnt["A"]
cnt.most_common()
cnt.items()

from collections import defaultdict
d = defaultdict(lambda: "hej") # default value is "hej"

# Topsort
N = 123
edges = [[] for _ in range(N)] # adjencency list
indeg = [0] * N
todo = [i for i in range(N) if indeg[i] == 0]
topsort = []
while todo:
    v1 = todo.pop()
    topsort.append(v1)
    for v2 in edges[v1]:
        indeg[v2] -= 1
        if indeg[v2] == 0:
            todo.append(v2)
if len(topsort) != N:
    # cycle
    pass

# BFS / (DFS)
from collections import deque # ()
N = 123
START = 0
edges = [[] for _ in range(N)]
seen = [False] * N
todo = deque([START]) # ([START])
while todo:
    v1 = todo.pop()
    if seen[v1]: continue
    seen[v1] = True
    for v2 in edges[v1]:
        if seen[v2]: continue
        todo.appendleft(v2) # (todo.append(v2))

# FloydWarshall
INF = float('inf')
N = 123
edges = [[0] * N for _ in range(N)] # matrix with weights(+/-) or INF
for i in range(N): edges[i][i] = min(edges[i][i], 0)
for k in range(N):
    for i in range(N):
        for j in range(N):
            if edges[i][k] != INF and edges[k][j] != INF:
                new_d = max(edges[i][k] + edges[k][j], -INF) # why max? 
                edges[i][j] = min(edges[i][j], new_d)
for k in range(N): # skip if pos edges
    if edges[k][k] < 0:
        for i in range(N):
            for j in range(N):
                if edges[i][k] != INF and edges[k][j] != INF:
                    edges[i][j] = -INF
