# copy-setup
import sys
INF = float('inf')
input = lambda: sys.stdin.readline().rstrip()
def iinput(): return list(map(int, input().split()))
def debug(*ss): print("\n".join(map(lambda s:f"\t{s} = {globals()[s] if s in globals() else locals()[s]}", ss)))

# infinite
INF = float('inf')

# floats
.5
1.

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
next(input)
n, k = map(int, next(input).split())

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
edges = [[] for _ in range(N)]
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
from collections import deque # (pass)
N = 123
START = 0
edges = [[] for _ in range(N)]
seen = [False] * N
todo = deque([START]) # ([START])
while todo:
    v1 = todo.pop()
    for v2 in edges[v1]:
        if seen[v2]: continue
        todo.appendleft(v2) # (todo.append(v2))
